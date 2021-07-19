import smtplib
from email.mime.text import MIMEText
from email.header import Header

def email_(info:dict, action:str, flag=0):
    receivers=[info['receiver']]
    if action == 'evening':
        title = '晚点名'
    elif action == 'morning':
        title = '打卡'
  
    message=MIMEText(title, 'plain', 'utf-8')
    message['From']=Header(info['sender_name'],'utf-8')
    message['To']=Header(info['sender_name'],'utf-8')

    if flag:
        subject = title + '已完成'
    else:
        subject = 'error-' + title + '出错，请您自己手动' + title + '，并告知程序发布者代码有bug :-)'
    message['Subject']=Header(subject,'utf-8')
  
    try:
        smtpobj=smtplib.SMTP_SSL(info['mail_realm_name'], info['mail_port'])
        smtpobj.set_debuglevel(1)
        smtpobj.login(info['mail_user'], info['mail_pass'])
        smtpobj.sendmail(info['sender'], receivers, message.as_string())
        smtpobj.quit()
    except smtplib.SMTPException as e:
        pass

if __name__ == '__main__':
    email_()