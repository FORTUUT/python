'''
python公选课作业
可视化之柱状图
'''

import DataCleaning
import matplotlib.pyplot as plt

data_2 = DataCleaning.data[["sex", "tip"]]
data_2 = data_2.groupby('sex', as_index=False).mean()

x = []
y = []
for i in data_2.index:
    x.append(data_2.loc[i, "sex"])
    y.append(data_2.loc[i, "tip"])

plt.title("性别与小费的关系")
plt.xlabel("性别")
plt.ylabel("小费")
plt.bar(x, y, width=0.5)
plt.show()
