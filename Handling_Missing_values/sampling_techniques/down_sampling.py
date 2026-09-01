import numpy as np
import pandas as pd

# set random sedd or reproducability
np.random.seed(123)
# create a data frame with two classes
n_sample=1000
class_0_ratio=0.9
class_0=int(n_sample*class_0_ratio)
class_1=n_sample-class_0
#print(class_0,class_1)

# create a dataset imbalanced dataset
class_0=pd.DataFrame({
    'feature1':np.random.normal(loc=0,scale=1,size=class_0),
    'feature2':np.random.normal(loc=0,scale=1,size=class_0),
    'target':[0]*class_0
})
class_1=pd.DataFrame({
    'feature1':np.random.normal(loc=0,scale=1,size=class_1),
    'feature2':np.random.normal(loc=0,scale=1,size=class_1),
    'target':[1]*class_1
})
df=pd.concat([class_0,class_1])
#print(df)

#print(df['target'].value_counts())

minority=df[df['target']==1]
majority=df[df['target']==0]

# down sampling
from sklearn.utils import resample
majority_down_sampling=resample(majority,replace=False,n_samples=len(minority),random_state=42)
print(majority_down_sampling)
print(majority_down_sampling['target'].value_counts())
print(majority_down_sampling.shape)

df_downsampling=pd.concat([minority,majority_down_sampling])
print(df_downsampling)
print(df_downsampling.target.value_counts())