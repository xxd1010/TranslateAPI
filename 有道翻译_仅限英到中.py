# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:51:33 2018

@author: kissaki
"""

import requests
import random
import time
import hashlib
import json
import urllib.parse



def UrlCode(s,code):
    """
    编码与解码函数,使用urllib.parse中urlencode/unquote进行编码/解码操作
    """
    # 编码
    if code == 1:
        # s = urllib.parse.urlencode({'kw':s})[3:]
        s = urllib.parse.quote_plus(s, encoding= 'utf-8')
    # 解码
    elif code == 2:
        s = urllib.parse.unquote(s)
    return s
def MD5_encrypt(s):
    """
    MD5加密
    """
    md = hashlib.md5()
    md.update(s.encode(encoding='utf-8'))
    return md.hexdigest()

user_agent_list = [
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ',
 'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]
data = {
    'from': 'Auto',
    'to': 'Auto',
    'action': 'an-select',
    'client': 'anyideskweb',
    'doctype': 'json',
    'keyfrom': 'fanyi.web',
    'smartresult': 'dict',
    'typoResult': 'false',
    'version':'2.1'
}
header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '214',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1520622950@10.168.8.61; OUTFOX_SEARCH_USER_ID_NCOO=1740825838.7348733; JSESSIONID=aaaSHSqFcRNwlcPyyBZyw; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1538462788799',
        'DNT': '1',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': random.choice(user_agent_list),
        'X-Requested-With': 'XMLHttpRequest'
    }
url = 'http://fanyi.youdao.com/translate?'
f = 'fanyideskweb'
m = '6x(ZHw]mwzX#u0V7@yfwK'
time = int(time.time() + random.randint(1, 10))

while True:
    content = input('输入翻译内容:')
    content = UrlCode(content, 1)
    sign = f + content + str(time) + m
    data['i'] = content
    data['salt'] = time
    data['sign'] = MD5_encrypt(sign)
    contents = requests.post(url, headers = header, data = data)
    res = UrlCode((eval(json.loads(json.dumps(contents.text))))['translateResult'][0][0]['tgt'], 2).replace('+', ' ')
    print('译:\t%s\n' % res)