# http 请求
# 201-08-29
# see https://2.python-requests.org//zh_CN/latest/user/quickstart.html
# 
import requests
import json


def post(url, data):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Referer": "http://jinbao.pinduoduo.com/index?page=5",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    response = requests.post(url, data=data, headers=headers)
    return response.text

post("http://192.168.0.11/", {"a":1})