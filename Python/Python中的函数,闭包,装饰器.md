## Python中的函数, 闭包, 装饰器

### 函数是对象吗?

- 函数也是python中的重要对象

  ```python
  # 定义函数
  In [1]: def add(a,b): 
     ...:     return a+b 
  
  In [2]: add                                                                     
  Out[2]: <function __main__.add(a, b)>
  
  In [3]: type(add)                                                               
  Out[3]: function
  
  In [4]: sum = add                                                               
  In [5]: sum(1,2)                                                                
  Out[5]: 3
  # 函数是对象, 与其他对象一样可以进行赋值操作
  In [8]: del add 
  In [6]: sum.__name__                                                            
  Out[6]: 'add'
  # 查看函数用于调试的表示符号,  为定义函数时的函数名, 但当前已无法调用add.
  
  ```

### 函数可以传递,且可以嵌套

```python
# 函数传递
In [13]: def a(text): 
    ...:     print(text) 
    ...:                                                                        

In [14]: def b(func): 
    ...:     res = func("hao are you!") 
    ...:     return  
    ...:      
In [15]: b(a)                                                                   
hao are you!
# 通过函数可传递特性, 可以抽象出函数的行为并传递出去, 而针对传递的不同的函数行为, 可获得不同结果. 

# 高阶函数: 能接受函数作为参数的函数, 例如:python中的map函数
In [17]: def a(text): 
    ...:     print(text) 
    ...:   
In [22]: res = list(map(a, ["你好", "你坏", "你帅"]))                           
你好
你坏
你帅

# 函数嵌套
In [26]: def speak(text): 
    ...:     def upper(): 
    ...:         print(text) 
    ...:     return upper 
    ...:                                                                        
In [27]: speak("hello world")                                                   
Out[27]: <function __main__.speak.<locals>.upper()>

In [28]: speak("hello world")()                                                 
hello world
# 函数可以接受函数作为参数, 也可以返回函数对象
# 需要理解为, 函数不但可以接受行为, 还可以返回行为.

```

### 闭包

- 我们在函数内部定义函数时, 内部函数使用了外部函数的变量, 外部函数返回内部函数的引用, 这样构成了闭包.

```python
# 什么是闭包
In [26]: def speak(text):  # 外部函数
    ...:     def upper():  # 内部函数
    ...:         print(text) # 内部函数使用了外部函数的变量
    ...:     return upper # 外部函数返回了内部函数的引用
    ...:  
# 这里还需要理解, 函数的作用域
In [30]: a = 1                                                                  
In [31]: def add(b): 
    ...:     print(a+b)  # 查看全局变量a
        
In [32]: add(2)                                                                 
3

In [33]: def add1(b): 
    ...:     a += 1  # 赋值操作,默认a为局部变量, 函数体中无a局部变量
    ...:     print(a+b) 
                                                                      
In [34]: add1(2)                                                                
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-34-b2710846a280> in <module>
----> 1 add1(2)

<ipython-input-33-02e1cdb3c7a5> in add1(b)
      1 def add1(b):
----> 2     a += 1  # 由于a为不可变类型, 当发生赋值操作, a的指向的对象已改变, add1函数默认在add1的作用域去寻找a, 但是add1并没有定义a
      3     print(a+b)
      4 

UnboundLocalError: local variable 'a' referenced before assignment
# 如果对变量有赋值操作，则证明这个变量是一个局部变量，并且它只会从局部变量中去读取数据。这样设计可以避免我们在不知道的情况下，获取到全局变量的值，从而导致一些错误数据的出现
```

### 闭包的使用  -- 装饰器

- 装饰器: 主要是用来修改函数的行为, 但不对函数进行本身的修改.  可理解为函数扩展功能
- 用途:
  - 日志
  - 访问控制权限
  - 衡量函数, 如执行时间
  - 限制请求速率
  - 缓存

```python
# 理解装饰器,首先需要知道的特性
# 1. 函数是对象, 可以传递给其他函数, 也可以从其他函数返回
# 2. 在函数内部也可以定义函数,  内部函数可以捕捉到外部函数的状态

# 定义简单装饰器, 输出大写字母
In [36]: def upper_wrap(func):  # 装饰器
    ...:     def wrapper(params): 
    ...:         params = params.upper() 
    ...:         res = func(params) 
    ...:     return wrapper 
    ...:                                                                        
In [37]: @upper_wrap 
    ...: def speak(params):  # 被装饰函数
    ...:     print(params) 
    ...:                                                                        
In [38]: speak("how are you!")                                                  
HOW ARE YOU!
# 这里采用简单的输出大写来解释装饰器,当然采用装饰器难免画蛇添足了,但这里只做解释用
# 通过装饰器, 修改了speak函数的行为, 输出均为大写字母的字符

# 利于调试的装饰器
# 查看speak函数对象, 发现speak的函数对象已换成了如下,相对原函数发生了改变
In [41]: speak                                                                  
Out[41]: <function __main__.upper_wrap.<locals>.wrapper(params)>
In [42]: speak.__name__                                                         
Out[42]: 'wrapper'

# 为装饰中的wrapper加上装饰器
In [40]: import functools
In [45]: def upper_wrap(func): 
    ...:     @functools.wraps(func) 
    ...:     def wrapper(params): 
    ...:         params = params.upper() 
    ...:         res = func(params) 
    ...:     return wrapper 
    ...:                                                                        
In [46]: @upper_wrap 
    ...: def speak(str1): 
    ...:     print(str1) 
    ...:    
        
In [47]: speak                                                                  
Out[47]: <function __main__.speak(str1)>

In [48]: speak.__name__                                                         
Out[48]: 'speak'
# speak函数在加上装饰器之后, 自身并没有发生改变, 保留了函数的元数据

```

- 小结:
  - 装饰器可自定义可重用的组件, 并可将其应用于其他的可调用对象修改器行为, 同时无需永久修改可调用对象本身
  - @语法调用装饰器的简写方式, 其原理就是把要装饰的函数的引用传入给装饰器函数, 在存在多装饰器时, 执行装饰顺序为  先装饰先执行(直观: 从下至上, 或者说从底部到顶部)
  - 为了调试函数, 需要在装饰器中使用functools.wraps(func) , 将被装饰的函数的元数据转移到装饰后的对象中
  - 装饰器功能虽然强大, 但是过度的使用会造成性能问题,  或者说可能会加大代码的维护难度.

