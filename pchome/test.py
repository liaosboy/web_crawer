# import requests
# import json
# import time
# import random as rnd
# import pandas as pd
# from openpyxl import load_workbook
# s = requests.session()

# headers = {

#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
#     "Upgrade-Insecure-Requests": "1"
# }


# def search(cate, key):

#     temp_url = "https://ecshweb.pchome.com.tw/search/v3.3/all/category/{cate}/results?q={key}&page={page}&sort=sale/dc"
#     price = []
#     urls = []
#     name = []
#     describe = []
#     print('這是'+str(key))
#     i = 0

#     # 開始抓取產品資訊
#     while True:
#         try:
#             mydict = {'q': key,
#                       'page': i,
#                       'sort': 'sale/dc'}
#             print('第'+str(i)+'次')
#             url = temp_url.format(cate=cate, key=key, page=i)
#             res = s.get(url, headers=headers, params=mydict)
#             t = res.text
#             print(url)
#             data = json.loads(t)

#             if data['totalPage'] < i:
#                 break

#             for prod in data['prods']:
#                 price.append(prod['price'])
#                 u = "https://mall.pchome.com.tw/prod/"+str(prod['Id'])
#                 urls.append(u)
#                 name.append(prod['name'])
#                 describe.append(prod['describe'])

#             i += 1
#             time.sleep(rnd.uniform(1, 3))
#         except requests.exceptions.RequestException as e:
#             print('request error')
#             break
#         except KeyError as e:
#             print('e')
#             break
#         except Exception as e:
#             print(e)

#     data = {'名稱': name, '規格': describe, '價格': price, '網址': urls}
#     df = pd.DataFrame(data)

#     book = load_workbook('temp.xlsx')
#     writer = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
#     writer.book = book
#     df.to_excel(writer, key)
#     writer.save()
#     writer.close()


# search('DRAD', '顯示卡')
# search('DHAA', '筆記電腦')
# %%
# import re

# # 編譯成 Pattern 對象
# pattern = re.compile(r'hello')

# # 取得匹配結果，無法匹配返回 None
# # 得到匹配結果

# if(pattern.search('whello world! hello')):
#     print('Y')
# --------------------
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
#user_agent = ua.random
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
s = requests.session()
res = s.get('https://www.amazon.com.au/gp/offer-listing/B07MQ36Z6L/ref=dp_olp_new_mbc?ie=UTF8&condition=new',
            cookies={'i18n-prefs': 'AUD', 'lc-acbau': 'en_AU'}, headers={'user-agent': user_agent})
print(res.encoding)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
soup.encode('utf-8')

text = soup.prettify()
f = open('hello.txt', 'w')
f.write(text)
f.flush()
f.close()
