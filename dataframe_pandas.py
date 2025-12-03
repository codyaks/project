import pandas as pd
import numpy as np
company={"id":[1,2,3,4],"name":["gita","ram","syam","laxman"],"role":["ceo",None,None,None],"salary":[200,300,None,None]}
df=pd.DataFrame(company)
print(df.head(2))
print(df.tail(2))
print(df.info())
new_df=df.dropna()
print(new_df)
new_df2=df.dropna(axis=1)
print(new_df2)
df['salary'].fillna(300,inplace=True)
print(df)
df['role'].fillna("ceo",inplace=True)
print(df)