import matplotlib.pyplot as plt

value=[13,45,10,22,10]
names=['mca','mba','mtech','msc','bsc']

plt.pie(value,labels=names)

plt.title('Students in Stream')
plt.legend()
plt.show()