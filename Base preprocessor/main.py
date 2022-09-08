import pandas as pd
import numpy as np

df=pd.read_csv('Add file name here')
column_list=df.columns.values
null_columns=[i for i in column_list if df[i].isnull().any()==True]
sizedf=np.size(df,axis=0)

diff=list(set(column_list) - set(null_columns))

int_list=[j for j in diff if df[j].dtype in (int,np.short,np.int64,np.int16,np.int32)]
float_list=[k for k in diff if df[k].dtype in (float,np.double,np.float64,np.longdouble,np.longfloat,np.float32)]
string_list=[l for l in diff if df[l].dtype in (str,object)]

int_nulllist=[j for j in null_columns if df[j].dtype in (int,np.short,np.int64,np.int16,np.int32)] 
float_nulllist=[k for k in null_columns if df[k].dtype in (float,np.double,np.float64,np.longdouble,np.longfloat,np.float32)]
string_nulllist=[l for l in null_columns if df[l].dtype in (str,object)]