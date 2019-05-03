import numpy as np
from matplotlib import pyplot as plt


# 准备数据
file_path = "./youtube_video_data/GB_video_data_numbers.csv"
data = np.loadtxt(file_path, delimiter=",", dtype="int")

# 筛选需要数据


# 准备plot的x，y
x = data[:, 1]
y = data[:, -1]

# 设置图形
plt.figure(figsize=(20, 8), dpi=80)

# 画图
plt.scatter(x,y)


plt.show()
