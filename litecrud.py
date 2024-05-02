# import sqlite3
# exe=sqlite3.connect('employee.db')

# #create table
# exe.execute('CREATE TABLE STUDENTS (ID INTEGER(20) PRIMARY KEY , NAME VARCHAR(200), STREAM VARCHAR(200))')


#insert table
# exe.execute("""INSERT INTO STUDENTS VALUES (1,'rahul','mca'),
#                                             (2,'vidhey','mba'),
#                                             (3,'yuvraj','mtech'),
#                                                 (4,'vatsal','msc')""")
# print('Data inserted successfully ')
# exe.commit()

# #display table
# result=exe.execute('SELECT * FROM STUDENTS')
# for i in result:
#     print(i)

#update table
# exe.execute("UPDATE STUDENTS SET NAME='AJAY', STREAM='MECHANICAL' WHERE ID=1")

# result = exe.execute('select * from students')
# for i in result:
#     print(i)

# #delete table
# exe.execute('DELETE FROM STUDENTS WHERE ID=1')
# result=exe.execute('select * from students')
# for i in result:
#     print(i)