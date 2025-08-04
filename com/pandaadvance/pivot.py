import pandas as pd
import seaborn as sea
import matplotlib.pyplot as py

"""
# 1. Heatmap: Monthly trends across years
# 2. Lineplot: Year-wise total passengers (growth over years)
# 3. Barplot: Average passengers by month (seasonal performance)
"""

df = sea.load_dataset("flights")
print(df.head(2))

yearly = df.groupby("year")["passengers"].sum().to_frame()
monthly = df.groupby("month")["passengers"].sum().to_frame()

avgmonthly =  df.groupby("month")["passengers"].mean().to_frame()
print(yearly)
print(avgmonthly)

sea.heatmap(df.pivot(index='month', columns="year", values='passengers'))
sea.jointplot(x='year', y='passengers', data=yearly ,kind='reg')
sea.barplot(x='month', y='passengers', data=avgmonthly)

py.show()