import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd

df=pd.read_excel('report.xlsx')
print(df)

years=[2022,2023,2024]

x=df['pencil']
x1=df['pen']

xaxis=np.arange(len(years))

plt.bar(xaxis -0.2,x,0.4,label='pencil')
plt.bar(xaxis +0.2,x1,0.4,label='pen')

plt.xlabel('years')
plt.ylabel('products')
plt.title('sales in stationary')
plt.legend()
plt.show()
