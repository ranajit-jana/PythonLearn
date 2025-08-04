import matplotlib.pyplot as plt



days=['mon','tue','wed','thu','fri','sat','sun']

city1=[20,21,20,24,22,21,22]
city2=[23,26,20,23,26,27,26]

plt.ylabel("Centigrade")
plt.plot(days,city1,marker='*' ,linestyle='-',label='city1')
plt.plot(days,city2,marker='s' ,linestyle='--',label='city2')
plt.legend()
plt.ylim(5,50)
plt.show()