# UESTC_student_clock_in

## Introduction

电子科技大学信通研究生自动打卡，需要挂在后台，并提醒是否成功


## Enviroment

- python >= 3.7
- selenium >= 3.141.0
- requests >= 2.22.0
- opencv-python >= 4.5.2
- numpy >= 1.20.3
- apscheduler >= 3.7.0


## What you need

- 上面的Enviroment
- Firefox浏览器
- Firefox浏览器驱动geckodriver.exe
- 微信/邮箱


## File INFO
```
UESTC_student_clock_in
├── email_.py  发送邮件
├── evening.py 晚点名
├── main.py    定时调用方法
├── morning.py 打卡
├── post.py    发送微信推送
```
## Step
- 配置好以上环境
- 上[这个网站](http://pushplus.hxtrip.com/)，微信扫码登陆，并获得token
- 将代码中省略部分填上自己信息
- 将main.py后缀改为pyw，双击运行，挂在后台

## Functions

### 已实现功能：
- 晚点名
- 邮件或者微信推送是否成功
- 打卡
- 定时晚点名和打卡



### 待实现功能：
- 后台运行
- 运行时不保存图片
- 无窗口运行
- 使用json文件配置
- 开机启动
- 跨操作系统(windows与linux均可)
- 增加验证码成功正确率
- ...

