import pandas as pd
from matplotlib import pyplot as plt


# 读取数据
data = pd.read_csv("./BeijingPM20100101_20151231.csv")
print(data.info())
print(data.iloc[:, :7].head(), "\n", data.iloc[:, 10:].head(), "\n", data.iloc[:5, 7:10])

# 时间序列
# 年月日分列显示的，可以先转换为pandas对应的时间序列
periodindex = pd.PeriodIndex(year=data["year"], month=data["month"], day=data["day"], hour=data["hour"], freq="H")

data.set_index(periodindex, inplace=True)
# 对数据进行重采样，进行降采样， 从1小时降为10天
cn_data = data["PM_Dongsihuan"].resample("10D").mean()
us_data = data["PM_US Post"].resample("10D").mean()
# cn_data = cn_data.dropna(axis=0)
# us_data = us_data.dropna(axis=0)

# 准备数
x = cn_data.index
y = cn_data.values
us_x = us_data.index
us_y = us_data.values
plt.figure(figsize=(20, 8), dpi=60)

plt.plot(range(len(us_x)), us_y, label="US")
plt.plot(range(len(x)), y, label="CN")

plt.xticks(range(len(x))[::5], x[::5], rotation=45)
plt.legend()

plt.show()



