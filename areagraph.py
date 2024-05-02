import numpy as np
import matplotlib.pyplot as plt

x=range(1,6)
y=[5,2,1,6,3]

plt.fill_between(x,y)

plt.title('Area Graph')
plt.show()