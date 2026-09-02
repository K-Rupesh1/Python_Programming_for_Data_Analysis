import pandas as pd
from sklearn.preprocessing import LabelEncoder

lbl_encoder=LabelEncoder()
df=pd.DataFrame({
    'color':['red','green','blue','green','red']
})

# fit // learn the data
# fit transform 
encoded=lbl_encoder.fit_transform(df)
print(encoded)

# transform //convert the data
print(lbl_encoder.transform([['blue']]))
print(lbl_encoder.transform([['red']]))
print(lbl_encoder.transform([['green']]))


# ordinal encoding
from sklearn.preprocessing import OrdinalEncoder

df=pd.DataFrame({
    'size':['medium','small','large','medium','large']
})
 
print(df)
encoder=OrdinalEncoder(categories=[['small','medium','large']])

encoded=encoder.fit_transform(df)
print(encoded)

print(encoder.transform([['medium']]))