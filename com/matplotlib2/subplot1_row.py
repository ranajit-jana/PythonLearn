import matplotlib.pyplot as plt
import numpy as np




x=[1,2,3,4]
y=[10,20,25,30]
z=[5,10,15,20]
a=[15,10,15,20]



plt.subplot(3,1,1)

plt.plot(x,y, marker='*')

plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.subplot(3,1,2)

plt.plot(x,z, marker='*')

plt.xlabel("xlabel")
plt.ylabel("zlabel")

plt.subplot(3,1,3)

plt.plot(x,a, marker='*')

plt.xlabel("xlabel")
plt.ylabel("alabel")
plt.show()
