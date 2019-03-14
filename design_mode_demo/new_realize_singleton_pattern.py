# 单例设计：执行过程中只存在一个实例化对象；
# 实现，通过类的new方法，不断返回第一次创建的对象的引用,即对象不变；
#  new 方法实现的单例为伪单例


class Mediaplay:
    # 记录创建对象
    instance = None
    # 记录初始化
    init_flags = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            print("初次创建对象")
        return cls.instance

    def __init__(self, name):
        self.name = name  # 对象为同一对象，但属性会重新初始化
        if not Mediaplay.init_flags:
            super().__init__()
            print("执行初始化")
            # self.name = name  # 通过init_flags记录初始化，可以只执行一次初始化
            Mediaplay.init_flags = True


if __name__ == '__main__':
    med1 = Mediaplay("Louis")
    print(med1)
    print(med1.name)
    med2 = Mediaplay("Merry")
    print(med2)
    print(med2.name)
