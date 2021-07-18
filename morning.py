import time
from selenium import webdriver
import math
from email_ import email_
from post import post
import requests
import base64
from PIL import Image
import cv2
import numpy as np
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def set_info():
    url = 'https://idas.uestc.edu.cn/authserver/login?service=https%3A%2F%2Feportal.uestc.edu.cn%3A443%2Fjkdkapp%2Fsys%2FlwReportEpidemicStu%2Findex.do%3Fclient%3Dmobile'
    id = 'xxxxxxxxxxx' # 学号
    pw = 'xxxxxxxxx' # 密码
    name = 'xx' # 姓名
    path = 'D:/Drivers(not delete)/geckodriver.exe'
    option = 'post'
    kind = '打卡'
    info = {'url':url, 'id':id, 'password':pw, 'name':name, 'path':path, 'option':option, 'kind':kind}
    return info


def main(info):
    driver = webdriver.Firefox(executable_path = info['path'])
    driver.get(info['url'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(info['id'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(info['password'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
    time.sleep(1)

    flag = 0
    while not flag:
        captcha_background_url = driver.find_element_by_xpath('//*[@id="img1"]').get_attribute('src')
        captcha_foreground_url = driver.find_element_by_xpath('//*[@id="img2"]').get_attribute('src')
        background, foreground = captcha_background_url.split(',')[1], captcha_foreground_url.split(',')[1]
        background, foreground = base64.b64decode(background), base64.b64decode(foreground)
        with open('./image/background.png', 'wb') as f:
            f.write(background)
        with open('./image/foreground.png', 'wb') as f:
            f.write(foreground)
        target = cv2.imread('./image/foreground.png')
        template = cv2.imread('./image/background.png', 0)
        x = get_pos(template)
        if x == 0:
            x = get_pos_backup(target, template)
        print(x)
        track = get_track(x*240/500)
        flag = slide(driver, track)
    
    # result=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[5]')))
    time.sleep(5)
    # element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[5]')
    # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    element = driver.find_element_by_css_selector('.mint-fixed-button')
    driver.execute_script("arguments[0].click();", element) 
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/button').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
    driver.quit()

    return 1

def get_track(distance):
        '''
        拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
        匀变速运动基本公式：
        v=v0+at
        s=v0t+(1/2)at²
        v²-v0²=2as

        :param distance: 需要移动的距离
        :return: 存放每0.2秒移动的距离
        '''
        # 初速度
        v=0
        # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
        t=0.3
        # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
        tracks=[]
        # 当前的位移
        current=0
        # 到达mid值开始减速
        mid=distance * 5/8

        distance += 10  # 先滑过一点，最后再反着滑动回来
        # a = random.randint(1,3)
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
                a = random.randint(1,3)  # 加速运动
            else:
                a = -random.randint(2,4) # 减速运动

            # 初速度
            v0 = v
            # 0.2秒时间内的位移
            s = v0*t+0.5*a*(t**2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v= v0+a*t

        # 反着滑动到大概准确位置
        for i in range(4):
           tracks.append(-random.randint(1,3))
        # random.shuffle(tracks)
        return tracks


def slide(driver, tracks):

    former = driver.current_url
    slider =driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div')
    # 鼠标点击并按住不松
    webdriver.ActionChains(driver).click_and_hold(slider).perform()
    # 让鼠标随机往下移动一段距离
    webdriver.ActionChains(driver).move_by_offset(xoffset=0, yoffset=100).perform()
    time.sleep(0.15)
    for item in tracks:
        webdriver.ActionChains(driver).move_by_offset(xoffset=item, yoffset=random.randint(-2,2)).perform()
    # 稳定一秒再松开
    time.sleep(0.5)
    webdriver.ActionChains(driver).release(slider).perform()
    time.sleep(2)
    # 随机拿开鼠标
    later = driver.current_url
    if former == later:
        return 0
    else:
        return 1


def get_pos(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    canny = cv2.Canny(blurred, 150, 300)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv2.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        # print(cx, cy, cv2.contourArea(contour), cv2.arcLength(contour, True))
        if 4500 < cv2.contourArea(contour) < 5776 and 320 < cv2.arcLength(contour, True) < 400:
            if cx < 60:
                continue
            x, y, w, h = cv2.boundingRect(contour) # 外接矩形
            return x
    return 0

def get_pos_backup(target, template):
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    target = cv2.cvtColor(target, cv2.COLOR_GRAY2RGB)
    template = cv2.cvtColor(template, cv2.COLOR_GRAY2RGB)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)  # 进行匹配
    x, y = np.unravel_index(result.argmax(), result.shape)  # 通过np转化为数值，就是坐标
    return y

def morning():
    info = set_info()
    start = time.perf_counter()
    flag = 0
    # flag = main(info)
    try:
        flag = main(info)
        end = time.perf_counter()
        print("The opration costs {} senconds.".format(math.ceil(end-start)))
    except:
        pass
    finally:
        if info['option'] == 'post':
            post(info['kind'], flag)
        else:
            email_(info['kind'], flag)

if __name__ == '__main__':
    morning()