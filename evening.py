import time
from selenium import webdriver
import math
from email_ import email_
from post import post

    
def main(info:dict):
    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.add_argument("--headless")
    driver = webdriver.Firefox(executable_path = info['path'], options=firefoxOptions)
    driver.get('https://jinshuju.net/f/kDiOo6')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input').send_keys(info['name'])
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input').send_keys(info['id'])
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[6]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[8]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[10]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[12]/div/div[2]/div/div/span/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[14]/div/div/div[2]/div/div/span/div/div/button').click()
    time.sleep(2)
    try:
        a = driver.switch_to.alert
        a.accept()
    except:
        pass
    finally:
        pass
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div/button').click()
    time.sleep(2)
    driver.quit()
    return True


def evening(info):
    # start = time.perf_counter()
    flag = 0
    try:
        flag = main(info['base'])
        # end = time.perf_counter()
        # print("The opration costs {} senconds.".format(math.ceil(end-start)))
    except:
        pass
    finally:
        if info['base']['option'] == 'post':
            post(info['post'], action='evening', flag=flag)
        else:
            email_(info['email'], action='evening', flag=flag)


if __name__ == '__main__':
    evening()