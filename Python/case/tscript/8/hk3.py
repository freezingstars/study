import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 101)
y = x * np.random.rand(101)

plt.scatter(x, y, s=20)
plt.title("散点图示例图", fontsize=24)
plt.xlabel("X的值")
plt.ylabel("Y的值")
plt.tick_params(axis='both', labelsize=16)
plt.show()
