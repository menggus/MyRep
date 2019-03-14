# 使用装饰器，实现单例


def sigle_pattern(cls):
    a = []  # 记录第一创建对象

    def in_sigle_pattern(*args, **kwargs):
        if not a:  # 进行判断，是否进行创建过对象
            a.append(cls(*args, **kwargs))
            print(id(a))
        return a

    return in_sigle_pattern


@sigle_pattern
class Demo:

    def __init__(self):
        pass


if __name__ == '__main__':
    d1 = Demo()
    d2 = Demo()
    print(id(d1))
    print(id(d2))
