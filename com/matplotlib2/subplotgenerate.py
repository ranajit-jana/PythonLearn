import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator



x=np.linspace(0,2 * np.pi, num=100)


plt.plot(x,np.sin(x),label="sin(x)")
plt.plot(x,np.cos(x),label="cos(x)")
# Access current axes
ax = plt.gca()

# Set grid spacing to 0.5
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
plt.legend()
plt.grid(True)
plt.show()
