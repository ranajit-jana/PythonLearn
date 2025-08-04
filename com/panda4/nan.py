import pandas as pd
from io  import  StringIO


data =  ("col1,col2,col3,col4\n"
        "x,y,10,40\n"
        "a,b,1,")
data1 =  ("col1,col2,col3,col4\n"
        "x,y,10,40\n"
        "a,b,1,5")
df = pd.read_csv(StringIO(data1),dtype={'col3':int,'col4':float})
                  
print(df)