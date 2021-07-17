import time
from selenium import webdriver
import math
from email_ import email_
from post import post


def set_info():
    url = 'https://jinshuju.net/f/kDiOo6'
    id = 'xxxxxxx' # 学号
    pw = 'xxxxxxxxxxx'
    name = 'xx'
    path = 'D:/Drivers(not delete)/chromedriver.exe'
    option = 'post'
    info = {'url':url, 'id':id, 'password':pw, 'name':name, 'path':path, 'option':option}
    return info
    
def main(info:dict):
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument("--proxy-server=http://192.168.50.238:10152")
    driver = webdriver.Chrome(executable_path = info['path'], chrome_options = chromeOptions)
    driver.get(info['url'])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input').send_keys(info['name'])
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input').send_keys(info['id'])
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[6]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[8]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[10]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[12]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[14]/div/div/div[2]/div/div/span/div/div/button').click()
    # time.sleep(2)
    # a = driver.switch_to.alert     #  新方法，切换alert
    # a.accept()                       # 确认，相当于点击[确定]按钮
    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div/button').click()
    time.sleep(10)
    return True


def evening():
    info = set_info()
    start = time.perf_counter()
    flag = 0
    try:
        flag = main(info)
        end = time.perf_counter()
        print("The opration costs {} senconds.".format(math.ceil(end-start)))
    except:
        pass
    finally:
        if info['option'] == 'post':
            post(flag)
        else:
            email_(flag)


if __name__ == '__main__':
    evening()