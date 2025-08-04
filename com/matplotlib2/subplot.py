import matplotlib.pyplot as plt
import numpy as np




x=[1,2,3,4]
y=[10,20,25,30]
z=[5,10,15,20]
a=[15,10,15,20]



plt.subplot(1,3,1)
plt.tight_layout()
plt.plot(x,y, marker='*')

plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.subplot(1,3,2)
plt.tight_layout()
plt.plot(x,z, marker='*')

plt.xlabel("xlabel")
plt.ylabel("zlabel")

plt.subplot(1,3,3)
plt.tight_layout()
plt.plot(x,a, marker='*')

plt.xlabel("xlabel")
plt.ylabel("alabel")
plt.show()
