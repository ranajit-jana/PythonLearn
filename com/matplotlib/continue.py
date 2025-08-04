import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,20)
y = x*x 
#np.arange(21,41)


plt.scatter(x,y,c='r',marker='*')

plt.title("simple graph")

plt.xlabel("xside")
plt.ylabel("ylable")

plt.show()