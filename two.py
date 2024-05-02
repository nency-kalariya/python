#array
#syntax
#array_name=array(type_code,[elements])

#example
#1st way to create array
# import array
# a=array.array('i',[1,23,45,67]) #the first array represent the array module and the second array represent the class of module array.
# print(a)

#2nd way to create array
# import array as ar #we have used alias
# a=ar.array('i',[1,23,45,67])
# print(a)

#3rd way to create array
# from array import * #import all the classes, object, variables from the module array.
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
#format : array_name[start:stop:stride]
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

# structure:
# try:
# 	some code
# except:
# 	executed if error in the try block

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

#types of arrays
#1) single dimensional array
#2) multi dimensional array
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
#structure : linspace(start, stop, n)
#start : starting point, stop : ending element, n : no. of parts elements shoud be divided(by default 50) 
# from numpy import *
# a=linspace(2,10,5)
# print(a)
# a=linspace(2,10,9)
# print(a)

#creating array using arange()
#structure arange(start, stop, stepsize)
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
# c=where(a>b,a,b)  #where is the function
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

#slicing and indexing numpy arrays
#slicing
#structure : array_name(start:stop:stepsize)
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)

#retrieving the 1st element to the 6th element alternatively
#print(a[0:6:2])

#retrieving all the elements
# print(a[:])
# print(a[::])

#retrieving all elements from 3rd element and alternatively
#print(a[2:])

#retrieving all elements from 3rd element and alternatively
#print(a[2::2])

#indexing
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# i=0
# while(i<len(a-1)):
# 	print(a[i])
# 	i=i+1

#attributes of an array
#1) ndim : it represents the number of the dimensions of an array
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

#2) shape : it gives the shape of the array
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

#3) size : gives the total number of elements in the array
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

#4) dtype : gives the datatype of the elements in the array
# from numpy import *
# a=array([10,20,30,40,50,60,70])
# print(a)
# print(a.dtype)

#5) reshape() : used to change the shape of an array
# from numpy import *
# a=array([1,2,3,4,5,6,7,8])
# print(a)
# a=a.reshape(2,4)
# print(a)

#6) flatten() : useful to collapse the elements of n array into single dimension array 
# from numpy import *
# a=array([1,2,3,4,5,6,7,8])
# print(a)
# a=a.reshape(2,4)
# print(a)
# a=a.flatten()
# print(a)

#multi-dimensional arrays
#the 2D arrays, 3D arrays etc. are called multi-dimensional arrays
# from numpy import *
# a=array([[10,11,12,13],[14,15,16,17]])
# print(a)

#the reshape()
#used to convert 1D array into a multi-dimensional arrays
#structure : reshape(array name,(n,(r,c)))
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
#structure : array_name[start:stop:stepsize]
# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a[0,:]) #0th row
# print(a[2,:]) #2nd row
# print(a[:,0]) #0th column
# print(a[0:1,0:1]) #element at the 0th row and 0th column
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
# print(st[0:17:1]) #same effect as above
# print(st[0:17:2]) #alternate character
# print(st[-1::-1]) #reverse the string
# print(st[-1::]) #only the last character

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
#structure: string-name.count(substring,begining,end)
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
# 	st.append(input()) #append() is used here
# 	print(st) 
# 	st1=st.sort() #sort() is used here
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
#to create list using range function
#structure: range(start,stop,stepsize)
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
#appending the list(adding the value at the last position)
# lst.append(9)
# print(lst)
#updating the element of the list
# lst[5]=60
# print(lst)
#deleting the element of the list by position
# del lst[5] 
# print(lst)
#deleting the element of the list by value
# lst.remove(5)
# print(lst)
#finding the index of an element
#print(lst.index(3))
#finding the length of a list
#print(len(lst))
#clearing all the elements from the list
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
# #converting lists into set
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
#tuple is similar to list, with one difference that it cannot be modified(immutable).
#writing elements into the variable without any type of brackets will create tuple
# a=(1,)
# print(a)
# a=(1)
# print(a)
# a=1,
# print(a)
# a=1,2,3,4,5
# print(a)
# #convert the list into tuple
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
#data stored in the form of key-value pairs.
#the first element is considerd as key and the immediate value is considered as its value.
#we cannot use slicing or indexing to retrieve elements.
# dic={1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno'} #creating a dictionary
# print(dic)
# #operations on dictionaries
# print('the roll no of students are',dic.keys()) #retriving vlues(key)
# print('the name of students are',dic.values()) #retriving vlues(value)
# #to find length of dictionary
# a=len(dic)
# print('number of elements in the dictionary are:',a)
# dict1={'eid':1,'name':'abc','sal':1000}
# print(dict1)
# dict1['sal']=100000 #updating the salary
# print(dict1)
# print('the salary of the employee is:',dict1['sal']) #display the salary
# print('the name of the employee is:',dict1['name']) #display the name
# dict1['designation']='developer' #adding one more key:value
# print(dict1)
# del dict1['name'] #deleting the key:value
# print(dict1)
# print('name' in dict1) #to check whrther the key inserted is available
# print('name' not in dict1) #to check whrther the key inserted is available

#methods of dictionary
# dict1={'eid':1,'name':'abc','sal':1000}
# print(dict1)
# dict2=dict1.copy()
# print(dict1)
# print(dict2)
# a1=dict1.keys() #to get keys of the dictionary
# print(a1)
# a1=dict1.values() #to get values of the dictionary
# print(a1)
# print(dict1.get('name')) #display the value of specified key
# dict1.update({'sal':25000}) #updating the value of specified key
# print(dict1)
# print(dict1.items()) #display each individual key:value as a separate tuple
# dict1.pop('name') #it removes the value of the specified key
# print(dict1)
# print(dict1.clear()) #it removes all the pairs of key:value
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
#it does not require the name
#it can be written without 'def'
#it is used to perform some calculations easilty
#def functionname(parameter)

#example: a=lambda y,z:y+z
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
# dic=dict(a) #use of dict() to convert zip file into dictionary
# print(dic)
#zip(): it is useful to convert the list or any sequances into a zip object
#we can pass 1 or more sequances to zip

#passing dictionary to the function
# def func(dictionary):
# 	for i,j in dictionary.items():
# 		print(i,':',j)
# #calling the function
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

