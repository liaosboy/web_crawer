
from selenium import webdriver
from bs4 import BeautifulSoup
import random as rnd
import time
import pandas as pd
from openpyxl import load_workbook
import re


urls = []
browser = webdriver.Chrome()
browser.get("https://24h.pchome.com.tw/")
time.sleep(5)
# time.sleep(10)

print('inputting value')
search_box = browser.find_element_by_id('keyword')
search_box.send_keys("顯示卡")

time.sleep(2)

print('do click')
search_btn = browser.find_element_by_id('doSearch')

search_box.send_keys("\n")
time.sleep(5)

print('choose category')
pattern = re.compile(r'顯示卡')
alis = browser.find_elements_by_xpath("//a[@href]")
for a in alis:
    match = pattern.match(a.text)
    if match:
        a.click()
        break
time.sleep(2)

print('scroll page')
for i in range(1, 30):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

print('get source')
html = browser.page_source
browser.close()
soup = BeautifulSoup(html)
title = soup.find_all('h5', {"class": "prod_name"})
for h5 in title:
    alis = h5.find_all('a')
    for a in alis:
        url = a['href']
        urls.append(url)

data = {"網址": urls}
df = pd.DataFrame(data)

#book = load_workbook('pchome_url.xlsx')
writer = pd.ExcelWriter('pchome_url.xlsx', engine='openpyxl')

df.to_excel(writer, "顯示卡")
writer.save()
writer.close()
