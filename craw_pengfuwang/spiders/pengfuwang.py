# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from craw_pengfuwang.items import CrawPengfuwangItem


class NewsSpider(Spider):
    name = 'pengfuwang'
    # allowed_domains = ['www.qiushibaike.com']
    allowed_domains = ['www.pengfu.com']
    start_urls = ['https://www.pengfu.com/qutu_1.html']

    def parse(self, response):
        sel = Selector(response)
        all_li = sel.xpath('//*[@class="list-item bg1 b1 boxshadow"]')
        print(all_li.__len__())
        # items = []
        if all_li:
            for li in all_li:
                item = CrawPengfuwangItem()
                title = li.xpath('dl/dd/h1/a/text()').extract()
                img_url = li.xpath('dl/dd/div[2]/img/@src').extract()

                item['title'] = title
                item['img_url'] = img_url
                yield item
