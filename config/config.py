
# domain -> (ip, time to die)
# 0: stay alive forever
hosts = {                                   
    "www.baidu.com": ("127.0.0.1", 0),
}

# udp address to bind.
# 127.0.0.1 means only receive data from local PC
# 0.0.0.0 means receive any from the network
addr = ('127.0.0.1', 53)

'''
    doh.pub
    dns.alidns.com
    cloudflare-dns.com
DoH server defines in https://tools.ietf.org/html/rfc1035
https://{domain}/dns-query?dns={ base64(DNS wire data) }
'''
DoH = 'dns.alidns.com'