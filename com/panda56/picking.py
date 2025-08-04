import pandas as pd
from io  import  StringIO


df = pd.read_csv("pandas.csv",index_col=0)


#print(df)
print(type(df))
#df.to_pickle("pandas_pickle.pkl")
#print("##############serialized")

#un_pd = pd.read_pickle("pandas_pickle.pkl")
#print("##############unpickled")
#print(un_pd)



hdf = pd.read_html("sample.html")
print(type(hdf))
newhdf = hdf[0]
print(type(newhdf))
newhdf.to_pickle("sample_html.pkl")


#print(hdf)

#hdf.to_pickle("html_pickle.pkl")
#print("##############serialized")

#un_hpd = pd.read_pickle("html_pickle.pkl")
#   print("##############unpickled")
#print(un_pd)

