# -*- coding: utf-8 -*-


import re
import random
import time
import amazon_crawler
import scrapy
from bs4 import BeautifulSoup
from amazon.amazon.items import AmazonItem


# %%


class ProdinfoSpider(scrapy.Spider):
    name = 'prodinfo'
    allowed_domains = ['amazon.com.au']
    start_urls = ['https://www.amazon.com.au/']
    # prod_Id = amazon_crawler.execute(
    #     'https://www.amazon.com.au/s?k=graphics+card&i=computers&rh=n%3A4851683051%2Cn%3A4913341051&dc&crid=1VG7HBIQE1S7M&qid=1589519127&rnid=5367991051&sprefix=gra%2Caps%2C279&ref=sr_pg_1')
    prod_Id = ['B07MQ36Z6L', 'B071CQ4MMK',
               'B07646VQ6T', 'B06XZQMMHJ', 'B07YYZGM51', 'B081L7NHCM']

    def parse(self, response):
        for id in self.prod_Id:
            time.sleep(random.uniform(2, 5))
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            url = 'https://www.amazon.com.au/dp/'+id

            yield scrapy.Request(url, headers={'user-agent': user_agent}, cookies={'i18n-prefs': 'USD', 'skin': 'noskin'}, callback=self.parse_article, encoding='utf-8')

    def parse_article(self, response):
        #response.encoding = 'utf-8'
        items = []
        item = AmazonItem()
        target = response.xpath('//div[@class="pdTab"]/table/tbody/tr')
        model_pattern = re.compile('Model')
        for tag in target:
            try:
                if(tag.css("td.label::text")[0].extract() == 'Brand'):
                    item['Brand'] = tag.css("td.value::text")[0].extract()

                elif(model_pattern.search(tag.css("td.label::text")[0].extract())):
                    item['Model'] = tag.css("td.value::text")[0].extract()

                elif(tag.css("td.label::text")[0].extract() == 'Computer Memory Type'):
                    item['Memory_Type'] = tag.css(
                        "td.value::text")[0].extract()

                elif(tag.css("td.label::text")[0].extract() == 'Graphics Card Ram Size'):
                    item['Ram_Size'] = tag.css("td.value::text")[0].extract()

            except IndexError:
                pass
            continue

        price = response.xpath(
            "//span[@class='a-color-price']")[0].extract()

        item['Price'] = price
        item['Url'] = response.request.url
        items.append(item)
        try:
            return items
        except:
            print('return error')
