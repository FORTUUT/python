'''
python公选课作业
可视化之散点图
'''

import matplotlib.pyplot as plt
import DataCleaning

data_1 = DataCleaning.data
print(data_1)

x = data_1[["total_bill"]]
y = data_1[["tip"]]

print(x)
print(y)

plt.title("消费总额与小费的关系")
plt.xlabel("总金额")
plt.ylabel("小费")

plt.scatter(x, y)
plt.show()
