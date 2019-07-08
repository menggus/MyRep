from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基类"""
    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者类"""

    def __init__(self):
        self.__observer = []

    def add_observer(self, observer):
        self.__observer.append(observer)

    def rm_observer(self, observer):
        self.__observer.remove(observer)

    def notify(self, obj=0):
        for o in self.__observer:
            o.update(self, obj)