# 工厂模式：是在开发过程中用来创建对象的设计模式；
# 实现：
"""
  Person父类： 获取属性
  Male子类： 继承Person类，
  Female子类： 继承Person类
  Factory工厂类： 通过传入参数和工厂类来创建对象，创建时并不知道是由哪一个类来创建；

"""


class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):

    def __init__(self, name, gender):
        super().__init__(name, gender)


class Female(Person):
    def __int__(self, name, gender):
        super.__init__(name, gender)


class Factory:
    def getPerson(self, name, gender):
        if gender == "man":
            return Male(name, gender)
        if gender == "woman":
            return Female(name, gender)


if __name__ == '__main__':
    factory = Factory()
    object = factory.getPerson("luois", "man")
    print(type(object))
    print(object.getName(), object.getGender())





