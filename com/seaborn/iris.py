import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(sb.load_dataset("iris"))


print(df.head(3))
print(df.corr(numeric_only=True))

#sb.heatmap(df.corr(numeric_only=True))

#sb.jointplot(x='sepal_length', y='sepal_width', data=df,kind='hex')
#sb.jointplot(x='sepal_length', y='petal_length', data=df,kind='hex')

#sb.jointplot(x='sepal_width', y='petal_width', data=df,kind='hex')
#sb.jointplot(x='sepal_width', y='petal_length', data=df,kind='hex')



#sb.jointplot(x='sepal_length', y='sepal_width', data=df,kind='reg')
#sb.jointplot(x='sepal_length', y='petal_length', data=df,kind='reg')

#sb.jointplot(x='sepal_width', y='petal_length', data=df,kind='reg')
#sb.jointplot(x='sepal_width', y='petal_length', data=df,kind='reg')

#sb.pairplot(data=df, hue='species')
sb.pairplot(data=df, kde=False)
#sb.pairplot(data=df, hue='smoker')
#sb.distplot(df['tip'])
#sb.distplot(df['tip'],kde=False) #KDE - kernel density estimation
#sb.distplot(df['tip'],kde=False,bins=50) #No idea what is bin- search TODO
plt.show()


