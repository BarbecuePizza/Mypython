import urllib.request
import ssl
import re   # 导入正则表达式
import random
import time

uapools = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/69.0.3497.100 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
]

# 浏览器伪装
def UA():
    ssl._create_default_https_context = ssl._create_unverified_context  # 建立ssl连接
    opener = urllib.request.build_opener()  # 创建opener对象
    thisua = random.choice(uapools)
    UA = ("User-Agent", thisua)
    opener.addheaders = [UA]  # 修改opener中的headers属性
    urllib.request.install_opener(opener)  # 将opener设置为全局生效

# 开始爬取
UA()
url = "http://www.qiushibaike.com"
# 利用 rullib.request.urlopen 直接爬取网页内容
# 爬到内存中
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
"""
# 爬到硬盘的文件中
urllib.request.urlretrieve(url, filename="D:/xxx/xxx")
"""
pat = "<title>(.*?)</title>"  # 正则(.*?)
# 分析网页url和JavaScript
# <div class="content">.*?<span>(.*?)</span>.*?</div>
rst = re.compile(pat, re.S).findall(data)  # 利用re正则对pat进行编译，re.s避免空格消除多行的影响
for i in range(0,len(rst)):
    print(rst[i])
    print("---------")



