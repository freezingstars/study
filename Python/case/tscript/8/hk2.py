import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'STKAITI'
plt.rcParams['font.size'] = 20

data = pd.read_csv("temperature.csv", encoding="utf-8")
data["month"] = pd.to_datetime(data["month"])

plt.plot(data["month"], data["temperature"])
plt.title("某地全年气温变化折线图")
plt.xlabel("月份")
plt.ylabel("气温")
plt.show()
