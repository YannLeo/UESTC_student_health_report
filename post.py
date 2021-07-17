import requests
import json

def post(flag=0):
    token = 'xxxxxxxxxxxxxxxxxx' #在pushpush网站中可以找到
    title= '晚点名' #改成你要的标题内容
    if flag:
        content = '晚点名已点' #改成你要的正文内容
    else:
        content = 'error 晚点名出错'
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        "token":token,
        "title":title,
        "content":content
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    requests.post(url,data=body,headers=headers)

