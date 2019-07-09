from State_Pattern.state_pattern_framework import ContextState, State
import functools
import time


class Water(ContextState):
    """water class"""

    def __init__(self):
        super().__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GaseousState("气态"))
        self.set_temperature(25)  # 依赖信息,即状态信息设置为25,

    def get_temperature(self):

        return self._get_stateinfo()

    def set_temperature(self, temperature):

        self._set_stateinfo(temperature)

    def rise_temperature(self, step):

        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):

        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    """single decorator"""
    instance = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class SolidState(State):
    """SolidState"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, stateinfo):

        return stateinfo < 0

    def behavior(self, context):

        print("当前状态: {}, 这是一种很好的武器......^-^".format(context.get_state().get_name()))


@singleton
class LiquidState(State):
    """SolidState"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, stateinfo):

        return 0 < stateinfo < 100

    def behavior(self, context):

        print("当前状态: {}, 滋润万物的责任就交给我把......^-^".format(context.get_state().get_name()))


@singleton
class GaseousState(State):
    """SolidState"""
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, stateinfo):

        return stateinfo >= 100

    def behavior(self, context):

        print("当前状态: {}, 看不到我,看不到我......^-^".format(context.get_state().get_name()))


if __name__ == '__main__':
    water = Water()
    water.behavior()

    water.set_temperature(-4)
    water.behavior()

    water.set_temperature(120)
    water.behavior()

    while True:
        water.reduce_temperature(10)
        water.behavior()
        time.sleep(2)
        if water.get_state().get_name() == "固态":
            break
