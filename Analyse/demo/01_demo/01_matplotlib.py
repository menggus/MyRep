from matplotlib import pyplot as plt

x = range(2, 26, 2)

y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
fig = plt.figure(figsize=(15, 6), dpi=80)

# 设置x轴刻度
plt.xticks(x)
plt.xticks(range(2, 26, 1))  # 传入参数为刻度的列表

# 设置y轴的刻度
plt.yticks(range(min(y), max(y)+1))



plt.plot(x, y)
# 保存图片
plt.savefig("./01.png")
plt.show()
