"""
To normalize and create proper structure.
Takes in all kinds on values and applies appropriate methods to
normalize the data.
At each call pass in values of column along with attribute specfic details.
"""

from null import *

def intnorm():
    for i in mainint:
        df[i].apply(lambda x: round(x))
    pass

def floatnorm():
    for j in mainfloat:
        df[j].apply(lambda x: round(x,2))
    pass

def stringnorm():
    for k in mainstring:
        df[k].apply(lambda x: x.strip())
        df[k].apply(lambda x: x.capitalize())
    pass

intnorm()
floatnorm()
stringnorm()

print(df.info())

# download the file onto your device using the pandas to_csv() command