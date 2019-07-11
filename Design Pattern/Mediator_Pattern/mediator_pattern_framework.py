class InteractiveObject:
    """进行交互的对象"""
    pass


class InteractiveObjectImplA:
    """实现类A"""
    pass


class InteractiveObjectImplB:
    """实现类B"""
    pass


class Mediator:
    """中介类"""

    def __init__(self):
        self.__interactive_objA = InteractiveObjectImplA()
        self.__interactive_objB = InteractiveObjectImplB()

    def interactive(self):
        """交互操作"""
        # 通过 self.__interactive_objA 或者 self.__interactive_objB进行交互操作
        pass
