# import pandas as pd
# import re
# import numpy as np
import matplotlib.pyplot as plt
import test01

data_1 = test01.data
print(data_1)
# x = []
# y = []
# for i in data_1.index:
#        x.append(data_1.loc[i, "total_bill"])
#        y.append(data_1.loc[i, "tip"])

x = data_1[["total_bill"]]
y = data_1[["tip"]]

print(x)
print(y)
plt.scatter(x, y)
plt.show()
