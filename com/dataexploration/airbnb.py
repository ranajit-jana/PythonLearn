'''
Airbnb Listings in a City (e.g., NYC)
Dataset: http://insideairbnb.com/get-the-data.html

Goal:
Explore pricing, availability, and location trends.

Questions:
Which neighborhoods have the highest prices?

Is there seasonality in bookings?

How do room types differ in cost?

Seaborn EDA:
sns.boxplot() for price by neighborhood

sns.histplot() for distribution of availability

sns.heatmap() for geographical density (requires some mapping)
'''
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import ast


df=pd.read_csv("airbnblistings.csv")

print("\n".join(df.columns))

#print(df)


#print(df.groupby("neighbourhood")["price"].mean())

print(df.groupby("neighbourhood")["availability_365"].mean())