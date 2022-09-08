""" 
Check if a given attribute is non-categorical.
Condition: If float --> non-categorical test.
Seperate non-categorical functions based on the data type of the attribute.
At each call pass in values of column along with attribute specfic details.
"""

import pandas as pd

def ncat_ifill(x,l):
    x=pd.DataFrame(x)
    x1=x.dropna(axis=0)
    for i in x.columns:
        meanvalue=x1[i].mean()
        x[i].fillna(round(meanvalue))


def ncat_sfill(x):
    x=x.fillna("-")
    # dropping non cat strings is optional

def ncat_ffill(x):
    x=pd.DataFrame(x)
    x1=x.dropna(axis=0)
    for i in x.columns:
        meanvalue=x1[i].mean()
        x[i]=x[i].fillna(meanvalue)
    return x