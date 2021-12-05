'''
python公选课作业
可视化之柱状图
'''

import DataCleaning
import matplotlib.pyplot as plt

data_4 = DataCleaning.data[["size", "tip"]]
data_4 = data_4.groupby('size', as_index=False).mean()

x = []
y = []
for i in data_4.index:
    x.append(data_4.loc[i, "size"])
    y.append(data_4.loc[i, "tip"])

plt.title("聚餐时间段/人数与小费的关系")
plt.xlabel("聚餐时间段/人数")
plt.ylabel("小费")
plt.bar(x, y, width=0.5)
plt.show()
