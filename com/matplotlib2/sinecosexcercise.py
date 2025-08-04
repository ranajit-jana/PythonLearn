"""

1.. Sine Wave — Modeling Sound Waves

Scenario:

Sound waves can be modeled as sine waves because they are periodic vibrations in air pressure.

Explanation:

The air pressure varies sinusoidally over time, creating compressions and rarefactions that our ears interpret as sound.


2. Cosine Wave — Modeling Daylight Intensity Over a Year

Scenario:

The amount of daylight (solar intensity) over the course of a year roughly follows a cosine curve because of the Earth's tilt and orbit.

Explanation:

Daylight length changes periodically, peaking at summer solstice and minimum at winter solstice — a smooth wave similar to a cosine function.

"""


#5 oscillations in 2*pi seconds
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

time=np.linspace(0,2 * np.pi, num=100)

soundwave = np.sin(5*time)


#months = np.arange(0,12, 1 )
#intesity=np.sin(months)

solarintensity=10+(5*np.cos(time))

plt.subplot(2,1,1)
plt.tight_layout()
plt.xlabel("time")
plt.ylabel("soundwave")
plt.plot(time,soundwave,color='r')

plt.subplot(2,1,2)
plt.tight_layout() 
plt.xlabel("time")
plt.ylabel("solar intensity")
plt.plot(time,solarintensity)


plt.show()