import numpy as np
from matplotlib import pyplot as plt


# 读取数据
files_path = "./youtube_video_data/GB_video_data_numbers.csv"
data = np.loadtxt(files_path, delimiter=",", dtype="int")

# 选择数据
comment = data[:, -1]
comment = comment[comment <= 6000]


# 绘制直方图
plt.figure(figsize=(20, 8), dpi=60)

# 确定组距
print(comment.max(), comment.min())
# 假设分为20组
d = 300
bin_nums = (comment.max()-comment.min())//d

plt.xticks(list(range(comment.min(), comment.max()+d))[::d])

plt.hist(comment, bins=bin_nums)

plt.show()
