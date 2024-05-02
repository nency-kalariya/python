# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# print(mydb)

#create database
#exec=mydb.cursor()
#exec.execute('CREATE DATABASE game')



import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='game')

#create table
exe=mydb.cursor()
# exe.execute("create table employee (id integer(12) primary key auto_increment , name varchar(211), salary integer(34))")


#insert records
# query=(""" insert into employee (name,salary)
#                                 values(%s,%s)
#                                        """)
# record=[('rahul',48488),('ram',55488)]
# exe.executemany(query,record)
# mydb.commit()
# print('data inserted')

#display records
# exe.execute('select * from employee')
# result =exe.fetchall()
# for i in result:
#     print(i)

# #update the record
# exe.execute("update employee set name='sita',salary=89899 where id=6")
# mydb.commit()
# print('data updated successfully')


# #delete the record
# exe.execute('delete from employee where id=7')





