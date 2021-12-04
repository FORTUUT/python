import pandas as pd
import re

data = pd.read_excel('E:/desktop/python/data/tips_1.xls')
data = pd.DataFrame(data)

data1 = data[["tip"]]
data1.fillna('0$', inplace=True)
data[["tip"]] = data1

data1 = data[["smoker"]]
data1.fillna('No', inplace=True)
data[["smoker"]] = data1

data = data.dropna()

for i in data.index:
    data.loc[i, "total_bill"] = float(re.sub(r'.$', "", data.loc[i, "total_bill"]))
for i in data.index:
    data.loc[i, "tip"] = float(re.sub(r'.$', "", data.loc[i, "tip"]))
for i in data.index:
    data.loc[i, "size"] = int(re.sub(r'.$', "", data.loc[i, "size"]))

for i in data.index:
    if data.loc[i, "sex"] != 'Female' and data.loc[i, "sex"] != 'Male':
        data.drop(i, inplace=True)
for i in data.index:
    if data.loc[i, "smoker"] != 'No' and data.loc[i, "smoker"] != 'Yes':
        data.drop(i, inplace=True)
for i in data.index:
    if data.loc[i, "time"] != 'Dinner' and data.loc[i, "time"] != 'Lunch':
        data.drop(i, inplace=True)
for i in data.index:
    a = data.loc[i, "day"]
    if a != 'Sun' and a != 'Sat' and a != 'Thur' and a != 'Fri' and a != 'Mon' and a != 'wed' and a != 'Tue':
        data.drop(i, inplace=True)
