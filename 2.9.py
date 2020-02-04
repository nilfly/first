from urllib import request
import random

proxy_list = [
    {"http": "221.229.252.98:9797"}
]

proxy = random.choice(proxy_list)

proxy_hander = request.ProxyHandler(proxy)

opener = request.build_opener(proxy_hander)

request.install_opener(opener)

req = request.Request("http://www.baidu.com")

reponse = opener.open(req).read().decode()

print(reponse)

