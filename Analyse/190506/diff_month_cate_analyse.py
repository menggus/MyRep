import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
"""dataframe：时间序列的使用"""
"""绘制不同月份不同类型的电话次数的变换情况"""


# read data
file_path = "./911.csv"
data = pd.read_csv(file_path)

# 分类
temp_list = data["title"].str.split(":")
data["Cate"] = [i[0] for i in temp_list]

# 时间序列化
data["timeStamp"] = pd.to_datetime(data["timeStamp"])
data.set_index(["Cate", "timeStamp"], inplace=True)

# 获取数据
ems_data = data.loc["EMS", :]["title"].resample("M").count()
Fire_data = data.loc["Fire", :]["title"].resample("M").count()
Traffic_data = data.loc["Traffic", :]["title"].resample("M").count()

# 设置图形
plt.figure(figsize=(20, 8), dpi=60)
my_font = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")

plt.plot(ems_data.index, ems_data.values, label="EMS")
plt.plot(Fire_data.index, Fire_data.values, label="Fire")
plt.plot(Traffic_data.index, Traffic_data.values, label="Traffic")

plt.xticks(ems_data.index, ems_data.index.strftime("%Y-%m-%d"), rotation=45)

plt.legend(prop=my_font)

plt.show()







