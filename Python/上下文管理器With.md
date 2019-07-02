## 上下文管理器  和 With语句



### with语句

```python
# 打开文件时,建议使用with语句,因为这样能确保文件在程序执行离开with语句时,文件能自动关闭
with open("file.txt", "w") as f:
    f.write(data)

# 另一种写法
f = open("file.txt", "w")
try:
    f.write(data)
finally:
    f.close()
# 对比上述,第二种写法过于冗余
# with可以让处理系统资源的代码更易读.而且绝对不会忘记清理和释放资源
# 因此, with语句还可以避免bug和资源的泄露

# 怎样可以自定义函数或类,且支持with语句呢?
# 只要实现了上下文管理器,就可以在自定义的函数和类使用with语句
```

### 实现上下文管理器的自定义类

```python
# 第一种实现上下文管理器来支持with语句
class Managerfile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):  # 必须方法
        self.file = open(self.name, "w")
        return self.file
    def __exit__(self, exc_type, exc_val,exc_tb):  # 必须方法,参数为4个
        if self.file:
            self.file.close()
# Managerfile 支持了上下文管理器, 并支持with语句
with Managerfile("file.txt") as f:
    f.write(data)
# 程序开始执行with语句时,python会调用__enter__获取资源,离开时会调用__exit__释放资源

# 第二中实现上下文管理器来支持with语句
# python标准库中的 contextlib 模块
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()
# 上述代码已实现上下文管理,可通过with语句来进行操作
with managed_file("file.txt") as f:
    f.write("hello world")
   
```

### 练习: 使用上下文管理器和with语句实现,文档首行缩进

```python
# 定义一个类,用于首行缩进, 实现上下文管理器
In [6]: class Indent: 
   ...:     def __init__(self): 
   ...:         self.indent = 0 
   ...:     def __enter__(self): 
   ...:         self.indent += 1 
   ...:         return self  # 返回with执行对象, 如下with中的ind对象
   ...:     def __exit__(self, a, b, c): 
   ...:         self.indent -= 1  # 进行资源的释放
   ...:     def printf(self, str): 
   ...:         print("    "*self.indent+ str) 

# 使用with
In [7]: with Indent() as ind: 
   ...:     ind.printf("asdasgfa") 
   ...:                                                                                                         
    asdasgfa
```



### 小结

- 上下文管理器是一种 协议 或者说 接口, 实现了\__enter__方法和\__exit__方法的类就是一种上下文管理器,且支持with语法
- 实现上下文管理器的方法:
  -  1.通过自定义类,并实现\__enter__ 和 \__exit__方法;
  -  2.通过标准库中的contextlib模块中的contextmanager装饰器实现
- with语句一般用来管理系统资源的安全获取和释放.资源首先有with获取,并在执行离开with语句时进行释放.



















