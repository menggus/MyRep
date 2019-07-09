from abc import ABCMeta, abstractmethod


class ContextState(metaclass=ABCMeta):
    """状态模式上下文环境类, 状态管理类"""

    def __init__(self):
        self.__states = []  # 可能有多种状态
        self.__curstate = None  # 当前状态
        self.__stateinfo = 0  # 状态发生变化的依赖属性, 这里水的依赖属性为 温度

    def add_state(self, state):
        """
            add some state
        :param state: state object
        :return: None
        """
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        """
            change state of object
        :param state: target state
        :return: True or False
        """
        if state is None:
            return False
        if self.__curstate is None:
            print("状态初始化为: {}".format(state.get_name()))
        else:
            print("状态由 {} 转变为 {}".format(self.__curstate.get_name(), state.get_name()))
        self.__curstate = state
        self.add_state(state)
        return True

    def get_state(self):
        """
            get current state of object
        :return: current state
        """
        return self.__curstate

    def _set_stateinfo(self, stateinfo):
        """
            when the information of object is changed, the state of object should also be changed
        :param stateinfo: he information of object
        :return:
        """
        self.__stateinfo = stateinfo
        for state in self.__states:
            if state.is_match(stateinfo):
                self.change_state(state)

    def _get_stateinfo(self):

        return self.__stateinfo


class State:
    """State base class"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, stateinfo):
        """
            Whether the attributes of the state match
            状态的属性是否在当前范围内
        :param stateinfo: attributes
        :return:
        """
        return False

    @abstractmethod
    def behavior(self, context):

        pass









