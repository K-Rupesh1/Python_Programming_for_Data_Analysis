import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips=sns.load_dataset('tips')
try:
    tips=sns.load_dataset('tips')
except ValueError:
    print("file path is not exist")
except Exception as e:
    print(" error {e}")
else:
    print(tips)
finally:
    print("exicuted Successfully")
print(tips)


df=tips.groupby('day')['total_bill'].sum()
plt.subplot(2,2,1)
sns.barplot(df,color='purple',edgecolor='black')
plt.show()

# Scatter plot
plt.subplot(2,2,2)
sns.scatterplot(x='tip',y='total_bill',data=tips)
plt.title("total bill vs tip")
plt.show()

# line chart
plt.subplot(2,2,3)
sns.lineplot(x='size',y='total_bill',data=tips)
plt.title("size by total bill")
plt.show()

# box plot
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

# violine plot
sns.violinplot(x='day',y='total_bill',data=tips)
plt.show()

# histogram
sns.histplot(tips['total_bill'],bins=10,kde=True)
plt.show()

# KDE plot
sns.kdeplot(tips['total_bill'],fill=True)
plt.show() 

# Pair Plot
# It will shows the all the relations in a data set
sns.pairplot(tips)
plt.show()

# Heat Map
corr=tips[['total_bill','size','tip']].corr()
print(corr)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show() 