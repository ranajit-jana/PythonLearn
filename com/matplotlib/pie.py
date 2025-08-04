import matplotlib.pyplot as plt

activities = ['Sleep', 'Study', 'Exercise', 'Entertainment', 'Others']
hours = [8, 6, 2, 5, 3]
explode=(0.1,0.1,0.1,0.01,0.3)

plt.pie(hours,labels=activities,explode=explode)