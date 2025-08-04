import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,10).reshape(2,5), index=['r1','r2'],columns=['c1','c2','c3','c4','c5'])
                  #,index=['r1','r2'],column=['c1'.'c2','c3','c4','c5'])
#print(df)
print(df.iloc[:,:3:2]) 
