from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import time
import requests
import random as rnd
import pandas as pd
import re


urls = []


def get_Prod_url(keyword):
    driver = webdriver.Chrome()  # 開啟Chrome
    driver.get("https://www.aliexpress.com/")  # 前往這個網址
    cookies = {'name': 'xman_t',
               'value': 'vNrsGCCw1yUCDnb0+TZkUzaDuDycld0ENUmxkfB9qthLEDWS1rasClVRVx3So9Q+vpDCuzZ6F/Ymuv0cEHY4bJgtexrSBSuPcGnFEI278tHoIIQXZYkvBVfZW7/ZYUajeiKZkYxcApMNmodMHAuRD0fVxpMVrMK8GxYgSzEbMfao97a4mWOle8m1iQdCyh5KHSC4EbiAHIDSr422BSixCiDGCwCmftP81OIrUga6tSQv4Qnqb9Tw11bfKCURigFn3R3T/FomcD7Z8Sir65q3ZUm0Y4kaJG/Ych9QUgi9ZslkdG+LdbAxf74thNwsB0hK6M4NbQt+0mYN4fg7JuMkFj8B+7uMwp3mMl1KHZJiQi1sAXBHwyOQnDp1BEKnHo9LCYvMHL0uQJN7OKr5vbuUnmfwZUuWiCByjRwOUTfKihKpHBD4P3OWFbNrbSLg0svLwxN8wh3Xyk4GVOc48p64fp6kO6+b8EUAUQaw0AEEBmdDLpHg6h5t4XIO8TH0WqGLrIfKPmLHtQIjwkmPoyNy5apUpCNQZ3Hd7gG3GmDehEHzWA2I80X2ozL92TyVmVc/AO0SOJ/wZd66iP6oIsiTDaTdEBD3p7fBlzU5Tn2pDT+eZG6YUrW1L0nsMnL+haC3hfmCqPrpGWkqMChQSrBjow6kKRLVpl+FHRF1mYh1yEU='}
    # driver.add_cookie(cookies)
    time.sleep(rnd.uniform(1, 3))

    print('inputting value')
    search_box = driver.find_element_by_id('search-key')
    search_box.send_keys(keyword)
    time.sleep(rnd.uniform(5, 8))
    try:
        ad = driver.find_element_by_xpath(
            "//a[@class='close-layer']")  # 若頁面彈出廣告，將他關閉
        ad.click()
    except:
        print('no ad')
    print('do click')

    search_btn = driver.find_element_by_xpath(
        '//*[@id="form-searchbar"]/div[1]/input')
    search_btn.click()  # 執行搜尋
    time.sleep(rnd.uniform(1, 3))

    # 輸入帳號密碼登入
    try:
        email = driver.find_element_by_xpath("//input[@name='fm-login-id']")
        password = driver.find_element_by_xpath(
            "//input[@name='fm-login-password']")
        email.send_keys('b10623009@yuntech.edu.tw')
        time.sleep(2)
        password.send_keys('testpassword')
        time.sleep(rnd.uniform(3, 5))
        # form = driver.find_element_by_xpath("//form[@class='login-form']")
        # form.submit()
        btn = driver.find_element_by_xpath(
            "//button[@class='fm-button fm-submit password-login']")
        print(btn.text)
        btn.click()
    except:
        pass


    print('choose category')
    pattern = re.compile(keyword)
    alis = driver.find_elements_by_xpath("//a[@href]")
    for a in alis:
        match = pattern.match(a.text)
        if match:
            a.click()
            break
    time.sleep(rnd.uniform(1, 3))

    print('scroll page')
    for i in range(1, 5):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

    try:
        ad = driver.find_element_by_xpath(
            "//a[@class='close-layer']")  # 若頁面彈出廣告，將他關閉
        ad.click()
    except:
        print('no ad')

    time.sleep(2)
    print('get source')
    html = driver.page_source
    driver.close()

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('a', {'class': 'item-title'})
    for a in titles:
        url = "https:"+a['href']
        urls.append(url)


def open_prod_page(url):

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(rnd.uniform(2, 5))
    try:
        ad = driver.find_element_by_xpath("//a[@class='next-dialog-close']")
        ad.click()
    except:
        print('no ad')
    time.sleep(1)
    print('scroll page2')

    driver.execute_script(
        'window.scrollTo(0, 1000)')

    time.sleep(rnd.uniform(2, 5))
    specification = driver.find_element_by_xpath(
        "//li[@ae_button_type='tab_specs']")
    specification.click()
    time.sleep(rnd.uniform(1, 3))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(rnd.uniform(1, 3))
    title = soup.find('title')
    title_len = len(title)-25
    name = title.text[:title_len]
    print('product name:'+name)
    time.sleep(rnd.uniform(3, 5))
    specify = soup.find_all('li', {'class': 'product-prop line-limit-length'})
    print(specify)
    for li in specify:
        s_name = li.find('span', {'class': 'property-title'})
        s_vaule = li.find('span', {'class': 'property-desc line-limit-length'})
        print(s_name.text+":"+s_vaule.text)
        print("--------------------------")

    driver.close()
    time.sleep(rnd.uniform(1, 3))


def open_all_url():
    for url in urls:
        open_prod_page(url)


get_Prod_url("motherboard")  # 輸入要查詢的關鍵字
open_all_url()
