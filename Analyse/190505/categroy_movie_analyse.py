import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


# 需求: 统计不同分类下电影的分布情况

# 读取数据
file_path = "./IMDB-Movie-Data.csv"
data_all = pd.read_csv(file_path)

# 查看数据信息
# print(data_all.info())
# print(data_all[["Title", "Genre"]].head(1))

# 筛选数据：分类和电影数
# 获取所有分类
genre_data = data_all["Genre"].str.split(",")  # 获取Genre，里面包含了所有分类的信息
# 第一步：遍历genre_data获取所有分类信息，但是其中有重复的分类信息
# 第二步：转换为set集合类型，因为集合元素唯一，所以去除重复信息，得到  需要的分类信息
# 第三部：对于分类信息，绘制图形时，需要为列表形式，转换为list类型
genre = list(set([i for j in genre_data for i in j]))

# 统计不同类型下的电影数，每一部电影有多种类型，所以在这里不能使用简单方法进行统计
# 构造一个行数与genre_data一样，列为genre分类，值都为0的DataFrame
npdata = np.zeros(shape=(len(genre_data), len(genre)))
df = pd.DataFrame(npdata, columns=genre)

for i in range(len(genre_data)):
        df.loc[i, genre_data[i]] = 1

# 绘制图形的数据
sum_df = df.sum()  # 结果为Series
sum_df = sum_df.sort_values()  # 排序

# 绘制图形
my_font = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC", size=14)
plt.figure(figsize=(18, 8), dpi=60)
plt.title("不同种类电影数量统计表", fontproperties=my_font)
plt.xlabel("类型", fontproperties=my_font)
plt.ylabel("数量", fontproperties=my_font)

plt.yticks(range(600)[::50])
plt.grid(alpha=0.4)

plt.bar(sum_df.index, sum_df.values, width=0.7, color="orange")

plt.show()




