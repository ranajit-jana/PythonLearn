import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
expenses = [12000, 15000, 10000, 13000]


plt.plot(months, expenses)

plt.bar(months, expenses,color='a')