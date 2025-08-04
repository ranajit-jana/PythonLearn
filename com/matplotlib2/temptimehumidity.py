import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator



"""
temp=[20,22,32,19,18,18,19,21,24,27,30,33,28,26,22,22]

humidity=[80,85,87,90,87,92,88,65,50,55,45,50,70,75]

"""
hourofday=np.arange(0,24, 1 )
temp=    [20,22,32,19,18,18,19,21,24,27,30,33,28,26,22,22,30,21,31,26,27,27,22,29]
#print(len(temp))

humidity=[80,85,87,90,87,92,88,65,50,55,45,50,70,75,90,87,92,88,65,50,55,45,50,75]
#print(len(humidity))
plt.subplot(2,1,1)
plt.tight_layout()
plt.xlabel("time")
plt.ylabel("temp")
plt.plot(hourofday,temp,color='r')

plt.subplot(2,1,2)
plt.tight_layout() 
plt.xlabel("time")
plt.ylabel("humidity")
plt.plot(hourofday,humidity)


plt.show()