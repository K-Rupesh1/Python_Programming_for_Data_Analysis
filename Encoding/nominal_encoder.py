import pandas as pd
from sklearn.preprocessing import OneHotEncoder

encoder=OneHotEncoder()
# create a data frame 
'''df=pd.DataFrame({
    'color':['red','green','blue','red','blue']
})
print(df)
# fit and transform the data
encoded=encoder.fit_transform(df[['color']]).toarray()
print(encoded)
# convert array into a dataframe
encoder_df=pd.DataFrame(encoded,columns=encoder.get_feature_names_out())
print(encoder_df)

# add new coloum to dataframe
new=encoder.transform([['blue']]).toarray()
print(new)

print(pd.concat([df,encoder_df],axis=1))'''

import seaborn as sns
df=sns.load_dataset('titanic')
print(df)
encoder=OneHotEncoder()
encoded=encoder.fit_transform(df[['class','who','adult_male']]).toarray()
print(encoded)

encoder_df=pd.DataFrame(encoded,columns=encoder.get_feature_names_out())
print(encoder_df)
print(pd.concat([df[['class','who','adult_male']],encoder_df],axis=1).head())