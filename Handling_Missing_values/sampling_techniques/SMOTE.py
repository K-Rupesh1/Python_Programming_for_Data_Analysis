# SMOT(Synthetic Minority OverSampling Technique)
import pandas as pd
from sklearn.datasets import make_classification
x,y=make_classification(n_samples=1000,n_redundant=0,n_features=2,n_clusters_per_class=1,weights=[0.90],random_state=12)
print(x,y)

df1=pd.DataFrame(x,columns=['f1','f2'])
df2=pd.DataFrame(y,columns=['target'])
final_dataframe=pd.concat([df1,df2],axis=1)
print(final_dataframe)
print(final_dataframe.target.value_counts())

import matplotlib.pyplot as plt
plt.scatter(final_dataframe['f1'],final_dataframe['f2'],c=final_dataframe['target'])
plt.show()

# Over Sampling by using SMOTE
from imblearn.over_sampling import SMOTE
over_sample=SMOTE()
x,y=over_sample.fit_resample(final_dataframe[['f1','f2']],final_dataframe['target'])
print(x.shape)
print(y.shape)
print(len(y[y==0]))
print(len(y[y==1]))

df1=pd.DataFrame(x,columns=['f1','f2'])
df2=pd.DataFrame(y,columns=['target'])
final_dataframe=pd.concat([df1,df2],axis=1)
plt.scatter(final_dataframe['f1'],final_dataframe['f2'],c=final_dataframe['target'])
plt.show()
