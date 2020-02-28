import requests
from bs4 import BeautifulSoup
import json

def getsong():
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    for a in range(5):
        params={
            'ct': '24',
            'qqmusic_ver': '1298',
            'remoteplace': 'txt.yqq.lyric',
            'searchid': '99154877725421559',
            'aggr': '0',
            'catZhida': '1',
            'lossless': '0',
            'sem': '1',
            't': '7',
            'p': str(a+1),
            'n': '5',
            'w': '周杰伦',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        res=requests.get(url,headers=headers,params=params)
        js1=res.json()
        contents=js1['data']['lyric']['list']
        for i in contents:
            content=i['content']
            print(str(content))

