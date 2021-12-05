'''
python公选课作业
可视化之柱状图
'''

import DataCleaning
import matplotlib.pyplot as plt

data_6 = DataCleaning.data[["sex", "smoker"]]

data_6['smoker'] = data_6['smoker'].str.replace("Yes", "1")
data_6['smoker'] = data_6['smoker'].str.replace("No", "0")
data_6['smoker'] = data_6['smoker'].astype(int)

data_6 = data_6.groupby('sex', as_index=False).count()

x = []
y = []
for i in data_6.index:
    x.append(data_6.loc[i, "sex"])
    y.append(data_6.loc[i, "smoker"])

plt.title("性别与吸烟的关系")
plt.xlabel("性别")
plt.ylabel("吸烟人数")
plt.bar(x, y, width=0.5)
plt.show()
