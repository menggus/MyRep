from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# 准备数据
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 设置图形的大小
plt.figure(figsize=(15, 6), dpi=80)

# 方法一:设置字体  windows 下无效
# font = {'family': '微软雅黑', 'weight': 'bold', 'size': 12}
# matplotlib.rc("font", **font)

# 方法二：通过字体管理器  window下有效，使用该方法必须每一个显示item均需要传入fontproperties=myfont
myfont = font_manager.FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")  # 传入字体地址

# 方法三：网上方法  仅限window下使用，测试有效， 使用该方法简单，但貌似不能选择字体
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# 添加描述信息
plt.xlabel("时间", fontproperties=myfont)
plt.ylabel("温度 (℃)", fontproperties=myfont)
plt.title("10点~12点间温度的变化情况", fontproperties=myfont)

plt.plot(x, y)  # 传入数据

# 数据显示，设置x轴坐标显示中文
_xticks_label = ["10时{}分".format(i) for i in x if i < 60]
_xticks_label += ["11时{}分".format(i-60) for i in x if i >= 60]
plt.xticks(x[::5], _xticks_label[::5], rotation=45, fontproperties=myfont)
# plt.xticks(x[::5], _xticks_label[::5], rotation=45)  # 对应设置字体，方法一，方法二

# 保存图形
plt.savefig("./03_mat.png")

# 显示图形
plt.show()