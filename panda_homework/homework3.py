
import pandas as pd


df = pd.read_csv("/home/rj/projects/mercedes/mercedesbenz.csv")
newdf = df.iloc[11:15]
print(newdf["ID"]>30)

#print(df.iloc[0:2,0:2])
#print(df.loc[0:2,['ID','y']])
#df.info()
#print(df.describe())