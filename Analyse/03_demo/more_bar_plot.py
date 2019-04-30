from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


# data
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

# 图形设置
myfont = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC", size=14)
plt.figure(figsize=(20, 8), dpi=60)

bar_width = 0.25  # 偏移的值取值范围最好在(0~.3) 不能大于0.33  不然图形会重叠

x_14 = range(len(a))
x_15 = [x+bar_width for x in x_14]
x_16 = [x+bar_width for x in x_15]

plt.xticks(x_15, a, fontproperties=myfont)


# plot
plt.bar(x_14, b_14, width=bar_width, label="9月14日")
plt.bar(x_15, b_15, width=bar_width, label="9月15日")
plt.bar(x_16, b_16, width=bar_width, label="9月16日")

plt.legend(prop=myfont)
plt.show()
