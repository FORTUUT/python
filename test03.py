import test01
import matplotlib.pyplot as plt

data_2 = test01.data[["sex", "tip"]]
data_2 = data_2.groupby('sex', as_index=False).mean()

# print(data_2)
# y = data_2[["tip"]].as
# x = data_2[["sex"]]
x = []
y = []
for i in data_2.index:
    x.append(data_2.loc[i, "sex"])
    y.append(data_2.loc[i, "tip"])

plt.bar(x, y)
plt.show()
