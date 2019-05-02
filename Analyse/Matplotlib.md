## matplotlib

-   python底层的绘图库

-   基本使用案例：

    时间10-12点间，气温的变化图形

    ```python
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
    
    # 方法二：通过字体管理器  window下有效
    myfont = font_manager.FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC")  # 传入字体地址
    
    # 方法三：网上方法  仅限window下使用，测试有效
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    
    plt.plot(x, y)  # 传入数据
    
    # 数据显示，设置x轴坐标显示中文
    _xticks_label = ["10时{}分".format(i) for i in x if i < 60]
    _xticks_label += ["11时{}分".format(i-60) for i in x if i >= 60]
    plt.xticks(x[::5], _xticks_label[::5], rotation=45, fontproperties=myfont)
    # plt.xticks(x[::5], _xticks_label[::5], rotation=45)  # 对应设置字体，方法一，方法二
    
    # 添加描述信息
    
    # 显示图形
    plt.show()
    ```

    关于男女朋友个数随年龄变化的趋势图

    ```python
    from matplotlib import pyplot as plt
    from matplotlib.font_manager import FontProperties
    
    # 准备数据
    x = range(11, 31)
    y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
    z = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
    
    # 设置图形显示
    # 图形大小
    plt.figure(figsize=(15, 6), dpi=80)
    # 字体
    myfont = FontProperties(fname=r"C:\WINDOWS\FONTS\MSYH.TTC", size=16)
    # 标题
    plt.xlabel("年龄", fontproperties=myfont)
    plt.ylabel("数量 (个)", fontproperties=myfont)
    plt.title("11岁~30岁交往女(男)朋友数量的走势图", fontproperties=myfont)
    
    # 设置x, y显示格式
    _xticks = ["{}岁".format(x) for x in x]
    plt.xticks(x, _xticks, fontproperties=myfont)
    plt.yticks(range(1, 10))
    
    # 设置网格 alpha透明度(0-1)
    plt.grid(alpha=0.4)
    
    # plot画图
    plt.plot(x, y, label="自己")
    plt.plot(x, z, label="同桌")
    
    # 设置图例 需要在画图后设置，因为在画图前设置，不知道你需要画几条数据
    # 第一步: 在画图时，需要设置label参数，即图例名称
    # 第二步: 设置图例，prop参数-设置字体  loc参数-设置图例位置(具体查看源码3)
    plt.legend(prop=myfont, loc=0)
    
    # 保存，显示
    plt.savefig("朋友个数走势图.png")
    plt.show()
    ```

    