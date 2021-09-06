# UESTC_student_clock_in

## Introduction

```diff
- 免责声明：
- 这是本人写的第一个较完整的 *github* 项目，还在学习中。本项目没有收集个人信息的代码和接口，如要使用请放心使用。
- 若使用后被学校发现并处罚，本人不负任何责任。
- 且本项目编写初衷是学习，并非是逃离国家疫情监管，我永远支持国家疫情监管措施。
```

*UESTC* 信通研究生自动打卡与晚点名，并提醒是否成功，需要挂在后台(打卡从 *00:06* 开始且每天只能打一次；晚点名从 *17:01* 开始，*24:00* 结束，可晚点名多次)


***若对本项目感兴趣，可联系本人获得可用的学号与密码，但请勿修改信息，只能供本项目使用，望遵守***

***Email : yangliu991022@163.com***

***QQ: 1070032777***



## Enviroment

- *python* >= 3.7
- *selenium* >= 3.141.0
- *requests* >= 2.22.0
- *opencv-python* >= 4.5.2
- *numpy* >= 1.20.3
- *apscheduler* >= 3.7.0


## What you need

- 适合该项目的 *python* 环境
- *Firefox* 浏览器
- *Firefox* 浏览器驱动 geckodriver.exe
- 微信/邮箱
- 一台装有 *Windows* 系统的不断电的计算机


## File INFO
```
UESTC_student_clock_in/
├── driver/
├────── Firefox-latest.exe 火狐浏览器安装包
├────── geckodriver.exe    火狐浏览器驱动
├── config/
├────── config.json      配置文件，通过修改json文件来实现信息配置
├── email_.py        发送邮件
├── evening.py       晚点名
├── main.py          定时调用方法
├── morning.py       打卡
├── post.py          发送微信推送
├── README.md        项目说明
├── requirements.txt 项目所需环境
├── (background.png) 程序运行中生成的验证码背景图
├── (foreground.png) 程序运行中生成的验证码前景图
```
## Step
- 使用 ./driver/Firefox-latest.exe 安装火狐浏览器
- 下载 [*Anaconda*](https://www.anaconda.com/) 或 [*python*](https://www.python.org/)
- 检查 *python* 环境是否安装以上包。若没有，可在本项目路径下运行 ```pip install -r requirements.txt```
- 上[这个网站](http://pushplus.hxtrip.com/)，微信扫码登陆，并获得 token
- 在 config文件夹下 json 文件中修改配置或增加新的 json 文件，具体步骤见 [Config setting step 章节](#config-setting)
- 将 *main.py* 后缀改为 *pyw* ，双击运行，挂在后台

## <span id="config-setting">Config setting step</span>
json 文件格式如下：
```
{
    "base":{
        "id": "XXXXXXXXXXXXXXXX",
        "password": "xxxxxxxxxxxxxxxx",
        "name": "xxx",
        "path": "./driver/geckodriver.exe",
        "option": "post"
    },

    "post":{
        "token": "xxxxxxxxxxxxx"
    },

    "email":{
        "mail_realm_name": "smpt.qq.com",
        "mail_port": 465,
        "mail_user": "xxxxxxxx",
        "mail_pass": "xxxxxxxxxx",
        "sender": "xxxxxxxxxxxxx",
        "receiver": "xxxxxxxxxx",
        "sender_name": "xx"
    }

    "time":{
        "morning":{
            "hour": 0,
            "minute": 15
        },
        "evening":{
            "hour": 17,
            "minute": 5
        }
    }
}
```

### **base : 基本设定**
- id : 学号
- password : 密码
- name : 真实姓名
- path : 浏览器 driver 的 path
- option : 提醒为微信推送或邮箱，分别对应 ```"post"``` 与 ```"email"```

### **post : 微信推送设定**
- token : [微信推送网站](http://pushplus.hxtrip.com/message)上显示的 token

### **email : 邮件推送设定**
- mail_realm_name : 邮箱服务器域名，默认为 QQ 邮箱，为 ```"smpt.qq.com"```
- mail_port : 邮箱服务器端口，若为 QQ 邮箱，则可为465或587
- mail_user : 邮箱登陆名，若为 QQ 邮箱，则为 QQ 号
- mail_pass : 邮箱开启 STMP 服务时设置的授权码
- sender : 发送方邮箱
- reciver : 接收方邮箱
- sender_name : 发送邮件时的发件人与收件人

### **time : 时间设定**
- morning
    - hour : 打卡时间点-小时
    - minute : 打卡时间点-分钟
- evening
    - hour : 晚点名时间点-小时
    - minute : 晚点名时间点-分钟

## Functions

### 已实现功能：
- 晚点名
- 邮件或者微信推送是否成功
- 打卡
- 定时晚点名和打卡
- 后台运行
- 无窗口运行
- 使用 json 文件配置

### 待实现功能：

- 封装成 exe
- 编写图形界面
- 运行时不保存图片
- 开机启动
- 跨操作系统( *Windows* 与 *Linux* 均可)
- 增加验证码成功正确率
- 尝试实现交互，打卡失败可对程序发信号，使其再次打卡
- bug report
- ...

