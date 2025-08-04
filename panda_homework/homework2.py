# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("my.csv",index_col=0)
df.index.name=None
print(df)
