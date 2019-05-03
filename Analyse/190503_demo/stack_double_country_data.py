import numpy as np


# 对两个文件中的数据合并一起进行研究，并且保留国家信息
# 考虑需要合并数组
# 读取数据文件
us_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/US_video_data_numbers.csv"

us_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")
uk_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")

print(len(us_data[:, 0]))

# 构造国家信息数组，0 表示美国  1表示英国
us_info = np.zeros((len(us_data[:, 0]), 1)).astype("int")
uk_info = np.ones((len(uk_data[:, 0]), 1)).astype("int")

# 横向拼接国家信息
us_data = np.hstack((us_data, us_info))
uk_data = np.hstack((uk_data, uk_info))

# 纵向拼接两个国家的数据
data = np.vstack((us_data, uk_data))

#
print(data)


