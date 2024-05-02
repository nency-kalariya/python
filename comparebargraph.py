import matplotlib.pyplot as plt

#production
#id
x=[101,102,103,104,105]
#salary
y=[1000,6512,6555,9898,8989]


#qc
#id
x1=[106,107,108,109,110]
#salary
y1=[65000,555,9888,4555,1111]


plt.bar(x,y,label='Production',color='blue')
plt.bar(x1,y1,label='QC',color='green')

plt.xlabel('Id')
plt.ylabel('salary')
plt.legend()
plt.title('Salary Comparison')
plt.show()


