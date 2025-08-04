# -*- coding: utf-8 -*-

import pandas as pd
from io  import  StringIO


df = pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code",header=0,match="Country")

print(df)

