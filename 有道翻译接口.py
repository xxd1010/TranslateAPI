# -*- coding: utf-8 -*-
'''
@author Kissaki
'''


import hashlib
import random
from urllib import parse
import time

import requests

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


# MD5加密
def MD5_encrypt(t):
    # 创建MD5对象
    m = hashlib.md5()
    m.update(t.encode(encoding = 'utf-8'))
    return m.hexdigest()

# 编码与解码
def UrlCode(s,code):
    """
        编码与解码函数,使用urllib.parse中urlencode/unquote进行编码/解码操作
    """
#    编码:
    if code == 1:
        text = parse.quote(s)
#    解码:
    elif code == 2:
        text = parse.unquote(s)
    return text

# 翻译字符串处理、目标语言选择、添加目标语言
def Lang(s):
#    编码
    EncodeText = UrlCode(s, 1)
#    print(EncodeText)
    '''
        语言代码:
            English         ==>     en
            Chinese         ==>     zh-CHS
            japanese        ==>     ja
            South Korea     ==>     ko
            French          ==>     fr
    '''
    LangDic = {
        1: 'en',
        2: 'zh-CHS',
        3: 'ja',
        4: 'ko',
        5: 'fr',
    }
    var = int(input('1.选择翻译语言 OR 2.添加语言:\t'))
    if var == 1:
        # 选择翻译语言
        print(LangDic)
        lang = LangDic[int(input())]
    elif var == 2:
        # 添加目标语言
        print('添加语言')
    Package(EncodeText, lang)


# 对编码好的text内容与其他内容进行组装
def Package(s, Tolang):
    f = 'fanyideskweb'
    m = '6x(ZHw]mwzX#u0V7@yfwK'
    salt = time.time() + random.randint(1,10)
    FromData = {
        'action': 'an-select',
        'client': 'anyideskweb',
        'doctype': 'json',
        'from': 'Auto',
        'i': s,
        'keyfrom': 'fanyi.web',
        'smartresult': 'dict',
        'to': Tolang,
        'typoResult': 'false',
        'version':'2.1',
        'salt': salt,
        'sign': MD5_encrypt(f + s + str(salt) + m)
    }
    __request__(FromData)



# 发送请求与解析返回值
def __request__(Data):
#    url = 'https://fanyi.youdao.com'
    url = 'http://fanyi.youdao.com/translate?'
    RHeader = {
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

    contents = requests.post(url, headers = RHeader, data = Data)
    # 输出返回状态
    print(contents.text)
    # 有道翻译结果
    # eval函数: 将 json(str) --> dic
    result = (eval(contents.text))['translateResult'][0][0]
    print(result)
    res = ''
    for var in result['tgt'].split(' '):
        res += var
    t = result['src']
    text = UrlCode(t, 2)
    result = UrlCode(res, 2)
    print('原文: %s'% t)
    print('译文: %s'% result)


# main函数区
if __name__ == '__main__':
    print('欢迎使用有道翻译接口\n\t1.中 --> 外\n\t2.外 --> 中')
    select = int(input())
    if select == 1:
        content = input("请输入翻译内容:\t")
        Lang(content)
    elif select == 2:
        content = input("请输入翻译内容:\t")
        Lang(content)
    
#    print('请选择:')
