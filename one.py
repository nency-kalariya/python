#1
-------------------------------------
# a = 17.8
# print(type(a))
# print(int(a))

# b = 17
# print(type(b))
# print(int(b))

# no =9<36
# print(no)

# a = 'welcome to atmiya university'
# print(a[0])
# print(a[11:21])
# print(a[18:28])
# print(a[11:])
# print(a[-11:])
# print(a[-17:])
# print(a[-17])
# print(a[-17:18])
# print(a[:18])

# a ="""python is one of the very
#     intresting programing language"""

# print(a)

# a ='''python is one of the very
#     intresting programing language'''

# print(a)

# bytes
# a=[2,6,7,6,8,5,-9]
# print(a)

# a=[2,6,7,6,5]
# print(a)
# b=bytes(a)
# print(b)
# print(b[0])
# print(b[3])
# b[1]=25
# print(b)
# print(b[1])

# list
# a=[2,9,99,1000,12.5,-9,'atmiya','rajkot']
# print(a)
# print(a[3])
# print(a[4:7])
# print(a[-3])
# a[7]='gujarat'
# print(a)

# tuple
# a=(2,9,99,1000,12.5,-9,'atmiya','rajkot')
# print(a)
# print(a[3])
# print(a[4:7])
# print(a[-3])
# a[7]='gujarat'
# print(a)

# setdatatype
# a={2,3,5,8,9}
# print(a)
# a.update([20])
# print(a)
# a.remove(20)
# print(a)

# lst=[23,45,89,598,5,'a']
# print(lst)
# st=set(lst)
# print(st)

# frozen set
# a={2,33,3,5,8,9,2}
# print(a)
# fs=frozenset(a)
# print(fs)

# mapping
# key:values
# roll1:abc,roll2:cde
# a={}
# print(a)
# a[1]='abc'
# a[2]='cde'
# a[3]='fgh'
# print(a)
# print(a[2])
# print(a.keys())
# print(a.values())
# a[2]='xyz'
# print(a)
# del a[2]
# print(a)
# print(a['abc'])
# a[3]='aaa'
# print(a)

# literals
# a=25
# a=True
# a='atmiya'
# a=0b101
# a='python is easy'
# a='''python is very helpfull programming language. it is very \'trending' language.'''
# print(a)
# a='atmiya'
# print(type(a))

# arithmetic operator
# a=2+5
# b=5-2
# c=5*2
# d=10/2
# e=10%2
# f=13||2
# g=5**2

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

# assignment operator
# a=16
# b=2
# a+=b
# print(a)

# 10**2

# a**=b
# a>b
# a<b

# logical operator
# a=100
# b=200
# print(a and b)

# a=0
# b=45
# print(a and b)
# print(a or b)

# not b 
# not a

# a=0
# b=0
# print(a and b)
# print(a or b)

# bollean operator
# a=True
# b=True
# a and b

# b=False
# a and b
# print(a)
# print(b)
# a or b
# not b
# print(b)

# membership
# 'a' in 'MCA'
# 'A' in 'MCA'
# 'A' not in 'MCA'

# a=['mango','orange','apple']
# print(a)
# print('banana' in a)
# print('banana' not in a)

# is operator
# a=16
# b=6
# if(a is b):
#     print('a and b have same identity')
# else:
#     print('a and b not have same identity')

# is not operator
# a=16
# b=6
# if(a is not b):
#     print('a and b have same identity')
# else:
#     print('a and b not have same identity')

# a=['a','b','c','d']
# b=['a','b','c','e']
# if(a is b):
#     print('a and b have same identity')
# else:
#     print('a and b not have same identity')

# input and output statement
# output statement(print())
# print('this is the \n new line')
# print('the tab is \t used here')
# print('the city is' + 'rajkot')

# a,b=7,16
# print(a,b)
# print(a,b,sep='')
# print('Atmiya' end='')
# print('unversity')
# print('rajkot')

# a=7
# print(a,'the value of a is printed here')
# print('user has entered','a','as an input')

# to display single integer value
# a=7
# print('value = %i'%a)
# print('a = %i b=%i'%(a,b))

# string
# university = 'atmiya'
# print('hi %s'%university)
# print('hi %20s'%university)
# print('hi %-20s'%university)

# %c for single character
# university='atmiya'
# print('the first character is %c, and the second character is %c'%(university[0],university[1]))

# %f for the floating values
# a=123.45678
# print('the number is %f'%a)
# print('the number is %i'%a)
# name,salary='abc',16000
# print('hello {0}, your salary is {1}',format(name,salary))

# input statement
# taking input without message
# a=input()

# taking input with message
# a=input('enter the value :')

# taking restricted inputs
# only integer
# a=int(input('enter the value :'))
# a=float(input('enter the value :'))

# only the first character will be stored in the variable and printed
# character=input('enter the character :')[0]
# print(character)

# finding sum and product of two integers
# a=int(input('enter an integer value into a :'))
# b=int(input('enter an integer value into b :'))
# print('the sum of {0} and {1} is {2}'.format(a,b,a+b))
# print('the product of {0} and {1} is {2}'.format(a,b,a*b))

# use of split()
# n1,n2,n3=[int (no) for no in input('enter three numbers by giving space brtween them :').split()]
# print(n1)
# print(n2)
# print(n3)

# use of eval()
# a,b = 7,6
# ans = eval('a+b*3')
# print(ans)

# a,b = 7,6
# ans = eval('a+b**2')
# print(ans)

# command line arguments
# import sys
# a = int(sys.argv[0])
# b = int(sys.argv[1])
# sum = a+b
# print('the sum of a and b is',sum)

# control statement
# if statement
# syntax
# if condition
# statement

# #example
# a=1
# if a==1:
# 	print('the value of a is 1')

# a=int(input('enter the value of a :'))
# if a>7:
# 	print('the value of a is greater than 7')

# a='atmiya'
# if a=='atmiya':
# 	print('the value of a is atmiya')
# 	print('the value got matched')
# 	print('thank you')

# a=int(input('enter the value of a :'))
# b=int(input('enter the value of b :'))
# if a>b:
# 	print('the value of a is greater than value of b')

# a=int(input('enter the value of a :'))
# b=int(input('enter the value of b :'))
# if a==1:
#  	print('the value of a is 1')
#  	if b==2:
#  		print('the value of b is 2')
#  		print('end')

# quantity=int(input('enter the quantity to purchase :'))
# price=5
# if price*quantity<10000:
# 	print('the bill amount is less than rs. 10000, we cannot dispatch your order')

# a=int(input('enter the value :'))
# if a>7:
# 	print('the entered num is greater than 7')
# else:
# 	print('the entered num is less than 7')

#if...elif...else statement
#syntax:
#if condition1:
#	statement1
# elif condition2:
# 	statement2
# elif condition3:
# 	statement3
# else:
# 	statement4

#whether the entered number is positive, negative or zero
# a=int(input('enter the number :'))
# if a>0:
# 	print('the entered number is a positive number')
# elif a==0:
# 	print('the entered number is zero')
# else:
# 	print('the entered number is a negative number')

#that else part is not mandatory
# a=int(input('enter the number :'))
# if a==0:
# 	print('zero')
# elif a==1:
# 	print('one')
# elif a==2:
# 	print('two')
# elif a==3:
# 	print('three')
# elif a==4:
# 	print('four')
# elif a==5:
# 	print('five')

# amount=int(input('enter the number :'))
# if amount<=0:
# 	print('bill amount must be more than 0')
# elif amount<=5000:
# 	print('bill little more to avail discount')
# elif amount>5000 and amount<=8000:
# 	print('you got 10 percent discount')
# elif amount>8000 and amount<=10000:
# 	print('you got 12 percent discount')
# elif amount>=10000:
# 	print('highest discount of 25 percent')

# marks=int(input('enter the marks :'))
# if marks<=50:
# 	print('re-appear')
# elif marks>=50 and marks<60:
# 	print('pass')
# elif marks>=60 and marks<70:
# 	print('exam with first cls')
# elif marks>=70 and marks<80:
# 	print('exam with distinction')
# elif marks>=80 and marks<100:
# 	print('exam with honour')
# else:
# 	print('plz enter valid marks')

#if vs. elif
#(using if) accept marks of 4 students; display the students name who got the highest marks
# stud1=int(input('plz enter marks of student1 :'))
# stud2=int(input('plz enter marks of student2 :'))
# stud3=int(input('plz enter marks of student3 :'))
# stud4=int(input('plz enter marks of student4 :'))

# if stud1>stud2 and stud1>stud3 and stud1>stud4:
# 	print('stud1 is highest')
# if stud2>stud1 and stud2>stud3 and stud2>stud4:
# 	print('stud2 is highest')
# if stud3>stud2 and stud3>stud1 and stud3>stud4:
# 	print('stud3 is highest')
# if stud4>stud2 and stud4>stud3 and stud4>stud1:
# 	print('stud4 is highest')
# else:
# 	print('enter valid marks')

#nested if
# a=20
# b=40
# c=60
# d=80
# if(a>b):
# 	if(a>c):
# 		if(a>d):
# 			print('a is biggest')
# if(b>a):
# 	if(b>c):
# 		if(b>d):
# 			print('b is biggest')
# if(c>a):
# 	if(c>b):
# 		if(c>d):
# 			print('c is biggest')			
# if(d>a):
# 	if(d>b):
# 		if(d>c):
# 			print('d is biggest')

#while loop
#syntax
#while condition:
#	statements
#example
#to print number 1-10
# a=1
# while a<=10:
# 	print(a)
# 	a=a+1 #a+=1

# a=1
# while a<10:
# 	print(a)
# 	a=a+1 #a+=1

#take numbers from user, add them all and display, taking number from user gets terminated when user press 0.
# total=0
# number=int(input('enter a number:'))
# while number!=0:
# 	total=total+number  #total+=number
# 	number=int(input('enter a number:'))
# 	print('total=',total)

#print the table of 1
# num=1
# counter=1
# print('below is the table of',num)
# while counter<=10:
# 	ans=num*counter
# 	print(num,'x',counter,'=',ans)
# 	counter=counter+1

# num=int(input('enter the number for which table is to be printed:'))
# counter=1
# print('below is the table of',num)
# while counter<=10:
# 	ans=num*counter
# 	print(num,'x',counter,'=',ans)
# 	counter=counter+1

#printed even numbers between 1-10
# a=2  #a=1 for odd num,a=2 for even num
# while a>=1 and a<=10:
# 	print(a)
# 	a=a+2

#even or odd based on user choice (1 for odd,2 for even)
# print('enter 1 or 2, on the basic of your choice 1 for odd,2 for even:')
# num=int(input())
# if num == 1:
# 	while num>=1 and num<=10:
# 		print(num)
# 		num=num+2
# elif num == 2:
# 	while num>=1 and num<=10:
# 		print(num)
# 		num=num+2
# else:
# 	print('enter the valid choice')

#to print number and their square 
# number=1
# while number<=10:
# 	print(number,'\t',number**2)
# 	number=number+1

#display only even numbers from the set
# a=[2,4,5,6,8,6,7,9]
# b=0
# while(b<len(a)):
# 	if a[b]%2==0:
# 		print(a[b])
# 	b=b+1

#printing each character of string individually
# a='atmiya'
# b=0
# while(b<len(a)):
# 	print(a[b])
# 	b=b+1

# the for loop
# syntax:
# for var in sequance:
# 	statement
#printing each character of string individually
# a='atmiya'
# for c in a:
# 	print(c)	

#display elements of the string using index
# a='atmiya'
# c=len(a)
# for i in range(c):
# 	print(a[i])

#using range()
# for i in range(10):
# 	print(i)

#print odd numbers between 1-10
# for i in range(1,11,2):  #range(from,to,jump)
# 	print(i)
# for i in range(1,11,-2):  #range(from,to,jump)
# 	print(i)
#print even numbers between 1-10
#for i in range(2,11,2):  #range(from,to,jump)
#	print(i)

#printing each elements from the list individually
# a=[1,2.5,'a','rajkot','india']
# for i in a:
# 	print(i)

#add all the elements of the list
# a=[2,3,5,8,6,4,86,57,1]
# sum=0
# for i in a:
# 	print(i)
# 	sum=sum+i
# print('the sum of the elements of list is:',sum)

# a=[2,3,5,8,6,4,86,57,1]
# sum=0
# for i in a:
# 	print(i)
# 	sum=sum+i
# print('the sum of',a,'is :',sum)

#using else with for
# a=[1,2.5,'a','rajkot','india']
# for i in a:
# 	print(i)
# else:
# 	print('all the elements are printed')

#without else with for
# a=[1,2.5,'a','rajkot','india']
# for i in a:
# 	print(i)
# else:
# 	print('all the elements are printed')

#finding square of each element of the list
# num=[2,4,6,8,9]
# sqr=0
# n=len(num)
# for i in range(n):
# 	print(num[i])
# 	sqr=num[i]**2
# 	print(sqr)

#nested loops
#structure:
#outer loop:
#	inner loop:
#the 'inner loop' will be executed one time for each iteration of the 'outer loop'
#outer loop is in-change of rows; inner loop is in-change of columns
# for i in range(3):
#  	for j in range(4):
#  		print(j,end='') #print(i,end='')
#  		print()

#break statement
#print 10-1
# a=10
# while a>=1:
# 	print(a)
# 	a=a-1
# 	if a==5:
# 		break

#taking input to check whether the inserted number is available in the list
# a=[7,8,9,10,11]
# searh=int(input('enter the element to search :'))
# for e in a:
#  	if searh==e:
#  		print('enter element is found')
#  		break
# else:
# 	print('the entered element is not found')

#using break with string
# a='atmiya'
# for b in a:
# 	print(b)
# 	if b=='a':
# 		break

#the continue statement
# a='atmiyauniversityrajkot'
# for i in a:
# 	if i=='a':
# 		continue
# 	print(i,end=' ')

#print 1-10, except 5 and 6
# for i in range(1,11):
# 	if i==5 or i==6:
# 		continue
# 	else:
# 		print(i,end=' ')

#the pass statement
# a=0
# while a<10:
# 	a=a+1
# 	if a>5:
# 		pass
# 	print(a)

#to display only negative numbers from the list
# a=[1,2,-9,4,-5,6]
# for i in a:
# 	if(i>0):
# 		pass
# 	else:
# 		print(i)