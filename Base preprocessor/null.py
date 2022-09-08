"""
Functions to fill null entries based on type of data.
Function calls can be direct as well as indirect.
At each call pass in values of column along with attribute specfic details.
"""


from main import *
from categorical import *
from non_categorical import *

# intval floatval stringval all contain categorical values and the rest are non categoriacal.
def intfill():
    intval=cat_null(df[int_nulllist],int)
    difference_int=list(set(int_nulllist)-set(intval)) # use difference in both lists to call non categorical val

    if len(intval)==0:
        print("no val")
        pass
    else:
        df[intval]=cat_fill(df[intval])
        print(df[intval].isnull().any())
    
    if len(difference_int)==0:
        print("no val")
        pass
    else:
        df[difference_int]=ncat_ifill(df[difference_int])
        print(df[difference_int].isnull().any())

def stringfill():
    stringval=cat_null(df[string_nulllist],str)
    difference_string=list(set(string_nulllist)-set(stringval))

    if len(stringval)==0:
        print("no val")
        pass
    else:
        df[stringval]=cat_fill(df[stringval])
        print(df[stringval].isnull().any())

    if len(difference_string)==0:
        print("no val")
        pass
    else:
        df[difference_string]=ncat_sfill(df[difference_string])
        print(df[difference_string].isnull().any())

def floatfill():
    floatval=cat_null(df[float_nulllist],float)
    difference_float=list(set(float_nulllist)-set(floatval))

    if len(floatval)==0:
        print("no val")
        pass
    else:
        df[floatval]=cat_fill(df[floatval])
        print(df[floatval].isnull().any())

    if len(difference_float)==0:
        print("no val")
        pass
    else:
        df[difference_float]=ncat_ffill(df[difference_float])
        print(df[difference_float].isnull().any())


intfill()
stringfill()
floatfill()

mainint=[j for j in df.columns if df[j].dtype in (int,np.short,np.int64,np.int16,np.int32)]
mainfloat=[k for k in df.columns if df[k].dtype in (float,np.double,np.float64,np.longdouble,np.longfloat,np.float32)]
mainstring=[l for l in df.columns if df[l].dtype in (str,object)]