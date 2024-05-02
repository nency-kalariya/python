#database connectivity of python with mysql //pip install mysql.connector //pandas //matplotlib.pyplot //numpy  //xlrd //openpyxl
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# print(mydb)
#creating the database
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')
#showing the list of databases (checking whether the database 'mypy' is created or not)
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
# 	print(i)
#creating the 'stud_data' table
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE stud_dat(roll int, name varchar(25))')
#inserting the records in the table
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# insert_query='INSERT INTO stud_dat (roll,name) VALUES (%s,%s)'
# records_insert=[(1,'sunday'),(2,'monday'),(3,'saturday')]
# cursor=mydb.cursor()
# cursor.executemany(insert_query,records_insert)
# mydb.commit()
# print('record inserted succesfully')
# mydb.close()
#display the records inserted in the table
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud_dat')
# result=mycursor.fetchall()
# # for i in result:
# # 	print(i)
# print(result)
#updating the record
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# update_query="UPDATE stud_dat SET roll=5 WHERE name='monday'"
# mycursor.execute(update_query)
# mydb.commit()
#deleting the record
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# delete_query="DELETE FROM stud_dat WHERE roll=5"
# mycursor.execute(delete_query)
# mydb.commit()
# *********************************
#create database
# import sqlite3
# cnt=sqlite3.connect('mydb.dp')
#creating the table stud_data
# cnt.execute('create table stud_data(roll integer,name varchar)')
# print('table created')
#inserting the records
# cnt.execute("""
# 	insert into stud_data values
# 	(1,'january'),
# 	(2,'february'),
# 	(3,'march')
# 	""")
# print('record inserted successfully')
# cnt.commit()
# retriving the data
# cursor=cnt.execute('select * from stud_data')
# for i in cursor:
# 	print(i)
# retriving the record whose roll no greter than 2
# cursor=cnt.execute('select * from stud_data where roll>2')
# for i in cursor:
# 	print(i)
#update the name whose roll no is 3
# sql_upd="""update stud_data set name='april' where roll=3"""
# cnt.execute(sql_upd)
# cursor=cnt.execute('select * from stud_data')
# for i in cursor:
# 	print(i)
#deleting the record whose roll is 3
# sql_del="""delete from stud_data where roll=3"""
# cnt.execute(sql_del)
# cursor=cnt.execute('select * from stud_data')
# for i in cursor:
# 	print(i)