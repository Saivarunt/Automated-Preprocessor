""" 
Check if a given attribute is categorical.
Condition: If string, object or int opt for categorical test.
Seperate categorical functions based on the data type of the attribute.
At each call pass in values of column along with attribute specfic details.
"""

import pandas as pd

def check(x):
    tlist=[]
    for i in x.columns:
        for j in x[i]:
            if j.isnumeric():
                tlist.append(i)
    return tlist

def cat_null(x,dt):
    x=pd.DataFrame(x)
    x.dropna(axis=0,inplace=True)
    if dt==str:    
        cval=check(x)
        if len(cval)>0:
            try:
                y=pd.DataFrame(x[cval],dtype=int)
                x.drop(cval,inplace=True)
                x.merge(y,left_index=True,right_index=True)
            except:
                pass

    truevalue_list=[]
    for i in x.columns:
        if (len(x[i].unique())>0 and len(x[i].unique())<=10):
            truevalue_list.append(i)
    return (truevalue_list)

def cat_fill(x):
    # for all null values.
    x=pd.DataFrame(x)
    for c in x.columns:
        valcnt=x[c].value_counts(dropna=True)
        valcntidx=valcnt.index
        # filling it with max or min depends on size and bias based off of how the categories are distributed, 
        # here by default we try to support the max class
        maxval=valcnt.max()

        for i in valcntidx:
            if valcnt[i]==maxval:
                x[c]=x[c].fillna(i)
                break
    return x