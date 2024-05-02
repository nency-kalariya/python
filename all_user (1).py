#1-------------------
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

# if statement
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
# 	total=total+number 
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
# a=2 
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
# for i in range(1,11,2):  
# 	print(i)
# for i in range(1,11,-2): 
# 	print(i)
#print even numbers between 1-10
#for i in range(2,11,2): 
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

#2-------------------------
#1st way to create array
# import array
# a=array.array('i',[1,23,45,67]) 
# print(a)

#2nd way to create array
# import array as ar 
# a=ar.array('i',[1,23,45,67])
# print(a)

#3rd way to create array
# from array import *
# a=array('i',[1,23,45,67])
# print(a)

#using array to store characters and display all characters
# from array import *
# c=array('u',['a','b','c','d'])
# for ch in c:
# 	print(ch,end='') #print(ch,end=',')
	
#copying array type code and array elements
# from array import *
# c=array('u',['a','b','c','d']) 
# d=array(c.typecode,(c for c in c))
# for ch in d:
# 	print(ch)

#indexing and slicing on arrays
# from array import *
# a=array('i',[10,20,30,40,50])
# n=len(a)
# print(n)
# for i in range(n):
# 	print(a[i],end=' ')

#using while loop
# from array import *
# a=array('i',[10,20,30,40,50])
# n=len(a)
# print(n)
# i=0
# while i<n:
# 	print(a[i],end=' ')
# 	i=i+1

#slicing
# from array import *
# c=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t','i','n','d','i','a'])
# a=c[0:18]
# print(a)
# a=c[0:]
# print(a)
# a=c[:]
# print(a)
# a=c[2:5]
# print(a)
# a=c[-18:]
# print(a)
# a=c[0:0]
# print(a)
# a=c[-18:-5]
# print(a)

# from array import *
# c=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t','i','n','d','i','a'])
# for i in c[0:17]:
# 	print(i,end='')

# processing the arrays
# from array import *
# ar=array('i',[1,2,3,4,5])
# print('the initial value of an array is :',ar)

# appending the value to the array
# ar.append(6)
# ar.append(7)
# print('the value after append is :',ar)

# inserting the value at the desired position
# ar.insert(0,0)
# print('the value after insert is :',ar)
# ar.insert(4,3)
# print('the value after insert is :',ar)

# removing an element from the array
# ar.remove(5)
# print('the value of after removing an element is :',ar)

# removing the last element of the array
# ar.pop()
# print('the value after using the pop method is :',ar)

# finding the position of an element
# b=ar.index(3)
# print('the desired element is at the position :',b)

# converting an array into list
# lst=ar.tolist()
# print('value of the list is :',lst)

#taking marks of students, finding total of marks and percentage using array
# from array import *
# s=input('enter marks :').split(' ')
# marks=[int(num) for num in s]
# total=0
# for i in marks:
# 	print(i)
# 	total=total+i
# print('the total of marks is :',total)
# l=len(marks)
# percent=total/l
# print('the percentage is :',percent)

#searching an element from the array
# from array import *
# a=array('i',[])
# print('how many elements you want to enter?: ',end='')
# n=int(input())
# for i in range(n):
# 	print('enter an element: ',end='')
# 	a.append(int(input()))
# print('elements of the array are: ',a)
# print('enter the element to search: ',end='')
# search=int(input())
# try:
# 	position=a.index(search)
# 	print('an element is found at the position',position)
# except:
# 	print('the entered element is not found in the array')

#arrays
# from array import *
# a=array('i',[10,20,30,40,50])
# print(a)

# import numpy
# a=numpy.array([10,20,30,40,50])
# print(a)

# import numpy as nu
# a=nu.array([10,20,30,40,50])
# print(a)

# from numpy import *
# a=array([10,20,30,40,50])
# print(a)

#creating array using linspace
# from numpy import *
# a=linspace(2,10,5)
# print(a)
# a=linspace(2,10,9)
# print(a)

#creating array using arange()
# from numpy import *
# a=arange(1,10)
# print(a)

#operations on array
# from numpy import *
# a=array([1,2,3,4,-5])
# print(a)
# print('after adding 5 to each element of the array : ',a+5)
# print('after subtracting 5 to each element of the array : ',a-5)
# print('after multiplying 5 to each element of the array : ',a*5)
# print('after dividing 5 to each element of the array : ',a/5)
# print('the sum of elements: ',sum(a))
# print('the max elements: ',max(a))
# print('the min elements: ',min(a))
# print('the average: ',mean(a))

#comparing arrays
# from numpy import *
# a=array([1,2,3,4,5])
# print(a)
# b=array([5,4,3,2,1])
# print(b)
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a<b)

#compare individual elements to its corresponding element of other array and retrive the bigger one
# from numpy import *
# a=array([1,2,3,4,5,6])
# b=array([2,1,5,3,6,7])
# c=where(a>b,a,b)  
# print(c)

#retrive the non-zero elements from the array
# from numpy import *
# a=array([1,0,3,0,5,6])
# b=nonzero(a)
# print(a)
# print(a[b])

#to create a view of the existing array 
# from numpy import *
# a=array([1,0,3,0,5,6])
# b=a.view()
# print('elements of array a are: ',a)
# print('elements of array b are: ',b)
# b[3]=400
# print('elements of array b are: ',b)
# print('elements of array a are: ',a)

#to create a copy of the array
# from numpy import *
# a=array([1,0,3,0,5,6])
# b=a.copy()
# print('elements of array a are: ',a)
# print('elements of array b are: ',b)
# b[3]=500
# a[2]=200
# print('elements of array b are: ',b)
# print('elements of array a are: ',a)

#slicing
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a[0:6:2])
# print(a[:])
# print(a[::])
# print(a[2:])
# print(a[2::2])

#indexing
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# i=0
# while(i<len(a-1)):
# 	print(a[i])
# 	i=i+1

#attributes of an array
#1) ndim :
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a.ndim)
# b=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(b)
# print(b.ndim)
# c=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(c)
# print(c.ndim)

#2) shape :
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a.shape)
# b=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(b)
# print(b.shape)
# c=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(c)
# print(c.shape)

#3) size : 
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a.size)
# b=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(b)
# print(b.size)
# c=array([[10,20,30,40,50,60,70],[10,20,30,40,50,60,70],[10,20,30,40,50,60,70]])
# print(c)
# print(c.size)

#4) dtype : 
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a.dtype)

#5) reshape() : 
# from numpy import *
# a=array([1,2,3,4,5,6,7,8])
# print(a)
# a=a.reshape(2,4)
# print(a)

#6) flatten() : 
# from numpy import *
# a=array([1,2,3,4,5,6,7,8])
# print(a)
# a=a.reshape(2,4)
# print(a)
# a=a.flatten()
# print(a)

#multi-dimensional arrays
# from numpy import *
# a=array([[10,11,12,13],[14,15,16,17]])
# print(a)

#the reshape()
# from numpy import *
# a=array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# b=reshape(a,(4,3))
# print(b)
# c=reshape(a,(2,3,2))
# print(c)

#indexing in multi-dimensional arrays
# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# for i in range(len(a)):
# 	for j in range(len(a[i])):
# 		print(a[i][j],end='')

#slicing in multi-dimensional arrays
# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a[0,:]) 
# print(a[2,:]) 
# print(a[:,0]) 
# print(a[0:1,0:1]) 
# print(a[2:3,1:2])

#working with strings
# s1='welcome to atmiya university, rajkot'
# print(s1)
# s2="welcome to atmiya university, rajkot"
# print(s2)
# s3="welcome to 'atmiya university', rajkot"
# print(s3)
# s4="welcome to \t'atmiya university',\n rajkot"
# print(s4)
# s5=r"welcome to \t'atmiya university',\n rajkot"
# print(s5)
# print(len(s5))
# s6="atmiya"
# s7="university"
# s=s6+s7
# print(s)

#access each element of a string in forward order
# st='atmiya university'
# i=0
# for i in st:
# 	print(i,end='')
# print()

#access each element of a string in backward order
# st='atmiya university'
# for i in st[::-1]:
# 	print(i,end='')

#slicing the string
# st='atmiya university'
# print(st[0:17])
# print(st[0:17:1]) 
# print(st[0:17:2]) 
# print(st[-1::-1]) 
# print(st[-1::]) 

#checking whether string exist in the main string
# st=input('enter the main string:')
# sub=input('enter the string you wanted to find:')
# if sub in st:
# 	print(sub,'is available in the main string')
# else:
# 	print(sub,'is not available in the main string')

#checking whether entered string is palindrome
# st=input('enter the string:')
# st1=(st[-1::-1])
# if(st==st1):
# 	print('the string is a palindrome')
# else:
# 	print('the string is not a palindrome')

#counting sub string in a string
# st='better india for better world'
# n=st.count('better',0,30)
# print(n)
# n=st.count('india')
# print(n)

#changing case of a string
# st='your future is bright'
# print(st.upper())
# print(st.lower())
# print(st.swapcase())
# print(st.title())

#use of isdigit()
# mobile_number=input('enter your mobile number:')
# print(mobile_number.isdigit())
# if mobile_number.isdigit()!=True:
# 	print('enter valid mobile number')
# else:
# 	print('you have entered valid mobile number')

#sort a string into alphabetical order
# st=[]
# n=int(input('how many strings you want to enter?:'))
# for i in range(n):
# 	print('enter the string:',end='')
# 	st.append(input()) 
# 	print(st) 
# 	st1=st.sort() 
# 	for i in st:
#  		print(i)

#working with characters
# st='atmiya'
# ch=st[0]
# print(ch)
# ch=st[4]
# print(ch)
# ch=st[0:3]
# print(ch)
# ch=st[0:8]
# print(ch)

#program to know the type of a characters
# st=input('enter a character:')
# ch=st[0]
# if ch.isalpha():
# 	print('yes,it is an alphabet')
# 	if ch.isupper():
# 		print('character is in upper case')
# 	else:
# 		print('character is in lower case')
# else:
# 	print('oops,you have entered something else')

#list
#0 to 7
# lst=range(8) #lst=range(0,8,1)
# for i in lst:
# 	print(i,end='')

#8 to 15
# lst=range(8,16) 
# for i in lst:
# 	print(i,end='')

#odd numbers between 1-10
# lst=range(1,11,2) 
# for i in lst:
# 	print(i,end='')

#even numbers between 1-10
# lst=range(2,11,2) 
# for i in lst:
#	print(i,end='')

#updating the list
# lst=list(range(1,8))
# print(lst)
# lst.append(9)
# print(lst)
# lst[5]=60
# print(lst)
# del lst[5] 
# print(lst)
# lst.remove(5)
# print(lst)
#print(lst.index(3))
#print(len(lst))
#lst.clear()
#print(lst)

#display elements in the reverse order
# a=['abc','def','ghi','jkl']
# a.reverse()
# print(a)

#concatenation of lists
# a=[10,20,30]
# b=['one','two','three']
# print(a+b)

#repetation of list
# a=[10,20,30]
# print(a*3)

#membership in list
# lst=[10,20,30,40,45,50]
# a=25
# b=30
# print(a in lst)
# print(b in lst)
# print(a not in lst)
# print(b not in lst)

#aliasing a list
# lst1=[10,20,30,40,45,50]
# lst2=lst1
# print(lst1)
# print(lst2)
# lst2[3]=4
# print(lst1)
# print(lst2)

#cloninig a list
# lst1=[10,20,30,40,45,50]
# lst2=lst1[:]
# lst2[3]=4
# print(lst2)
# print(lst1)

#counting how many times an elements is found in the list
# a=[]
# n=int(input('how many elements you want to enter?:'))
# for i in range(n):
# 	print('enter an element:',end='')
# 	a.append(int(input()))
# print('the value of list is:',a)
# find=int(input('enter an element to count:'))
# count=0
# for i in a:
# 	if(find==i):
# 		count=count+1
# print('{} is found {} time(s).'.format(find,count))

#finding common elements in two available lists
# fruits1=['apple','banana','pineapple','grapes']
# fruits2=['watermelon','banana','kiwi','strawberry']
# set1=set(fruits1)
# set2=set(fruits2)
# print(set1.intersection(set2))
# s3=set1.intersection(set2)
# print(s3)
# l1=list(s3)
# print(l1)

#create a list which contains square of 1-10
# sqr=[]
# for i in range(1,11):
#  	sqr.append(i**2)
# print(sqr)

#tuple
# a=(1,)
# print(a)
# a=(1)
# print(a)
# a=1,
# print(a)
# a=1,2,3,4,5
# print(a)
# lst=[1,2,3]
# print(lst)
# tpl=tuple(lst)
# print(tpl)

# tpl=(1,2,3,4,5,6,7,8,9,10)
# print(tpl)
# print(tpl[2:6])
# print(tpl[2:6:2])

#storing value of tuple into 2 different variable
# tpl=('atmiya',1)
# uni,rank=tpl[0:2]
# print(uni)
# print(rank)

#function for tuple(len,min,max,count,index,sorted)
# tpl=(1,2,3,4,5,6,7,8)
# print(len(tpl))
# print(min(tpl))
# print(max(tpl))
# print(tpl.count(5))
# print(tpl.index(5))
# tpl=(1,2,3,4,55,6,7,8)
# print(sorted(tpl))

#nested tuples
# tpl=(10,20,30,(1,2,3))
# print(tpl)

#update the value in tuple at the desired position
# num=(1,2,3,4,5)
# print(num)
# lst=list(num)
# print(lst)
# a=int(input('enter the position to insert the value:'))
# lst[a]=int(input('enter the value to be update:'))
# print(lst)
# num=tuple(lst)
# print(num)

#dictionary
# dic={1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno'} 
# print(dic)
# print('the roll no of students are',dic.keys())
# print('the name of students are',dic.values()) 
# a=len(dic)
# print('number of elements in the dictionary are:',a)
# dict1={'eid':1,'name':'abc','sal':1000}
# print(dict1)
# dict1['sal']=100000 
# print(dict1)
# print('the salary of the employee is:',dict1['sal'])
# print('the name of the employee is:',dict1['name'])
# dict1['designation']='developer' 
# print(dict1)
# del dict1['name'] 
# print(dict1)
# print('name' in dict1)
# print('name' not in dict1)

#methods of dictionary
# dict1={'eid':1,'name':'abc','sal':1000}
# print(dict1)
# dict2=dict1.copy()
# print(dict1)
# print(dict2)
# a1=dict1.keys() 
# print(a1)
# a1=dict1.values() 
# print(a1)
# print(dict1.get('name')) 
# dict1.update({'sal':25000}) 
# print(dict1)
# print(dict1.items()) 
# dict1.pop('name') 
# print(dict1)
# print(dict1.clear()) 
# a=dict1.clear()
# print(a)

#take subject name and its corresponding marks from student and give the total of all subjects
# marks={}
# print('how many subjects you want to enter?:',end='')
# n=int(input())
# for i in range(n):
# 	print('enter the subject name:',end='')
# 	key=input()
# 	print('enter the marks:',end='')
# 	value=int(input())
# 	marks.update({key:value})
# print('the value of dictionary is:',marks)
# total=sum(marks.values())
# print('total of all the subjects is:',total)

# #display the marks of the subject, and asked by the users
# print('enter the name of the subject to know its marks:',end='')
# subject=input()
# marks=marks.get(subject,-1)
# if(marks==-1):
# 	print('enter the valid subject name')
# else:
# 	print('the marks in {} are {}.'.format(subject,marks))

#sorting elements of a dictionary using lambda
# months={3:'march',12:'december',1:'january'}
# a=sorted(months.items(),key=lambda e:e[0])
# print(a)
# b=sorted(months.items(),key=lambda e:e[1])
# print(b)
# a=sorted(months.items(),key=lambda e:e[0],reverse=True)
# print(a)
# b=sorted(months.items(),key=lambda e:e[1],reverse=True)
# print(b)

#converting lists into dictionary
# object_class=['flower','fruit','vegetable']
# value_name=['rose','mango','tomato']
# a=zip(object_class,value_name)
# print(a)
# print(type(a))
# dic=dict(a) 
# print(dic)

#passing dictionary to the function
# def func(dictionary):
# 	for i,j in dictionary.items():
# 		print(i,':',j)
# dic={1:'abc',2:'cde',3:'efg'}
# func(dic)

#it is a part of collections method 
# from collections import OrderedDict
# dic=OrderedDict()
# dic[1]='abc'
# dic[2]='cde'
# dic[3]='efg'
# dic[4]='ghi'
# for i,j in dic.items():
# 	print(i,j)

#3-----------------------------
#function
#to add two numbers using funcion
# def summation(a,b):
# 	sum=a+b
# 	print('the sum of two digit is:',sum)
# summation(3,6)
# summation(3.6,6.3)

#returning results from the function
# def summation(a,b):
# 	sum=a+b
# 	return sum
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
# odd_or_even(2)	
# odd_or_even(3)

#to check whether entered number is odd or even using function
#number=int(input('enter the number to check:'))
# def odd_or_even(number):
# 	if number%2==0:
# 		print('the number is even')
# 	else:
# 		print('the number is odd')
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
# number=int(input('enter the number to check:'))
# pos_neg_zer(number)

#returning multiple values from a function 
# def arithmatic(a,b):
# 	add=a+b
# 	sub=a-b
# 	mul=a*b
# 	div=a/b
# 	return add,sub,mul,div
# a,s,m,d=arithmatic(10,2)
# print('the addition of two numbers is:',a)
# print('the substraction of two numbers is:',s)
# print('the multipliction of two numbers is:',m)
# print('the division of two numbers is:',d)

#working with immutable objects
# def modify(a):
# 	a=7
# 	print('the value of a, in the body of function is',a,id(a))
# a=9
# modify(a)
# print('the value of a, in the body of function is',a,id(a))

#working with mutable objects
# def modify(lst):
# 	lst.append(7)
# 	print(lst,id(lst))
# lst=[1,2,3,4,5]
# modify(lst)
# print(lst,id(lst))

#list of actual arguments(4 types):
#1). positional arguments
# def conc(s1,s2):
# 	combined=s1+s2
# 	print(combined)
# conc('atmiya','university')
# conc('university','atmiya')

#2). keyword arguments
# def  stud_det(enr,name):
# 	print('the enrollment of student is:',enr)
# 	print('the name of student is:',name)
# stud_det(enr=111,name='abc')
# stud_det(name='abc',enr=111)

#3). default arguments
# def stud_det(enr,name='abc'):
# 	print('the enrollment of student is:',enr)
# 	print('the name of student is:',name)
# stud_det(enr=111,name='abc')
# stud_det(enr=111)

#4). variable length arguments
# def add(farg,*args):
# 	print('formal argument is',farg)
# 	sum=0
# 	for i in args:
# 		sum=sum+i
# 		print('the sum of all numbers:',(farg+sum))
# add(2,3)
# add(2,3,4)
# add(2)

#passing group of elements in a function
# def display(lst):
# 	for i in lst:
# 		print(i)
# print('enter elements separated by space:',end='')
# lst=[a for a in input().split()]
# #calling the function
# display(lst)

#anonymous function (also know as lambda)
# square=lambda a:a*a
# a=int(input('enter the number to know its square:'))
# print('the square of the entered number is:',square(a))

#generators
# def generator1(a,b):
# 	while a<=b:
# 		yield a
# 		a=a+1
# #filling the generator object
# gen=generator1(1,10)
# for i in gen:
# 	print(i,end='')
# #print(next(gen))
# gen=generator1(1,10)

#to create a text file and store some data into it.
# f=open('myfile.txt')
# f=open('myfile.txt','w')
# str1=input('enter the text you want to write into the file:')
# f.write(str1)
# f.close()

# #reading the existing file
# f=open('myfile.txt','r')
# str1=f.read()
# print(str1)
# f.close()

# #append into an existing file
# f=open('myfile.txt','a+')
# print('enter the text you want to append:')
# while str1!='$':
# 	str1=input() 
# 	if(str1!='$'):
# 		f.write(str1)
# 		break
# f.close()
# f=open('myfile.txt','r')
# str=f.read()
# print(str)
# f.close()

# #to check whether to the file is available or not, if available open the file
# import os
# fname=input('enter the file name to open:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# 	str1=f.read()
# 	print(str1)
# else:
# 	print(fname+'does not exist')
# f.close()

# #counting number of lines,words and characters if the files is available.
# import os
# fname=input('enter the file name to open:')
# if os.path.isfile(fname):
# 	f=open(fname,'r')
# else:
# 	print(fname+'does not exist')
# cl=cw=cc=0
# for line in f:
# 	words=line.split()
# 	cl=cl+1
# 	cw=cw+len(words)
# 	cc=cc+len(line)
# print('number of lines in a file is:',cl)
# print('number of words in a file is:',cw)
# print('number of character in a file is:',cc)
# f.close()

#to copy an image from one file to another
# f=open('d:\\download.png','rb')
# f1=open('d:\\atmiya_logo.png','wb')
# img = f.read()
# f1.write(img)
# f.close()
# f1.close()

#the 'with' statement
# record_length=10 
# with open('stationery_store','wb') as f:
# 	n=int(input('how many items you want to add?:'))
# 	for i in range(n):
# 		stat_item=input('entert the name of stationery:')
# 		length=len(stat_item) 
# 		stat_item=stat_item+(record_length-length)*''
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# with open('stationery_store','rb') as f:
# 	str1=f.read()
# 	print(str1.decode())
# 	print(type(str1))
# 	print(str1)

#zipping the content of files
# from zipfile import *
# f=ZipFile('demo.zip','w',ZIP_DEFLATED) 
# f.write('d:\\download.png')
# f.write('d:\\atmiya_logo.png')
# f.close()

# #unzipping the file
# from zipfile import *
# z=ZipFile('demo.zip','r')
# z.extractall('d:')

# with open('stationery_store','wb') as f:
# 	n=int(input('how many items you want to add?:'))
# 	for i in range(n):
# 		stat_item=input('entert the name of stationery:')
# 		length=len(stat_item) 
# 		stat_item=stat_item.encode()
# 		f.write(stat_item)
# 		f.write("\n".encode())

#random accessing the binary files (using mmap)
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
# 		n=mm.find(name.encode())
# 		n1=n+len(name) 
# 		en=mm[n1:n1+3] 
# 		print('the enrollment of said student is:',en.decode())
# 	if(choice==3):
# 		name=input('enter the name of student, for which you want to modify the enrollment number:')
# 		n=mm.find(name.encode())
# 		n1=n+len(name) 
# 		en1=input('enter the modified enrollment number:')
# 		mm[n1:n1+3]=en1.encode() 
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
# str1='net cat mat matter' 
# result=prog.search(str1) 
# print(result.group()) 
# str2='later or sooner truth of man matters' 
# result=prog.search(str2) 
# print(result.group()) 

#create a regular expression to search for string starting with 'm' a having total 3 characters using findall().
# import re
# str1='net cat mat matter'
# result=re.findall(r'm\w\w',str1)
# print(result)

#use of split()
# import re
# str1='Hello! All, Good; Morning'
# result=re.split(r'\W+',str1)
# print(result)

#create a regular expression that replaces a string with the new string
# import re
# str1='AITS is the best Organization'
# print(str1)
# result=re.sub(r'AITS','Atmiya University',str1)
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
# result=re.findall(r'\d[\w]*',str1) 
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
#5-----------------------
#pandas
# import pandas as pd
# df=pd.read_csv('stud.csv')
# print(df)

#working with .xlsx file using pandas
# import pandas as pd
# import xlrd
# df=pd.read_excel('stud.xlsx')
# print(df)

#working with python dictionary using pandas
# stud={'roll':[1,2,3,4,5],'name':['aa','bb','cc','dd','ee'],'city':['rajkot','surat','mumbai','goa','diu']}
# import pandas as pd
# df=pd.DataFrame(stud)
# print(df)

#working with python tuples using python
# stud=[{1,'aa','surat'},{2,'bb','diu'},{3,'cc','rajkot'},{4,'dd','goa'},{5,'ee','mumbai'}]
# import pandas as pd
# df=pd.DataFrame(stud,columns=['roll','name','city'])
# print(df)

#knowing number f row and columns
# import pandas as pd
# import xlrd
# df=pd.read_excel('stud.xlsx')
# print(df)
# print(df.shape)
#display first five records
#print(df.head())
#display first two records
#print(df.head(2))
#display last five records
#print(df.tail())
#display last two records
#print(df.tail(2))
#reteieving range of rows/records
#print(df[2:5])
#reteieving data from columns
#print(df[['name','city']])
#finding the maximum value
#print(df['marks'].max())
#finding the minimum value
#print(df['marks'].min())
#display students who belongs to rajkot
#print(df[df.city=='rajkot'])
#display students whose marks are more than 50
#print(df[df.marks>50])
#display the name of student who belongs to surat
#print(df[['name']][df.city=='surat'])
#print(df[['name','roll']][df.city=='surat'])
#handling the missing data
# import pandas as pd
# import xlrd
# df=pd.read_excel('stud.xlsx')
# #print(df)
# new=df.fillna({'roll':'roll no missing','name':'name is missing','city':'city is missing'})
# print(new)
# ***********************************
#bar graph
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_excel('bookstall.xlsx')
# print(df)

# extracting the type_of_book and sales into x and y
# x=df['types_of_book']
# y=df['sales']
# plt.bar(x,y,label='category wise sales of books',color='pink')
# plt.xlabel('type_of_book')
# plt.ylabel('sales in rs.')
# plt.title('atmiya book stall')
# plt.legend()
# plt.show()

#display employee id on x-axis and their salaries on y-axis in the form of a bargraph for two department
# import matplotlib.pyplot as plt
# x=[101,102,99,110,125]
# y=[25000,45000,12000,55000,38000]
# x1=[111,120,199,100,215]
# y1=[35000,40000,22000,25000,41000]
# plt.bar(x,y,label='production department',color='blue')
# plt.bar(x1,y1,label='coa department',color='red')
# plt.xlabel('emp_id')
# plt.ylabel('salary')
# plt.title('tata motors')
# plt.legend()
# plt.show()

#pie chart
# import matplotlib.pyplot as plt
# sales_per=[35,10,25,30]
# prod_name=['hatch back','sedan','premium','commercial']
# col=['red','green','yellow','blue']
# plt.pie(sales_per,labels=prod_name,colors=col)
# plt.title('maruti suzuki')
# plt.legend()
# plt.show()

#line graph
# import matplotlib.pyplot as plt
# years=('2023','2022','2021','2020','2019')
# incr_pop=[70,45,29,35,75]
# incr_pop1=[65,85,90,55,45]
# plt.plot(years,incr_pop,color='blue')
# plt.plot(years,incr_pop1,color='yellow')
# plt.title('population growth of india')
# plt.xlabel('years')
# plt.ylabel('increase_of_population_in_lakhs')
# plt.show()

#scatter diagram
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.randn(10)
# print(x)
# y=np.random.randn(10)
# plt.scatter(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('scatter diagram')
# plt.show()

#area plot
# import numpy as np
# import matplotlib.pyplot as plt
# x=range(1,6)
# y=[2,4,1,6,8]
# plt.fill_between(x,y)
# plt.title('area plot')
# plt.show()

#group bargraph
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import xlrd
# df=pd.read_excel('stationary.xlsx')
# print(df)
# year=[2021,2022,2023]
# x=df['pencil']
# y=df['pen']
# xaxis=np.arange(len(year))
# plt.bar(xaxis-0.2,x,0.4,label='pencil')
# plt.bar(xaxis+0.2,y,0.4,label='pen')
# plt.xticks(xaxis,year)
# plt.xlabel('year')
# plt.ylabel('sales')
# plt.legend()
# plt.show()
