# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb

class RecruitPipeline(object):
    def open_spider(self, spider):
        conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='200022',
        db ='news',
        charset='utf8'
        )
        self.conn=conn
        self.cursor = conn.cursor()

    def process_item(self, item, spider):
        sql="insert into news_news(news_title,text,writer_id,style,date) value (%s,%s,1,%s,now())"
        self.cursor.execute(sql,(item['title'],item['text'],item['type']))
        self.conn.commit()
        print("charuchenggong")
        return item

    def close_spider(self, spider):
        self.conn.close()


