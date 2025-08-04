import pandas as pd


df = pd.read_csv("customfile.csv", sep="%")
print(df)


df = pd.read_csv("customfile.csv", sep="%", usecols=['col1','col3'])


print(df)