import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
df=pd.read_excel('Exploratory_Data_analysis/flight_price_dataset/flight_price.xlsx')
print(df)
# dataset info
print(df.info())
# describe dataset
print(df.describe())
# head
print(df.head())
# change date_of_journey into day,month,year
df['journey_day']=df['Date_of_Journey'].str.split('/').str[0]
df['journey_month']=df['Date_of_Journey'].str.split('/').str[1]
df['journey_year']=df['Date_of_Journey'].str.split('/').str[2]
print(df.head())
print(df.info())

# change datatype 
df['journey_day']=df['journey_day'].astype(int)
df['journey_month']=df['journey_day'].astype(int)
df['journey_year']=df['journey_day'].astype(int)
print(df.info())

# drop Date of Journey Column
df.drop('Date_of_Journey',axis=1,inplace=True)
print(df.info())
print(df.head(2))

# departure time as hour and minute
df['dep_hour']=df['Dep_Time'].str.split(':').str[0]
df['dep_minute']=df['Dep_Time'].str.split(':').str[1]

# remove DEP_time column
df.drop('Dep_Time',axis=1,inplace=True)
print(df.info())

# chage data type
df['dep_hour']=df['dep_hour'].astype(int)
df['dep_minute']=df['dep_minute'].astype(int)
print(df.info())
print(df.head(2))
# Remove Route column
df.drop('Route',axis=1,inplace=True)
print(df.head(2))

# checking unique values in additional info
print(df['Additional_Info'].unique())

# checking unique values in Total_Stops
print(df['Total_Stops'].unique())

# convert stops into numerical values
df['Total_Stops']=df['Total_Stops'].map({'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4,np.nan:1})
print(df.head())

# DUration as hours and minutes
df['duration_hour']=df['Duration'].str.split(' ').str[0].str.split('h').str[0]
df['duration_minute']=df['Duration'].str.split(' ').str[1].str.split('m').str[0]
print(df.info())
print(df.head())
df['duration_minute']=df['duration_minute'].fillna('0')
print(df['duration_minute'].unique())

# if hour value is '5m' in duration hour use below statement to solve this.
df['duration_hour']=df['duration_hour'].str.extract(r'(/d+)h').fillna(0)
# change data type 
df['duration_hour']=df['duration_hour'].astype(int)
df['duration_minute']=df['duration_minute'].astype(int)
print(df.info())

# remove Duration column
df.drop('Duration',axis=1,inplace=True)
print(df.info())
print(df.head(2))

# Arrival time as hour and minutes
df['arrival_time']=df['Arrival_Time'].str.split(' ').str[0]
df['arrival_hour']=df['arrival_time'].str.split(':').str[0]
df['arrival_minute']=df['arrival_time'].str.split(':').str[1]
print(df.head(2))

# remove arrival time,Arrival_Time
df.drop(['Arrival_Time','arrival_time'],axis=1,inplace=True)
print(df.head(2))
print(df.info())

# change data type
df['arrival_hour']=df['arrival_hour'].astype(int)
df['arrival_minute']=df['arrival_minute'].astype(int)
print(df.info())

encoder=OneHotEncoder()
encoded=encoder.fit_transform(df[['Airline','Source','Destination']]).toarray()
print(encoded)
# convert encoded values into dataframe
encoder_df=pd.DataFrame(encoded,columns=encoder.get_feature_names_out())
print(encoder_df)
print(df.head(2))

# drop columns
df.drop(['Airline','Source','Destination','Additional_Info'],axis=1,inplace=True)
print(df.head(2))

from sklearn.preprocessing import OrdinalEncoder
encoder=OrdinalEncoder()
encoded=encoder.fit_transform(df[['Airline','Source','Destination']])
print(encoded)
# convert encoded values into dataframe
encoder_df=pd.DataFrame(encoded,columns=encoder.get_feature_names_out())
print(encoder_df)