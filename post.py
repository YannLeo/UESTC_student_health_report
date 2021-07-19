import requests
import json

def post(info:dict, action:str, flag=0):
    if action == 'evening':
        title = '晚点名'
    elif action == 'morning':
        title = '打卡'
    if flag:
        content = title + '已完成'
    else:
        content = 'error-' + title + '出错，请您自己手动' + title + '，并告知程序发布者代码有bug :-)'
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        "token":info['token'],
        "title":title,
        "content":content
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    requests.post(url,data=body,headers=headers)

