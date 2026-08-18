import pandas as pd

# create a series from a data 
# series is a one dimensional array
data=[1,2,3,4,5]
series=pd.Series(data)
print(f"series \n",series)
print(type(series))

# create a series from dictionary
data={'a':1,'b':2,'c':3}
series_dict=pd.Series(data) # keys act as index 
print(series_dict)

# Data Frame
# Data Frame is a two dimensional array
# create a data frame of  dictionary of lists
data={
    'name':['rupesh','rajesh','umesh'],
    'age' :[21,31,19],
    'city':['anantapur','banglore','hindupur']
}
df=pd.DataFrame(data)
print(df)

# create a data frame of list of dictionaries
data=[
    {'name':'rupesh','age':21,'city':'anantapur'},
    {'name':'umesh','age':19,'city':'hindupur'},
    {'name':'rajesh','age':31,'city':'banglore'}
]
df=pd.DataFrame(data)
print(df)

df=pd.read_csv('C:/Users/Kurak/Downloads/Data_ANalysis_Using_Python/pandas_package/sample_data.csv')
print(df)

# getting top rows
print(df.head(2))

# getting last rows
print(df.tail(2))
print()

# getting values by index values , coloum name
print(df.loc[2])
print(df.loc[1:3])
print(df.loc[0,'Name'])
print()

print(f"{df.iloc[2]}\n")
print(df.iloc[1:3])

# accessing a elements by headers
print(df['Name'])

# accessing particular elements by index number and header
print(df.at[1,'Name'])

# accessing particular elements by row and coloum number
print(df.iat[0,1])


# adding a salary coloum
df['salary']=[50000,60000,70000]
print(df)

# remove the salary coloum
print(df.drop('salary',axis=1))

# remove elements by index
print(df.drop(1))

print(df)

# remove permenentely
df.drop('salary',axis=1,inplace=True)
print(df)

# update age coloum by +5 years
df['updated_age']=df['Age']+5
print(df)

# update age for only one person 
df.loc[0,'updated_age']+=1
print(df)