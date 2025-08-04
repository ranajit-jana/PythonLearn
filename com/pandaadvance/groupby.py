# -*- coding: utf-8 -*-

import pandas as pd

import seaborn as sea

import matplotlib.pyplot as py


data= {
       
       "department":["IT","HR","IT","IT","HR" ],
       "salary":[10000,12000,20000,43000,12000]
       
       
       }

df = pd.DataFrame(data)

#res = df.groupby("department")["salary"].sum()

res = df.groupby("department")["salary"].sum().reset_index()

print(res)


sea.barplot(y="department",x="salary",data=res)

py.show()