#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import asyncio
import socket
import base64
import time
from util import dns_helper
from util import http
from config import config


class DNSoverHTTPSProtocol:
    def __init__(self, on_con_lost):
        self.on_con_lost = on_con_lost
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        dns = dns_helper.parse(data)
        if dns is not None:
            checkValidHosts()
            query = dns.query[0]
            if query._name in config.hosts:  # if domain in host table, just reply it
                ip, _ = config.hosts.get(query._name)
                answer = dns_helper.gen_A_response(query._name, ip, id=dns.id)
                self.transport.sendto(answer, addr)
            else:   # if domain not in host table, use DoH
                asyncio.create_task(ask_and_reply(
                    query._name, data, addr, self.transport))

    def connection_lost(self, exc):
        self.on_con_lost.set_result(True)

last_valid_chack_time = 0
def checkValidHosts():
    # we check this for at least 300s a round
    now = int(time.time())
    global last_valid_chack_time
    if now - last_valid_chack_time >= 300:
        last_valid_chack_time = now
        for domain, (_, time_to_die) in list(config.hosts.items()):
            if time_to_die > 0 and now >= time_to_die:
                config.hosts.pop(domain)

async def ask_and_reply(name, data, addr, transport):
    '''
    :param name: domain to query
    :param data: dns packet data
    :param addr: addr to answer
    :param transport: socket's transport, has a write() function
    '''
    try:
        dns_base64 = base64.encodebytes(data).decode().strip('\r\n=')
        res = await http.get(config.DoH, path='/dns-query?dns=' + dns_base64)
        if res and res.statusCode == 200:
            transport.sendto(res.data, addr)
            answers = dns_helper.parse(res.data).answer
            if len(answers) > 0:
                answer = answers[0]
                time_to_die = int(time.time()) + answer._ttl
                ip = answer._rData
                config.hosts[name] = (ip, time_to_die)
    except Exception as e:
        pass


async def main():
    loop = asyncio.get_running_loop()
    on_con_lost = loop.create_future()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: DNSoverHTTPSProtocol(on_con_lost),
        local_addr=config.addr)
    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == '__main__':
    asyncio.run(main())

