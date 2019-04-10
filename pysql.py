# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:26:51 2019

@author: user
"""
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","n124589304","my_db",charset="utf8" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

# 使用 execute()  方法执行 SQL 查询 
#cursor.execute("SELECT VERSION()")
sql="SELECT * FROM products"
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
      id = row[0]
      name = row[1]
      descr = row[2]
      price = row[3]
      print ("id=%s,name=%s,descr=%s,price=%s" % \
             (id,name,descr,price ))
except:
   print ("Error: unable to fetch data")
# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()
 
#print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()