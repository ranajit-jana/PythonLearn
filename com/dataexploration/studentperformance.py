import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import ast

df = pd.read_csv("StudentsPerformance.xls")

print(df.head())

#Explore how gender, parental education, and test preparation affect student scores.
#gbwgender = df.groupby('gender')["writing score"]
#print(gbwgender.mean())

#gbrgender = df.groupby('gender')["reading score"]
#print(gbrgender.mean())

#gbmgender = df.groupby('gender')["math score"]
#print(gbmgender.mean())

print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

#sea.boxenplot(data=df,x="gender", y= "math score")
#plt.show()
#parentedf = df['parental level of education'].replace({'high school': 1, "associate's degree": 2, "some college":3, "bachelor's degree":4, "master's degree":5}, inplace=True)

df.to_csv("parentaledu.csv")

#Does test preparation improve scores?
"""
gbwgender = df.groupby('test preparation course')["writing score"]
print(gbwgender.mean())

gbrgender = df.groupby('test preparation course')["reading score"]
print(gbrgender.mean())

gbmgender = df.groupby('test preparation course')["math score"]
print(gbmgender.mean())

sea.boxenplot(data=df,x='test preparation course', y= "math score")
"""
print(df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean())

#Does parental education influence outcomes?
df['parental level of education'].replace( {"some high school":1, 'high school': 2, "associate's degree": 3, "some college":4, "bachelor's degree":5, "master's degree":6}, inplace=True)
#df.to_csv("parentaledu.csv")

"""
gbwgender = df.groupby('parental level of education')["writing score"]
print(gbwgender.mean())

gbrgender = df.groupby('parental level of education')["reading score"]
print(gbrgender.mean())

gbmgender = df.groupby('parental level of education')["math score"]
print(gbmgender.mean())
"""
print(df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean())

"""
sea.boxplot(data=df, x="parental level of education", y="writing score")
plt.xticks(rotation=45)
plt.show()
sea.violinplot(data=df, x="parental level of education", y="reading score")
plt.xticks(rotation=45)
plt.title("Reading Scores by Parental Education")

plt.show()
sea.countplot(data=df, x="test preparation course", hue="gender")
plt.title("Test Preparation Course Completion by Gender")
#sea.pairplot(df[["math score", "reading score", "writing score"]])
plt.show()
"""
'''
sea.heatmap(df[["math score", "reading score", "writing score"]].corr(), annot=True)
plt.title("Score Correlation Matrix")
plt.show()
'''
df["average score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

sea.barplot(data=df, x="lunch", y="average score", ci=None)
plt.title("Average Score by Lunch Type")
plt.show()
