
import pandas as pd
from io import StringIO

data = ('col1,col2,col3\n'
        'a,b,c\n'
        '1,f,j\n'
        '5,7,3')

print(type(data))

df = pd.read_csv(StringIO(data))
print(df)