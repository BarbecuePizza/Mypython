import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context#建立ssl连接
opener=urllib.request.build_opener()#通过opener获取代理头
UA=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0")
opener.addheaders=[UA]
urllib.request.install_opener(opener)#将opener适用于全局
data=urllib.request.urlopen("http://www.qiushibaike.com").read().decode("utf-8","ignore")
import re #导入正则表达式
pat="<title>(.*?)</title>"
rst=re.compile(pat,re.S).findall(data)#re.s避免空格
print(rst)



