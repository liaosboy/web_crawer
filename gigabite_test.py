
from selenium import webdriver
from bs4 import BeautifulSoup
import random as rnd
import random as rnd
import time
import pandas as pd
from openpyxl import load_workbook
import re
import requests


urls = []


def get_Prod_url(keyword):
    urls.clear()
    browser = webdriver.Chrome()
    browser.get("https://24h.pchome.com.tw/")
    time.sleep(rnd.uniform(5, 7))

    print('inputting value')
    search_box = browser.find_element_by_id('keyword')
    search_box.send_keys(keyword)
    time.sleep(rnd.uniform(1, 3))

    print('do click')
    search_btn = browser.find_element_by_id('doSearch')
    search_box.send_keys("\n")
    time.sleep(rnd.uniform(1, 3))

    print('choose category')
    pattern = re.compile(keyword)
    alis = browser.find_elements_by_xpath("//a[@href]")
    for a in alis:
        match = pattern.match(a.text)
        if match:
            a.click()
            break
    time.sleep(rnd.uniform(1, 3))

    print('scroll page')
    for i in range(1, 30):
        browser.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

    print('get source')
    html = browser.page_source
    browser.close()

    soup = BeautifulSoup(html)
    title = soup.find_all('h5', {"class": "prod_name"})
    for h5 in title:
        alis = h5.find_all('a')
        for a in alis:
            url = "https:"+a['href']
            urls.append(url)


def open_prod_page(url):
    '''
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(rnd.uniform(5, 7))
    browser.close()
    '''
    s = requests.session()
    res = s.get(url)
    print(res.text)
    time.sleep(10)


def open_all_url():
    for url in urls:
        open_prod_page(url)


get_Prod_url("顯示卡")
open_all_url()
# get_Prod_url("筆記電腦")


""" data = {"網址": urls}
df = pd.DataFrame(data)

book = load_workbook('pchome_url.xlsx')
writer = pd.ExcelWriter('pchome_url.xlsx', engine='openpyxl')
writer.book = book
df.to_excel(writer, keyword)
writer.save()
writer.close() """
