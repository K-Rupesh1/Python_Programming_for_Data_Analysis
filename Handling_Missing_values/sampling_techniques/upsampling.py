import numpy as np
import pandas as pd

# set random seed  for reproducibility.
np.random.seed(123)

# create a dataframe with two classes
n_sample=1000
class_0_ratio=0.9
n_class_0=int(n_sample*class_0_ratio)
n_class_1=int(n_sample-n_class_0)

print(n_class_0,n_class_1)

# create dataframe with imbalanced dataset
class_0=pd.DataFrame({
    'feature1':np.random.normal(loc=0,scale=1,size=n_class_0), # loc:mean,scale:standard deviation
    'feature2':np.random.normal(loc=0,scale=1,size=n_class_0),
    'target':[0]*n_class_0
})
class_1=pd.DataFrame({
    'feature1':np.random.normal(loc=0,scale=1,size=n_class_1),
    'feature2':np.random.normal(loc=0,scale=1,size=n_class_1),
    'target':[1]*n_class_1
})

df=pd.concat([class_0,class_1]).reset_index(drop=True)
print(df.head())
print(df.tail())

target_count=df['target'].value_counts()
print(target_count)

# up sampling
minority=df[df['target']==1]
majority=df[df['target']==0]
print(majority)
print(minority)

from sklearn.utils import resample
updated_minority_sample=resample(minority,replace=True,n_samples=len(majority),random_state=42)
print(updated_minority_sample.shape)
updated_dataframe=pd.concat([majority,updated_minority_sample])
print(updated_dataframe)
print(updated_dataframe['target'].value_counts())

