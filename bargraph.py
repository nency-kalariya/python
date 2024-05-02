import pandas as pd
import xlrd
import matplotlib.pyplot as plt

df=pd.read_excel('bookss.xlsx')
print(df)

x=df['books']
y=df['sales']

#bar() function
plt.bar(x,y,label='type of books',color='red')

#x and y axis label
plt.xlabel('books')
plt.ylabel('sales')

plt.title('BOOK STORE')
plt.legend()
plt.show()