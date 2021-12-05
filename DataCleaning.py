'''
python公选课作业
项目主文件之数据清洗
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('E:/desktop/tips_1.xls')

data1 = data[["tip"]]
data1.fillna('0$', inplace=True)
data[["tip"]] = data1

data1 = data[["smoker"]]
data1.fillna('No', inplace=True)
data[["smoker"]] = data1

data = data.dropna()

data['total_bill'] = data['total_bill'].str.replace("$", "")
data['total_bill'] = data['total_bill'].astype(float)
data['tip'] = data['tip'].str.replace("$", "")
data['tip'] = data['tip'].astype(float)
data['size'] = data['size'].str.replace("人", "")
data['size'] = data['size'].astype(int)

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

a = data["total_bill"].quantile(0.75)
b = data["total_bill"].quantile(0.25)
for i in data.index:
    if data.loc[i, "total_bill"] >= (a - b) * 1.5 + a or data.loc[
            i, "total_bill"] < b - (a - b) * 1.5:
        data.drop(i, inplace=True)

a = data["size"].quantile(0.75)
b = data["size"].quantile(0.25)
for i in data.index:
    if data.loc[i, "size"] >= (a - b) * 1.5 + a or data.loc[
            i, "size"] < b - (a - b) * 1.5:
        data.drop(i, inplace=True)

a = data["tip"].quantile(0.75)
b = data["tip"].quantile(0.25)
for i in data.index:
    if data.loc[i, "tip"] >= (a - b) * 1.5 + a or data.loc[
            i, "tip"] < b - (a - b) * 1.5:
        data.drop(i, inplace=True)
print(data)

a = data["total_bill"].mean() + data["total_bill"].std() * 4
b = data["total_bill"].mean() - data["total_bill"].std() * 4
for i in data.index:
    if data.loc[i, "total_bill"] > a or data.loc[i, "total_bill"] < b:
        data.drop(i, inplace=True)

a = data["tip"].mean() + data["tip"].std() * 4
b = data["tip"].mean() - data["tip"].std() * 4
for i in data.index:
    if data.loc[i, "tip"] > a or data.loc[i, "tip"] < b:
        data.drop(i, inplace=True)

a = data["size"].mean() + data["size"].std() * 4
b = data["size"].mean() - data["size"].std() * 4
for i in data.index:
    if data.loc[i, "size"] > a or data.loc[i, "size"] < b:
        data.drop(i, inplace=True)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot()
plt.show()
