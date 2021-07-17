import smtplib
from email.mime.text import MIMEText
from email.header import Header

def email_(flag=0):
    mail_host="smtp.qq.com"#设置的邮件服务器host必须是发送邮箱的服务器，与接收邮箱无关。
    mail_user="1070032777"#qq邮箱登陆名
    mail_pass="wwfqrvngyibvbgaf" #开启stmp服务的时候并设置的授权码，注意！不是QQ密码。
  
    sender='1070032777@qq.com'#发送方qq邮箱
    receivers=['yangliu991022@163.com']#接收方qq邮箱
  
    message=MIMEText('晚点名','plain','utf-8')
    message['From']=Header("yl",'utf-8') #设置显示在邮件里的发件人
    message['To']=Header("yl",'utf-8') #设置显示在邮件里的收件人

    if flag:
        subject = '晚点名已点'
    else:
        subject = '晚点名点名出错'
    message['Subject']=Header(subject,'utf-8') #设置主题和格式
  
    try:
        smtpobj=smtplib.SMTP_SSL(mail_host,465) #本地如果有本地服务器，则用localhost ,默认端口２５,腾讯的（端口465或587）
        smtpobj.set_debuglevel(1)
        smtpobj.login(mail_user,mail_pass)#登陆QQ邮箱服务器
        smtpobj.sendmail(sender,receivers,message.as_string())#发送邮件
        print("邮件发送成功")
        smtpobj.quit()#退出
    except smtplib.SMTPException as e :
        print("Error:无法发送邮件")
        print(e)

if __name__ == '__main__':
    email_()