import pandas as pd
import seaborn as sea
import matplotlib.pyplot as py
import numpy as np
'''
*predict passenger is survived or not based on sex
*predict passenger is survived or not based on PClass
*find how many nan values are present /null---put it in heatmap
*Explore relationships between passenger features (like age, sex, class) and survival.
*Plot a dist plot to find avg age of the people in the boat
*find the count of siblings and spouse in the boat
*What is the average fare ?plot a graph
*Find the average age value for each passenger class using box plot.
'''

df = pd.read_csv("titanic_train.csv")

#np.where(df['Sex'] == 'Female', 0, 1)
#df['Sex'].replace({'female': 0, 'male': 1}, inplace=True)
print(df.head(2))

#surviveddf = dfgender.groupby("Survived")["Sex"].sum().to_frame()

#sea.boxplot(x='Survived', y='Sex', data=df)
#sea.jointplot(x='Sex', y='Survived', data=df,kind='reg')

#sea.barplot(y="Survived",x="Sex",data=df)
#sea.barplot(y="Survived",x="Pclass",data=df)
#sea.heatmap(df.isnull(), cbar=False)
#sea.heatmap(df.corr(numeric_only=True))

#sea.displot()
#siblings = df["SibSp"].sum()
#print(f"Total siblings and spouse: {siblings}")

#sea.distplot(df['Age'])
#sea.boxplot(x='Pclass',y='Fare',data=df)
#sea.boxplot(x='Pclass',y='Age',data=df)
res1 = df.groupby("Sex")["Age"].mean()
print(res1)
sea.barplot(x="Sex",y="Age",data=res1)

res2 = df.groupby("Pclass")["Age"].mean()
print(res2)

res3 = df.groupby("Pclass")["Survived"].sum()
print(res3)

py.show()
#print(surviveddf)