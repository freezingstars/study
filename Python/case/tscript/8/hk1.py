import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'STKAITI'
plt.rcParams['font.size'] = 16

x = list(range(1, 7))
y = [i ** 2 for i in x]

plt.plot(x, y, linewidth=3)
plt.title("数字的平方数折线图", fontsize=24)
plt.xlabel("数字")
plt.ylabel("数字的平方")
plt.tick_params(axis='both')
plt.show()
