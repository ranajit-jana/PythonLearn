import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(sb.load_dataset("tips"))
print(df.head(1))

#sb.countplot(xz="sex",data=df)
#sb.barplot(x='sex', y='smoker',data=df)
sb.boxplot(x='sex',y='total_bill',data=df)
plt.show()


    