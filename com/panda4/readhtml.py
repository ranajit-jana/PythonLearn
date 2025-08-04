import pandas as pd
from io  import  StringIO


df = pd.read_html("sample.html",index_col=0)

print(df)

