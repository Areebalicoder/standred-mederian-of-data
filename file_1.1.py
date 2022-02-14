import csv 
import plotly.express as px
import pandas as pd
import statistics

sum=0
marks=[]
df=pd.read_csv("class1.csv")

with open("class1.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
for i in filedata:
    sum=sum+float(i[1])
    marks.append(float(i[1]))
a=sum/len(filedata)
print(a)

z=statistics.stdev(marks)
print(z)

lower=a-z
print(lower)

upper=a+z
print(upper)

fig=px.scatter(df, x="Student Number", y="Marks", size="Marks")
fig.show()
