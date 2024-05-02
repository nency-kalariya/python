#function,file heandling, regular expression
#function
#structure:
	# def name_of_function(parameter1,parameter2,....)
	# 	function statements

#to add two numbers using funcion
# def summation(a,b):
# 	sum=a+b
# 	print('the sum of two digit is:',sum)
# #calling the function
# summation(3,6)
# summation(3.6,6.3)

#returning results from the function
#to add two numbers using function
# def summation(a,b):
# 	sum=a+b
# 	return sum
# #calling the function
# a=summation(3,6)
# print('the addition of two digits is:',a)
# b=summation(3.6,6.3)
# print('the addition of two digits is:',b)

#to check whether entered number is odd or even using function
# def odd_or_even(number):
# 	if number%2==0:
# 		print('the number is even')
# 	else:
# 		print('the number is odd')
# #calling the function
# odd_or_even(2)	
# odd_or_even(3)

#to check whether entered number is odd or even using function
#number=int(input('enter the number to check:'))
# def odd_or_even(number):
# 	if number%2==0:
# 		print('the number is even')
# 	else:
# 		print('the number is odd')
# #calling the function
# number=int(input('enter the number to check:'))
# odd_or_even(number)	

#to check whether entered number is positive,negative or zero using function
# def pos_neg_zer(number):
# 	if number<0:
# 		print('the entered number is negative')
# 	elif number==0:
# 		print('the entered number is zero')
# 	else:
# 		print('the entered number is positive')
# #calling the function
# number=int(input('enter the number to check:'))
# pos_neg_zer(number)

#returning multiple values from a function 
#to perform basic arithmatic operations
# def arithmatic(a,b):
# 	add=a+b
# 	sub=a-b
# 	mul=a*b
# 	div=a/b
# 	return add,sub,mul,div
# #calling the function
# a,s,m,d=arithmatic(10,2)
# print('the addition of two numbers is:',a)
# print('the substraction of two numbers is:',s)
# print('the multipliction of two numbers is:',m)
# print('the division of two numbers is:',d)

#pass by object
#immutable objects:integer,float,string,tuple
#mutable objects:list

#program to pass an integer to a function and modify it.
#working with immutable objects
# def modify(a):
# 	a=7
# 	print('the value of a, in the body of function is',a,id(a))
# #calling the function
# a=9
# modify(a)
# print('the value of a, in the body of function is',a,id(a))

#working with mutable objects
# def modify(lst):
# 	lst.append(7)
# 	print(lst,id(lst))
# #calling the function
# lst=[1,2,3,4,5]
# modify(lst)
# print(lst,id(lst))

#formal and actual arguments
#def arithmatic(a,b) --->this is known as parameters
#calling the function
#a,s,m,d=arithmatic(10,2) --->this is known as arguments

#list of actual arguments(4 types):
#1. positional arguments
#2. keyword arguments
#3. default arguments
#4. variable arguments

#1). positional arguments
#-no. of parameter and their position must match with when calling the function
# def conc(s1,s2):
# 	combined=s1+s2
# 	print(combined)
# #calling the function
# conc('atmiya','university')
# conc('university','atmiya')

#2). keyword arguments
#arguments are idenified by their names
# def  stud_det(enr,name):
# 	print('the enrollment of student is:',enr)
# 	print('the name of student is:',name)
# #calling the function
# stud_det(enr=111,name='abc')
# stud_det(name='abc',enr=111)

#3). default arguments
#we can give default value to the parameter
# def stud_det(enr,name='abc'):
# 	print('the enrollment of student is:',enr)
# 	print('the name of student is:',name)
# #calling the function
# stud_det(enr=111,name='abc')
# stud_det(enr=111)

#4). variable length arguments
#used when number of parameters cannot be defined in advance
#format:def name_of_fun(farg,*args)
# def add(farg,*args):
# 	print('formal argument is',farg)
# 	sum=0
# 	for i in args:
# 		sum=sum+i
# 		print('the sum of all numbers:',(farg+sum))
# #calling the function
# add(2,3)
# add(2,3,4)
# add(2)

#passing group of elements in a function
# def display(lst):
# 	for i in lst:
# 		print(i)
# #calling the function
# print('enter elements separated by space:',end='')
# lst=[a for a in input().split()]
# #calling the function
# display(lst)

#anonymous function (also know as lambda)
#normal function
#def square(a):
#	return a*a
# square=lambda a:a*a
# a=int(input('enter the number to know its square:'))
# print('the square of the entered number is:',square(a))

#generators
#generators are function that return a sequance of values.
#generator function are written same as ordinary function.
#it used 'yield' statement.
#the yield statement is usefult to return the value.

#example:create a generator that returns a sequance of numbers from a to b.
# def generator1(a,b):
# 	while a<=b:
# 		yield a
# 		a=a+1
# #filling the generator object
# gen=generator1(1,10)
# #displaying the values
# for i in gen:
# 	print(i,end='')
# #print(next(gen))
# gen=generator1(1,10)

#file handling
#1. text file
#2. binary file

#open():
#will be used to open a file.
#this function accepts 'filename' and 'openmod' to open the file.
#example
#file handler=open('filename','openmod')

#close():
#once the file is opened it must be closed.
#otherwise the data in the file may get corrupted or lose of data may happen.
#until the file is opened again without closing it will not free the memory.
#we can close the file using close().

#to create a text file and store some data into it.
# f=open('myfile.txt')
# #open a file
# f=open('myfile.txt','w')
# #writing data into the file by accepting it from the user
# str1=input('enter the text you want to write into the file:')
# f.write(str1)
# #closing the file
# f.close()

# #reading the existing file
# f=open('myfile.txt','r')
# str1=f.read()
# #display the data on the screen
# print(str1)
# f.close()

# #append into an existing file
# f=open('myfile.txt','a+')
# print('enter the text you want to append:')
# while str1!='$':
# 	str1=input() #accepting the text from the user
# 	if(str1!='$'):
# 		f.write(str1)
# 		break
# f.close()
# f=open('myfile.txt','r')
# str=f.read()
# print(str)
# f.close()

# #knowing whether a file exists or not
# #the operating system (os) module has a sub module name 'path'
# #which has a method isfile()
# #it is used to check whether the file really exist or not.

# #to check whether to the file is available or not, if available open the file
# import os
# #to enter the file name
# fname=input('enter the file name to open:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# #reading the file
# 	str1=f.read()
# #display on the screen
# 	print(str1)
# else:
# 	print(fname+'does not exist')
# f.close()

# #counting number of lines,words and characters if the files is available.
# import os
# #taking the file name
# fname=input('enter the file name to open:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# else:
# 	print(fname+'does not exist')
# #initialising counters and setting it to zero
# cl=cw=cc=0
# #reading lines from the file
# for line in f:
# 	words=line.split()
# 	cl=cl+1
# 	cw=cw+len(words)
# 	cc=cc+len(line)
# print('number of lines in a file is:',cl)
# print('number of words in a file is:',cw)
# print('number of character in a file is:',cc)
# f.close()

#working with binary files
#it stores data in the form of bytes.
#the mode to read the file is 'rb'
#the mode to write the file is 'wb'
#the read() will be used to read the data.
#the write() will be used to write the data.

#to copy an image from one file to another
#to open the file in binary mode
# f=open('d:\\download.png','rb')
# f1=open('d:\\atmiya_logo.png','wb')
# #read bytes from f and write it to f1
# img = f.read()
# f1.write(img)
# #closing the file
# f.close()
# f1.close()

#the 'with' statement
#it can be used while opening the file.
#the benefit of using 'with' is that, it takes care of closing the file which is opened.
#formate
#	with open('file_name','open_mode') as file object:
#taking data from the user and store in the form of binary file
# record_length=10 #record_length is a variable, in which we hase stored 10
# #opening the file in 'wb' mode
# with open('stationery_store','wb') as f:
# 	n=int(input('how many items you want to add?:'))
# 	for i in range(n):
# 		stat_item=input('entert the name of stationery:')
# 		length=len(stat_item) #to find the length of a stationery method
# 		stat_item=stat_item+(record_length-length)*''
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# #reading the file
# with open('stationery_store','rb') as f:
# 	str1=f.read()
# 	print(str1.decode())
# 	print(type(str1))
# 	print(str1)

#zipping the content of files
# from zipfile import *
# #creating the file
# f=ZipFile('demo.zip','w',ZIP_DEFLATED) #to zip the file after compressing
# #ZIP_STORED:to just zip the file
# #adding files to be zipped
# f.write('d:\\download.png')
# f.write('d:\\atmiya_logo.png')
# #closing the zip file
# f.close()

# #unzipping the file
# from zipfile import *
# z=ZipFile('demo.zip','r')
# z.extractall('d:')

# with open('stationery_store','wb') as f:
# 	n=int(input('how many items you want to add?:'))
# 	for i in range(n):
# 		stat_item=input('entert the name of stationery:')
# 		length=len(stat_item) #to find the length of a stationery method
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# 		f.write("\n".encode())

#random accessing the binary files (using mmap)
#the full form of mmap is 'memory maped file'
#format
#	mm=mmap.mmap(f.fileno(),0)
#where f represents file object
#	fileno() is a file descriptor (or handle) used to access file or i/o
#	0 represents the whole file to be readed

#to create a register in which name of students and their enr.no is stored
# with open('student_register.dat','wb') as f:
# 	n=int(input('enter the number of records to be inserted:'))
# 	for i in range(n):
# 		name=input('enter the name of student:')
# 		enr=input('enter the enrollment number of student:')
# 		name=name.encode()
# 		enr=enr.encode()
# 		f.write(name+enr)

#performing various operation on the file named student_register.dat 
# import mmap,sys
# print('1. to view details of all the students:')
# print('2. to view enrollment number of the student by passing his/her name:')
# print('3. to modify the enrollment number of students:')
# print('4. to exit:')
# choice=int(input('enter your choice:'))
# if choice==4:
# 	sys.exit()
# with open('student_register.dat','r+b') as f:
# 	mm=mmap.mmap(f.fileno(),0)
# 	if(choice==1):
# 		print(mm.read().decode())
# 	if(choice==2):
# 		name=input('enter the name of student, for which you want to know the enrollment number:')
# 		n=mm.find(name.encode()) #returns the position of the name in the file
# 		n1=n+len(name) #it will go to the end of the name
# 		en=mm[n1:n1+3] #it will display the next 3 bytes
# 		print('the enrollment of said student is:',en.decode())
# 	if(choice==3):
# 		name=input('enter the name of student, for which you want to modify the enrollment number:')
# 		n=mm.find(name.encode())
# 		n1=n+len(name) #it will go to the end of the name
# 		en1=input('enter the modified enrollment number:')
# 		mm[n1:n1+3]=en1.encode() #the old enrollment number will be modified/updated
# mm.close()

#regular expression (also known as regex or re)
#str=r'm\w\w'
# str1='this will be printed on the \nnewline'
# print(str1)
# str1=r'this will be printed on the \nnewline'
# print(str1)

#using compile() of 're' module to complile the regular expression.
# import re
# prog=re.compile(r'm\w\w')
# str1='net cat mat matter' #regular expression will act on this string
# result=prog.search(str1) #use of search(), to search the expression in the string
# print(result.group()) #use of group(), to display the result

# str2='later or sooner truth of man matters' #regular expression will act on this string
# result=prog.search(str2) #use of search(), to search the expression in the string
# print(result.group()) #use of group(), to display the result

#create a regular expression to search for string starting with 'm' a having total 3 characters using findall().
# import re
# str1='net cat mat matter'
# result=re.findall(r'm\w\w',str1)
# print(result)

#use of split()
#the split() splits the given string into pieces according to the regular expression and returns the pieces as elements of a list.
#re.split(r'\W+',str1)
#here, the 'capital W' represents any non-alphanumeric.
# import re
# str1='Hello! All, Good; Morning'
# result=re.split(r'\W+',str1)
# print(result)

#create a regular expression that replaces a string with the new string
# import re
# str1='AITS is the best Organization'
# print(str1)
# result=re.sub(r'AITS','Atmiya University',str1) #use of sub()
# print(result)

#create a regular expression that finds the words starting with 's'.
# import re
# str1='sun shines sooner or later'
# result=re.findall(r's[\w]*',str1)
# print(result)

#create a regular expression that finds the words starting with 'S'.
# import re
# str1='Sun shines sooner or later'
# result=re.findall(r'S[\w]*',str1)
# print(result)

#create a regular expression that finds the words starting with a number.
# import re
# str1='the special classes are arranged on 11th and 21st of every month'
# result=re.findall(r'\d[\w]*',str1) #id
# print(result)

#create a regular expression that retrieve the words having 5 characters.
# import re
# str1='sun mon tues wedn thurs frida saturday'
# result=re.findall(r'\b\w{5}\b',str1)
# print(result)

#create a regular expression that retrieve the words having 4 or 5 characters.
# import re
# str1='sun mon tues wedn thurs frida saturday'
# result=re.findall(r'\b\w{4,5}\b',str1)
# print(result)

#create a regular expression that retrieve the words having 2,4 or 6 characters.
# import re
# str1='sun mon tues wedn thurs friday saturday'
# result=re.findall(r'\b\w{2,6}\b',str1)
# print(result)

#create a regular expression that retrieve only single digit number from the string.
# import re
# str1='seven eight 9 10'
# result=re.findall(r'\b\d\b',str1)
# print(result)

#create a regular expression which retrieve last word of the string if it starts with 's'.
# import re
# str1='seven eight nine seventeen'
# result=re.findall(r's[\w]*\Z',str1)
# print(result)

# import re
# str1='seven eight nine seventeen'
# result=re.findall(r'\As[\w]*',str1)
# print(result)

#create a regular expression that retrieve the enrollment number of students.
# import re
# str1='abc 1234'
# result=re.findall(r'\d+',str1)
# print(result)

#create a regular expression that retrieve the name of students.
# import re
# str1='abc 1234'
# result=re.findall(r'\D+',str1)
# print(result)

#create a regular expression that retrieve the word starting with 'st'.
# import re
# str1='summer sun strong stanning storm small smell'
# result=re.findall(r's[t][\w]*',str1)
# print(result)

#create a regular expression that retrieve the word starting with 'st' and 'sm'.
# import re
# str1='summer sun strong stanning storm small smell'
# result=re.findall(r's[t,m][\w]*',str1)
# print(result)

#create a regular expression to retrieve only the birthdate of candidate.
# import re
# str1='001 abc 1-10-1999, 002 cde 21-10-1980, 003 efg 12-11-1980'
# # result=re.findall(r'\d{2}-\d{2}-\d{4}',str1)
# result=re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str1)
# print(result)

#create a regular expression to search whether the string starting with 'at' or not.
# import re
# str1='atmiya university'
# result=re.search(r'^at',str1)
# if result:
# 	print('the str1 starts with at')
# else:
# 	print('the str1 does not starts with at')

#create a regular expression to search whether the string end with 'ty' or not.
# import re
# str1='atmiya university'
# result=re.search(r'ty$',str1)
# if result:
# 	print('the str1 end with ty')
# else:
# 	print('the str1 does not end with ty')

#create a regular expression to retrieve the price of the products.
# import re
# str1='the pen is of r.10 pencil of r.2 and the eraser is of r.5'
# # result=re.findall(r'\d{1,3}',str1)
# result=re.findall(r'[1-10]',str1)
# print(result)

# import re
# str1='Atmiya'
# result=re.search('[A-Z][a-z*]',str1)
# if result:
# 	print('in the string the first character is capital and rest others are small characters')
# else:
# 	print('first latter is capital')

#create a regular expression that extracts the time.
# import re
# str1='the result may be declared at 1pm today or at 8pm tommorow'
# result = re.findall(r'\b\d{1,2}[ap]m\b', str1)
# print(result)