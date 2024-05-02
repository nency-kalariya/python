#5
#data science tools and libraries
#pandas
#working the .csv file using pandas
# import pandas as pd
# df=pd.read_csv('stud.csv')
# print(df)

#working with .xlsx file using pandas
#creating data frame from .xlsx files [package require : xlrd , openpyxl]
# import pandas as pd
# import xlrd
# df=pd.read_excel('stud.xlsx')
# print(df)

#working with python dictionary using pandas
#creating data frame from python dictionary
# stud={'roll':[1,2,3,4,5],'name':['aa','bb','cc','dd','ee'],'city':['rajkot','surat','mumbai','goa','diu']}
# import pandas as pd
# df=pd.DataFrame(stud)
# print(df)

#working with python tuples using python
#creating data frame from tuples
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
# print(df[['name']][df.city=='surat'])
# print(df[['name','roll']][df.city=='surat'])

#handling the missing data
# import pandas as pd
# import xlrd
# df=pd.read_excel('stud.xlsx')
# #print(df)
# new=df.fillna({'roll':'roll no missing','name':'name is missing','city':'city is missing'})
# print(new)

#data visualization
#need to import the module named 'matplotlib'
#bar graph
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_excel('bookstall.xlsx')
# print(df)

# #extracting the type_of_book and sales into x and y
# x=df['types_of_book']
# y=df['sales']
# #creating the bar graph using bar()
# plt.bar(x,y,label='category wise sales of books',color='pink')
# #setting the label of x-axis and y-axis
# plt.xlabel('type_of_book')
# plt.ylabel('sales in rs.')
# #setting the title of the ownership
# plt.title('atmiya book stall')
# #showing the legend
# plt.legend()
# #display the graph
# plt.show()

#display employee id on x-axis and their salaries on y-axis in the form of a bargraph for two department
# import matplotlib.pyplot as plt
# #taking employee id and salary of production departments
# x=[101,102,99,110,125]
# y=[25000,45000,12000,55000,38000]
# #taking employee id and salary of departments
# x1=[111,120,199,100,215]
# y1=[35000,40000,22000,25000,41000]
# #creating the bargraph
# plt.bar(x,y,label='production department',color='blue')
# plt.bar(x1,y1,label='coa department',color='red')
# #setting the label and legend
# plt.xlabel('emp_id')
# plt.ylabel('salary')
# plt.title('tata motors')
# plt.legend()
# #to display the graph
# plt.show()

#pie chart
#display the data of the sales of four different products of the company in the form of pie chart
# import matplotlib.pyplot as plt
# #taking the percentage of sales of different products
# sales_per=[35,10,25,30]
# #taking the names of the products
# prod_name=['hatch back','sedan','premium','commercial']
# #giving color to each product category 
# col=['red','green','yellow','blue']
# #creating the pie chart using pie()
# plt.pie(sales_per,labels=prod_name,colors=col)
# #setting up the legend and titles
# plt.title('maruti suzuki')
# plt.legend()
# #display the chart
# plt.show()

#line graph
#to draw a line chart to inresert population increase in last five years
# import matplotlib.pyplot as plt
# years=('2023','2022','2021','2020','2019')
# incr_pop=[70,45,29,35,75]
# incr_pop1=[65,85,90,55,45]
# #creating a line graph using plot()
# plt.plot(years,incr_pop,color='blue')
# plt.plot(years,incr_pop1,color='yellow')
# #setting the title and labels
# plt.title('population growth of india')
# plt.xlabel('years')
# plt.ylabel('increase_of_population_in_lakhs')
# #display the chart
# plt.show()

#scatter diagram
# import matplotlib.pyplot as plt
# import numpy as np
# #the value of x and y must be same-random is a sub module of numpy which has a function randm
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
#the np.arrange() from numpy library is used to create range of values.
#we are creating the x-axis values depending on the number of groups.
#the width of bars of each group is set.
# xaxis=np.arange(len(year))
# plt.bar(xaxis-0.2,x,0.4,label='pencil')
# plt.bar(xaxis+0.2,y,0.4,label='pen')
# #it helps to set the current ticks location.
# plt.xticks(xaxis,year)
# #setting the label for x-axis and y-axis
# plt.xlabel('year')
# plt.ylabel('sales')
# #setting the legend and display the graph
# plt.legend()
# plt.show()