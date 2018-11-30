# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:26:47 2018

@author: kissaki
"""


'''
    POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
    Host: fanyi.youdao.com
    Connection: keep-alive
    Content-Length: 202
    Accept: application/json, text/javascript, */*; q=0.01
    Origin: http://fanyi.youdao.com
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
    DNT: 1
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Referer: http://fanyi.youdao.com/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
    Cookie: OUTFOX_SEARCH_USER_ID=-1520622950@10.168.8.61; JSESSIONID=aaaZKPs87y5qvb_uOzvyw; OUTFOX_SEARCH_USER_ID_NCOO=1740825838.7348733; ___rl__test__cookies=1537957471156
    
    i={需要翻译部分(编码)}&from={语言一(默认AUTO)}&to={语言二(默认AUTO)}&smartresult=dict&client=fanyideskweb&salt=1537957471181&sign=bf978625b3a0a4e6754805353fb6f1b5&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
'''



import random
import urllib
from urllib import request

trasUrlList = []


user_agent_list = [
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
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


lang = {
    'chinese': 'zh-CHS',
    'english': 'en',
    'japanese': 'ja',
}


trasUrlDic = {
    # 有道翻译
    'youdao': 'http://www.youdao.com/',
    # google翻译
    'google': 'https://translate.google.cn/',
    # 百度翻译
    'baidu': 'https://fanyi.baidu.com/',
    # 爱词霸
    'iciba': 'http://fy.iciba.com/',
}

# 创建Url列表
def makeTrasUrlList():
    for var in trasUrlDic.keys():
        trasUrlList.append(var)

    # print(trasUrlList)

# 翻译模式添加函数区
def appendUrlDic():
    pass

# 翻译模式选择区
def trasSelect(Dic,urlList):
    print('请选择：')
    # 打印出所有的翻译工具
    index = 1
    # for var in Dic.keys():
    #     print(str(index) + '.' + var, end = ' '*4)
    #     index += 1
    print('input name! Please')
    # 按顺序打印出List里的值
    for var in trasUrlList:
        print(str(index) + '.' + var, end = ' ' * 4)
        index += 1
    try:
        def Select(var):
            if (var in Dic):
                print(Dic[var])
    except KeyError:
        print('Return To def Select()')
    # 定义全局变量selection
    global selection
    selection = input()
    trasfunction(selection)











# 翻译功能区
def trasfunction(selection):
    url = trasUrlDic[selection]
    # zwMode = int(input('\n1,中 -> 外\t2.外 -> 中\t'))
    '''
    if (zwMode == 1):
        mode1 = int(input('1.中 -> 英\t2.中 -> 日\t3.自动检测语言\t'))
        if (mode1 == 1):
            change = '&from=zh-CHS&to=en'
        elif (mode1 == 2):
            change = '&from=zh-CHS&to=ja'
        else :
            change = '&frome=AUTO&to=AUTO'
    elif (zwMode == 2):
        mode2 = int(input('1.英 -> 中\t2.日 -> 中\t3.自动检测语言\t'))
        if (mode2 == 1):
            change = '&from=en&to=zh-CHS'
        elif (mode2 == 2):
            change = '&from=ja&to=zh-CHS'
        else :
            change = '&frome=AUTO&to=AUTO'
    '''
    change = '&frome=AUTO&to=AUTO'
    var = input('输入需翻译内容: ')
    # 内容编码
    _text = urllib.parse.urlencode({'kw': var})[3:]
    # print(_text)
    _i = _text + change
    # print(_i)
    headers = {
        'User-Agent': random.choice(user_agent_list),
        'Host': 'fanyi.youdao.com',
        'Connection': 'keep-alive',
        'Content-Length': 202,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://fanyi.youdao.com',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://fanyi.youdao.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'i':_i
    }
    post(url,headers)


# Post请求区
def post(trasType,headers):
    # print(headers['i'])
    responce = request.Request(trasType,headers = headers)
    print(request.urlopen(responce).read())


# 主功能区
if __name__ == "__main__":
    makeTrasUrlList()
    print('\nMode:\n\tA.进入程序\n\tB.传入翻译网站\n\tC.等待开发')
    mode = input().lower()
    if (mode == 'a'):
        trasSelect(trasUrlDic,trasUrlList)
        youdaotras()
        post(trasType, headers)
    elif (mode == 'b'):
        writeUrl()
    elif (mode == 'c'):
        print('等待开发')
