from matplotlib import pyplot as plt
import random
# import matplotlib
from matplotlib import font_manager

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 方法一:设置字体  windows 下无效
# font = {'family': '微软雅黑', 'weight': 'bold', 'size': 12}
# matplotlib.rc("font", **font)

# 方法二：通过字体管理器  window下有效
myfont = font_manager.FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")  # 传入字体地址
# myfont = font_manager.FontProperties(r"C:\WINDOWS\FONTS\SIMFANG.TTF")

# 方法三：网上方法  仅限window下使用，测试有效
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

plt.figure(figsize=(15, 6), dpi=80)  # 设置图形的大小

plt.plot(x, y)  # 传入数据


_xticks_label = ["10时{}分".format(i) for i in x if i < 60]
_xticks_label += ["11时{}分".format(i-60) for i in x if i >= 60]
# 数据的显示
plt.xticks(x[::5], _xticks_label[::5], rotation=45, fontproperties=myfont)
# plt.xticks(x[::5], _xticks_label[::5], rotation=45)
plt.yticks(y)


plt.show()
