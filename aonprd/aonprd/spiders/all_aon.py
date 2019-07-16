# -*- coding: utf-8 -*-
import scrapy
import re

class NameLinkItem(scrapy.Item):
    name = scrapy.Field,
    link = scrapy.Field,

class AllAonSpider(scrapy.Spider):
    name = 'all_aon'
    start_urls = ["file:///C:/Users/mroga/PycharmProjects/scrapers/aonprd/aonprd/aon_prd_data.html"]

    def parse(self, response):

        links = response.css('a::attr(href)').extract()[28:-2]
        names = response.css('a::text').extract()[27:]

        items = []
        item_length = range(len(links))
        items.append({
            'links': links[0],
            'category': re.search(r"[A-Z]+.+\.aspx", links[0]),
            'name': names[0]
        })

        # for idx in item_length:
        #     items.append({
        #         'links': links[idx],
        #         'category': re.search(r"([A-Z])\w+", links[idx]),
        #         'name': names[idx]
        #     })

        return items

