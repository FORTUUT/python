'''
python公选课作业
可视化之柱状图
'''

import DataCleaning
import matplotlib.pyplot as plt

data_5 = DataCleaning.data[["day", "size"]]
data_5 = data_5.groupby('day', as_index=False).mean()

x = []
y = []
for i in data_5.index:
    x.append(data_5.loc[i, "day"])
    y.append(data_5.loc[i, "size"])

plt.title("时间与人数的关系")
plt.xlabel("一周时间")
plt.ylabel("人数")
plt.bar(x, y, width=0.5)
plt.show()
