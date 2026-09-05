import pandas as pd
from io import StringIO
data='[{"name":"Rupesh","email":"kurakularupesh1234@gmail.com","job profile":"software developer"}]'
df=pd.read_json(StringIO(data))
print(df)
print()
#convert dataframe into json
df=df.to_json(orient='index')
print(df)
df=df.to_json(orient='records')
print(df)

df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None)
print(df.head(5))
#to save as csv file
df.to_csv("wine.csv")

url="https://www.fdic.gov/bank-failures/failed-bank-list"
df=pd.read_html(url)[0]
print(df)

df=pd.read_csv("C:/Users/Kurak/Downloads/Data_ANalysis_Using_Python/Reading_data_from_various_sources_using_pandas/wine.csv")
# convert the csv data as a excel data
excel=df.to_excel("sample.xlsx")
