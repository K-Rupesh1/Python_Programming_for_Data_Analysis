import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
print(df)

#Print five values
print(df.head(5))
print(df.shape)

# print null values
print(df.isnull().sum())

# remove null values
print(df.dropna().shape)
# remove null values by columns
df.dropna(axis=1,inplace=True)
print(df)

# histogram for age
sns.histplot(df['age'],kde=True)
plt.title('AGE')
plt.show()

# fill nan age values with mean of age
df['mean_age']=df['age'].fillna(df['age'].mean())
print(df[['mean_age','age']])

# fill nan age values with meadian
df['median_age']=df['age'].fillna(df['age'].median())
print(df[['median_age','age']])

# fill mode with a categorical value
print(df[df['embarked'].isnull()])
print(df['embarked'].unique())
print(df['embarked'].mode()[0])
df['mode']=df['embarked'].fillna(df['embarked'].mode()[0])
print(df[['mode','embarked']])

sns.pairplot(df)
plt.show()
