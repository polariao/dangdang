# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import urllib.request
import random
class DdPipeline(object):
    def process_item(self, item, spider):
        mysql = pymysql.connect('localhost', 'root', '100521', 'python')
        for i in range(0,len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            comment = item['comment'][i]
            url = item['image'][i]
            imgurl = 'E:/PyCharm 2018.2.4/pycode/touch/dd/image/'+str(i)+str(random.randint(0,99999))+'.jpg'
            urllib.request.urlretrieve(url=url,filename=imgurl)
            sql = "insert into dangdang (title,url,comment,imageurl) values ('"+str(title)+"','"+str(link)+"','"+str(comment)+"','"+str(imgurl)+"');"
            res = mysql.query(sql)
            if res:
                print('写入成功')
        mysql.close()
        return item
