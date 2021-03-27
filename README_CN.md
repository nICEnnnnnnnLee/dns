# DNS Server
[English](/README.md)  [中文](/README_CN.md)  

## WHAT  
该项目可以建立一个DNS服务器，它使用DoH(DNS over HTTPS)来查询**真实的DNS**     
如果你把它放在本地运行，可以再也不必担心DNS被污染的问题。  
该项目没有额外的第三方依赖。  
该项目需要Python 3.7+ 的运行环境，因为它使用了异步`async`功能  
    
## HOW  
+ 配置 `config/config.py`.  
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

+ 运行程序  
```
python dns.py
```

+ 现在你可以在设备上配置并使用DNS服务器了  
![](/assets/dns_config.png)