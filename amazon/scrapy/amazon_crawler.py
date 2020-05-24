from selenium import webdriver
import time
import random as rnd
import pandas as pd
from openpyxl import load_workbook


def execute(url):
    browser = webdriver.Chrome()
    prod_ids = []
    browser.get(url)
    time.sleep(10)
    while True:
        try:
            prod_div = browser.find_elements_by_xpath(
                "//div[@class='sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32']")
            for prod in prod_div:
                id = prod.get_attribute('data-asin')
                prod_ids.append(id)
            next_btn = browser.find_element_by_xpath("//li[@class='a-last']/a")
            next_btn.click()
            time.sleep(rnd.uniform(3, 5))
        except:
            print("error")
            break
    browser.close()
    return prod_ids


# execute()

#
# data = {'id': prod_ids}
# df = pd.DataFrame(data)

# writer = pd.ExcelWriter('amazon.xlsx', engine='openpyxl')
# df.to_excel(writer, 'Graphics Card ID')
# writer.save()
# writer.close()
