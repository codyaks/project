import pandas as pd
import numpy as np
exam_data={"name":["ram",'sita','gita','shyam','krishna'],'score':[34,55,np.nan,67,90,],'attempts':[1,3,2,4,5],'qualify':['yes','no','yes','yes','no']}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print(df.info())
print(df.head())
new_df=df.dropna()
print(new_df.head())