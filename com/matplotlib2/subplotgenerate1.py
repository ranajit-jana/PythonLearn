import matplotlib.pyplot as plt
import numpy as np




x=np.arange(0,4 * np.pi, 0.1 )
print(4 * np.pi)
print(x)
y_sin=np.sin(x)
y_cos=np.cos(x)
#print(y)


plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.show()
