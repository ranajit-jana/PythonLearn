
import pandas as pd
from io  import  StringIO


data = '{"empid":["101"],"empName":["John"],"empSal":["10000"]}'

data1 = '{"empid":{"0":101},"empName":{"0":"John"},"empSal":{"0":10000}}'

df = pd.read_json(StringIO(data1))

print(df)