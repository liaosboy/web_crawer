import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time
import random
import re

#res = requests.get("https://www.lazada.com.ph/#")
#soup = BeautifulSoup(res.text,"html.parser")
#print(soup.prettify())
#for item in soup.select('.J_FSItemUnit'):
#   print(item.prettify())
from selenium.webdriver import ActionChains


def search(key):
    #proxy = '187.243.253.182:33796'
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=https://' + proxy)


    browser = webdriver.Chrome()


    browser.get('https://www.lazada.com.ph/#')
    time.sleep(random.uniform(7, 12))
    cookies = {
        'name':'x5sec',
        'value':'7b22617365727665722d6c617a6164613b32223a223234336431616561646534663963636163656636323236366165333733393738434f5434672f5946454e32307461614c71664b663067453d227d'
    }
    browser.add_cookie(cookies)#這是反爬蟲用cookies，加入之後就不會被擋，需定時更新。
    textbox = browser.find_element_by_xpath("//input[@id='q']")
    textbox.send_keys(key)
    btn = browser.find_element_by_xpath('//button[@class="search-box__button--1oH7"]')
    btn.click()
    time.sleep(random.uniform(1,3))
    print('get price')
    item_list = browser.find_elements_by_xpath("//div[@class='c2prKC']//a[@title]")
    for item in item_list:
        newpage = webdriver.Chrome()
        link = item.get_attribute('href')
        newpage.get(link)
        newpage.add_cookie(cookies)
        time.sleep(10)



        action = ActionChains(newpage)
        action.move_by_offset(200,100).perform()
        action.click()
        time.sleep(2)

        try:
            atn= newpage.find_element_by_xpath('//div[@class="content-block sfo"]//span[@class="sfo__close"]/i[@class="next-icon next-icon-close next-icon-small"]')
            print('click')
            atn.click()
            btn = newpage.find_element_by_xpath("//div[@class='expand-button expand-cursor']/button")
            print('click')
            btn.click()
        except:
            print('none')




        more = newpage.find_elements_by_xpath('//div[@class="pdp-mod-specification"]//li[@class="key-li"]/span[@class="key-title"]')
        more1 = newpage.find_elements_by_xpath('//div[@class="pdp-mod-specification"]//li[@class="key-li"]/div[@class="html-content key-value"]')
        for i in range(len(more)):
                print(more[i].text)
                print(more1[i].text)
        newpage.close()


        time.sleep(random.uniform(10,20))







search('notebook')
time.sleep(random.uniform(5,12))
search('graphics card')
time.sleep(random.uniform(5,15))
search('motherboard')