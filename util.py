# http 请求
# 201-08-29
# see 
# https://2.python-requests.org//zh_CN/latest/user/quickstart.html

import requests
import json
import os
from var_dump import var_dump

# post 请求
def post(url, data):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Referer": "http://jinbao.pinduoduo.com/index?page=5",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    response = requests.post(url, data=data, headers=headers)
    return response.text


# 读取目录下所有文件 不含子文件夹
def readDirFile(dir):
    files= os.listdir(dir) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            s.append(file) #每个文件的文本存到list中
    return s
