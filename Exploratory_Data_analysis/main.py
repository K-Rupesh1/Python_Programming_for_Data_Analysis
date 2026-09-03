import pandas as pd
# Load dataset
df=pd.read_csv("Exploratory_Data_analysis/winequality-red.csv",sep=';')

# print dataset
print(df.head())

# information about a dataset
print(df.info())

# describe dataset
print(df.describe())

# shape of a dataset
print(df.shape)

# columns present
print(df.columns)
# values present in a quality
print(df['quality'].unique())
count=df['quality'].value_counts()
print(count)

# checking null values
print(df.isnull().sum())

# checking duplicates
print(df[df.duplicated()])

# remove duplicates
print(df.drop_duplicates(inplace=True))

# shape of a dataset  
print(df.shape) 

# corr of a dataset
print(df.corr())

# heat map of a data set with values
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,60))
sns.heatmap(df.corr(),annot=True)
plt.show()

# visualization on quality
sns.pairplot(df)
plt.show()
sns.barplot(df['quality'].value_counts())
plt.xlabel('Wine Quality')
plt.ylabel('Values')
plt.show()

#categorical plot
sns.catplot(x='quality',y='alcohol',data=df,kind='box')
plt.show()
sns.scatterplot(x='alcohol',y='pH',hue='quality',data=df)
plt.show()