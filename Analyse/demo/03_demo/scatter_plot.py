from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


"""
    图形需求： 3月份~10月份 气温的分布散点图
"""

# data
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20, 20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1, 32)
x_10 = range(41, 72)
_yticks = range(0, 35)

# 图形设置
plt.figure(figsize=(15, 6), dpi=80)
myfont = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")

# xy轴刻度
x = list(x_3)+list(x_10)
_xticks = ["3月{}日".format(x) for x in x_3]
_xticks += ["10月{}日".format(x-40) for x in x_10]
plt.xticks(x[::3], _xticks[::3], fontproperties=myfont, rotation=45)
plt.yticks(_yticks[::2])

# 网格
plt.grid(alpha=0.4)

# 标题
plt.title("3月份~10月份 气温的分布散点图", fontproperties=myfont)
plt.xlabel("月份", fontproperties=myfont)
plt.ylabel("温度(℃)", fontproperties=myfont)


# plot 散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

# 图例
plt.legend(prop=myfont)

plt.show()

