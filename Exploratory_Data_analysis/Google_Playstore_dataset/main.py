import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df1=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')
df=df1.copy()
#print(df1.head())

# info of dataset
print(df1.info())
# shape of a dataset
print(df1.shape)
# describe a dataset
print(df1.describe())

# copy the dataset
df=df1.copy()
# clean the data
#print(df['Reviews'].unique().astype(int))
print(df['Reviews'].str.isnumeric().sum())
print(df[~df['Reviews'].str.isnumeric()])

# drop row 10472
df.drop(df.index[10472],axis=0,inplace=True)
print(df[~df['Reviews'].str.isnumeric()])
print(df.shape)
# chage data type
df['Reviews']=df['Reviews'].astype(int)
print(df.info())
print(df.head(2))

# size coloum
print(df['Size'].unique())
# Convert million into thousands 1m = 1000000
# 19000K==19M
df['Size']=df['Size'].str.replace('M','000')
df['Size']=df['Size'].str.replace('k','000')
df['Size']=df['Size'].str.replace('+','')
df['Size']=df['Size'].str.replace(',','')
df['Size']=df['Size'].replace('Varies with device',np.nan)
print(df['Size'].unique())
# change data type
df['Size']=df['Size'].astype(float)
print(df.info())

# Installs column
print(df['Installs'].unique())
print(df['Price'].unique())

Chars_to_remove=['+',',','$']
columns=['Installs','Price']
for item in Chars_to_remove:
    for col in columns:
        df[col]=df[col].str.replace(item,'')
df['Installs']=df['Installs'].replace('Free','0')

#print(df['Installs'].unique())
#print(df['Price'].unique())
print(df.info())
print(df.loc[df['Price'] == 'Everyone'])
df.drop(df.index[10472],inplace=True)
# change data type
df['Installs']=df['Installs'].astype(int)
df['Price']=df['Price'].astype(float)
print(df.info())

# last updated feature
print(df['Last Updated'].unique())
print(df.loc[df['Last Updated']=='1.0.19'])
# drop index location 10472
#df.drop(index=[10472],inplace=True)
# convert into date,month,year
df['Last Updated']=pd.to_datetime(df['Last Updated'])
df['Updated_day']=df['Last Updated'].dt.day
df['Updated_month']=df['Last Updated'].dt.month
df['Updated_year']=df['Last Updated'].dt.year
print(df.head(2))
print(df.info())
df.drop('Last Updated',axis=1,inplace=True)
print(df.info())
df.to_csv("Exploratory_Data_analysis/Google_Playstore_dataset/Cleaned_Dataset.csv")


# EDA analysis
df=pd.read_csv("Exploratory_Data_analysis/Google_Playstore_dataset/Cleaned_Dataset.csv")
print(df.head(2))
print(df.shape)
df.drop('Unnamed: 0',axis=1,inplace=True)

# Check Duplicate apps
print(df['App'].duplicated().sum())

# Remove Duplicates
df=df.drop_duplicates(subset=['App'],keep='first')
print(df.shape)

# find numeric and categorical columns
numeric_features=[feature for feature in df.columns if df[feature].dtype!='O']
categorical_features=[feature for feature in df.columns if df[feature].dtype =='O']
print("we have {} numerical features : {}".format(len(numeric_features),numeric_features))
print(" \n we have {} categorical features : {}".format(len(categorical_features),categorical_features))
print(df.info())

# proportional count of categorical features
for col in categorical_features:
    print(df[col].value_counts(normalize=True)*100)
    print("-------------------------------------")
    
# proportional count of numerical features
plt.figure(figsize=(15,15))
plt.suptitle('Univariate Analysis of Numerical Features',fontsize=20, fontweight='bold', alpha=0.8, y=1.) # used as a main title 
for i in range(0,len(numeric_features)):
    plt.subplot(5,3,i+1)
    sns.kdeplot(x=df[numeric_features[i]],fill=True,color='blue')
    plt.xlabel(numeric_features[i])
    plt.tight_layout()
plt.show()

# on categorical features
plt.figure(figsize=(20, 15))
plt.suptitle('Univariate Analysis of Categorical Features', fontsize=20, fontweight='bold', alpha=0.8, y=1.)
category = [ 'Type', 'Content Rating']
for i in range(0, len(category)):
    plt.subplot(2, 2, i+1)
    sns.countplot(x=df[category[i]],palette="Set2")
    plt.xlabel(category[i])
    plt.xticks(rotation=45)
    plt.tight_layout() 
plt.show()

# most popular app category
Category_counts=df['Category'].value_counts()
plt.figure(figsize=(15,16))
plt.title('Most Popular app Categories')
plt.pie(Category_counts,labels=Category_counts.index,autopct='%1.1f')
plt.show()

# top 10 app categories
Category=pd.DataFrame(df['Category'].value_counts())
Category.rename(columns={'Category':'count'},inplace=True)
print(Category)

plt.figure(figsize=(15,6))
sns.barplot(x=Category.index[:10], y ='count',data = Category[:10],palette='hls')
plt.title('Top 10 App categories')
plt.xticks(rotation=90)
plt.show() 

# Which Category has largest number of installations?? 
df_cat_installations=df.groupby(df['Category'])['Installs'].sum().sort_values(ascending=False).reset_index()
df_cat_installations['Installs']=df_cat_installations['Installs']/1000000000
df2=df_cat_installations.head(10)
plt.figure(figsize = (14,10))
sns.set_context("talk")
sns.set_style("darkgrid")

ax=sns.barplot(x='Installs',y='Category',data=df2)
ax.set_xlabel('No. of Installations in Billions')
ax.set_ylabel('')
ax.set_title("Most Popular Categories in Play Store", size = 20)
plt.show()