# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class TutorialPipeline:
    def __init__(self):
        # connection database
        self.connect = pymysql.connect(host='127.0.0.1', user='3306', passwd='123456',
                                       db='spider')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")
        # 清空数据库
        deletes = """truncate table news"""
        self.cursor.execute(deletes)
        self.connect.commit()
        print("清空原有数据")

    def open_spider(self, spider):
        print("爬虫开始...")

    #     self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider')
    #     print(self.conn)

    def process_item(self, item, spider):
        # sql语句
        insert_sql = """insert into news(title, imgUrl, newTime,url) VALUES (%s,%s,%s,%s)"""
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['title'], item['imgUrl'], item['newTime'], item['url']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        print("mysql数据插入成功", item['title'], item['imgUrl'], item['newTime'], item['newTime'])

        # self.cursor = self.conn.cursor()
        # sql = 'insert into news values("%s","%s","%s")' % ("item['title']", "item['imgUrl']"," item['newTime']")
        # try:
        #     self.cursor.execute(sql)
        #     self.conn.commit()
        # except Exception as e:
        #     print(e)
        #     self.conn.rollback()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()
        print("爬虫结束")
