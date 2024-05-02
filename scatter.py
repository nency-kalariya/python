import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(10)
y=np.random.randn(10)

plt.scatter(x,y)



plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('scatter graph')
plt.legend()
plt.show()
