# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql

from craw_pengfuwang.util.db import con
from craw_pengfuwang.rabbitmq import producer
from craw_pengfuwang.util import down_img


class CrawPengFuWangPipeline(object):
    def process_item(self, item, spider):
        return item

    def checkTitleFromDb(self, title):
        cursor = con.cursor()
        sqlStr = "select title from pengfu_news where title ='" + title[0] + "'"
        cursor.execute(sqlStr)
        d = cursor.fetchone()
        return d

    def process_item(self, item, spider):
        # 使用cursor()方法获取操作游标
        cursor = con.cursor(pymysql.cursors.DictCursor)
        row = self.checkTitleFromDb(item['title'])
        if row:
            return
        else:
            sql = (
            "insert into pengfu_news(title, img_url)""values( %s, %s)")
            lis = (item['title'], item['img_url'])
            cursor.execute(sql, lis)
            con.commit()

            img_url = down_img.saveImgFile(item['img_url'][0])
            data = {
                'title': item['title'][0],
                'img_url': img_url
            }
            json_str = json.dumps(data)
            producer.emit(json_str)
            return item
