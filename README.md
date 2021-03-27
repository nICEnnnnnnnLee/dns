# DNS Server
[English](/README.md)  [中文](/README_CN.md)  
## WHAT  
A DNS server that uses DoH(DNS over HTTPS) to find the real ip.     
NO extra dependency.  
Python version 3.7+, for `async` is used.  
    
## HOW  
+ Edit config in `config/config.py`.  
```python

# domain -> (ip, time to die)
# 0: stay alive forever
hosts = {                                   
    "www.baidu.com": ("127.0.0.1", 0),
}

# udp address to bind.
# 127.0.0.1 means only receive data from local PC
# 0.0.0.0 means receive any from the network
# 53 is the standard port for a DNS server
addr = ('127.0.0.1', 53)

'''
    doh.pub
    dns.alidns.com
    cloudflare-dns.com
DoH server defines in https://tools.ietf.org/html/rfc1035
https://{domain}/dns-query?dns={ base64(DNS wire data) }
'''
DoH = 'dns.alidns.com'

```

+ Just run it.  
```
python dns.py
```

+ Now you can configure the DNS on your device
![](/assets/dns_config.png)