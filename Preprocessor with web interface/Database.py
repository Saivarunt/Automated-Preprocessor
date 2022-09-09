#psycopg2
import psycopg2
import pandas as pd
import numpy as np
import pathlib

def main(f):
    df1=pd.read_csv(f)
    f=f.replace("\\","/")
    p=pathlib.PurePosixPath(f)
    n=p.stem
    
    conn=psycopg2.connect(dbname="cleanerdb",user="postgres",password="postgres",host="localhost")
    cursor=conn.cursor()
    val=tuple(df1.values)
    a=list(df1.columns)
    c=0
    dfdtype=list()

    for i in range(len(a)):
        dfdtype.append(df1[a[i]].dtype)

    def insert_val(x):
        ind=0
        s="""INSERT INTO """+n+""" VALUES("""
        while ind<len(val[x]):
            if ind==len(val[x])-1:
                if type(val[x][ind])==str or type(val[x][ind])==object:
                    s=s+"'"+val[x][ind]+"'"+")"
                else:
                    s=s+str(val[x][ind])+')'
            else:
                if type(val[x][ind])==str or type(val[x][ind])==object:
                    s=s+"'"+val[x][ind]+"'"+','
                else:
                    s=s+str(val[x][ind])+','
            ind=ind+1
        cursor.execute(s)

    #create the table name under the file name-- temporary
    cursor.execute("""CREATE TABLE IF NOT EXISTS """+n+"""();""")
    
    while c<len(a):
        if dfdtype[c]==int:
            cursor.execute("""ALTER TABLE """+n+""" ADD COLUMN """+a[c]+""" INT;""")
        elif dfdtype[c]==float:
            cursor.execute("""ALTER TABLE """+n+""" ADD COLUMN """+a[c]+""" FLOAT;""")
        elif dfdtype[c]==object or dfdtype[c]==str:
            cursor.execute("""ALTER TABLE """+n+""" ADD COLUMN """+a[c]+""" VARCHAR(100);""")
        else:
            cursor.execute("""ALTER TABLE """+n+""" ADD COLUMN """+a[c]+""" VARCHAR(100);""")
        c=c+1

    for x in range(len(val)):
        insert_val(x)
    conn.commit()
    conn.close()
    
def gmain(f):
    main(f.name)
    return "Done"
import gradio as gr
g=gr.Interface(gmain,inputs=["file"],outputs="text")
g.launch(debug=True)
