from urllib import request
import urllib

wd = {"wd": "北京"}

url = "http://www.baidu.com/s?wd=北京"

# wdd = urllib.parse.urlencode(wd)
reponse = request.urlopen(url).read().decode()

print(reponse)