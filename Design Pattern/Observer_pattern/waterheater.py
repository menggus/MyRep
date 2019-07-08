from obs_pattern_framework import Observer, Observable
# 在pycharm中导入自己的模块是,会标记红色下划线, 原因为当前路径未添加到path中.

class WaterHeater(Observable):
    """热水器类"""
    def __init__(self):
        super().__init__()
        self.__temperature = 25  # 常温情况下水的温25℃

    def get_temperature(self):

        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print("当前温度为 {} ℃ ".format(self.__temperature))

        self.notify()


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 50 and observable.get_temperature() < 70:
            print("正合适洗澡......".format(observable.get_temperature()))


class DrinkMode(Observer):
    """饮用模式"""

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print("可以饮用......")


def main():
    waterheater = WaterHeater()
    washingmode = WashingMode()
    drinkmode = DrinkMode()
    # 添加观察者
    waterheater.add_observer(washingmode)
    waterheater.add_observer(drinkmode)

    print("当前水温{}℃".format(waterheater.get_temperature()))

    print("开始烧水......")

    waterheater.set_temperature(30)

    print("-"*100)
    waterheater.set_temperature(53)

    print("-"*100)
    waterheater.set_temperature(100)


if __name__ == '__main__':
    main()
















