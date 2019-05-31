import pandas as pd
from matplotlib import pyplot as plt


# 读取本地数据
file_path = "./IMDB-Movie-Data.csv"
data = pd.read_csv(file_path)


# 处理数据
rating = data.loc[:, "Rating"]*10
rating = rating.astype("int")
bin_width = 5

a = rating.min()
b = rating.max()

bins_num = int((b-a)//bin_width)


# 设置图形
plt.figure(figsize=(20, 8), dpi=60)

# 设置x轴  存在图形与x轴标签偏移情况，怎么解决？？？？？？
_x = list(range(a, b+5, 5))

_xticks = [x/10 for x in _x]

plt.xticks(_x, _xticks)

#
plt.hist(rating, bins=_x)  # bins盒子，可以按照
plt.show()