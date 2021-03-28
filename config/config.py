
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
    dns.google
    dns.alidns.com
    dns.rubyfish.cn
    cloudflare-dns.com
DoH server defines in https://tools.ietf.org/html/rfc1035
https://{domain}/dns-query?dns={ base64(DNS wire data) }
'''
DoH = 'dns.alidns.com'
# you should better configure this before you set this dns server as the local server  
DoH_ip = '223.6.6.6'
# DoH_ip = None
# check the SSL cert or not
verify = False