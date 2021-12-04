import test01
import matplotlib.pyplot as plt

data_4 = test01.data[["size", "tip"]]
data_4 = data_4.groupby('size', as_index=False).mean()

print(data_4)

x = []
y = []
for i in data_4.index:
    x.append(data_4.loc[i, "size"])
    y.append(data_4.loc[i, "tip"])

print(x)
print(y)

plt.bar(x, y)
plt.show()
