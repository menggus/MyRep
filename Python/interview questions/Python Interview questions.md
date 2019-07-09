### **第一部分** **Python**基础篇（80题）

1. 为什么学习Python？

   ```python
   # Python之禅　了解一下
   import this
   
   # Python的优点很多，简单的可以总结为以下几点。
   1.简单和明确，做一件事只有一种方法。
   2.学习曲线低，跟其他很多语言相比，Python更容易上手。
   3.开放源代码，拥有强大的社区和生态圈。
   4.解释型语言，天生具有平台可移植性。
   5.支持两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
   6.可扩展性和可嵌入性，可以调用C/C++代码，也可以在C/C++中调用Python。
   7.代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。
   
   # Python的缺点主要集中在以下几点。
   1.执行效率稍低，因此计算密集型任务可以由C/C++编写。
   2.代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被淡化。
   3.在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。
   
   # Python的应用领域
   目前Python在Web应用开发、云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、图像识别和处理等一系列的职位。
   ```

2. 通过什么途径学习的Python？

    ```python
   # 自学(^_^)
   ```

   

3. Python和Java、php、C、C#、C++等其他语言的对比？

   ```python
   #　https://blog.csdn.net/qq_40925239/article/details/88793774
   ```

4. 简述解释型和编译型编程语言？

   ```python
   # 解释型语言
   执行过程中,先通过解释器把程序代码解释为机器语言,逐行读取,转换,然后再执行
   运行速度相对较慢
   跨平台性好(只需要平台上有专用的解释器即可)
   # 编译型语言
   程序编写好之后,会先经过编译成为机器语言,之后代码运行时,直接执行,效率高
   运行速度快
   跨平台性差
   ```

5. Python解释器种类以及特点？

   ```python
   # CPython
   C语言开发,使用最广
   # IPython
   基于CPython, 交互式增强, 功能与CPython一样
   # PyPy
   动态编译(注意不是解释),采用JIT技术(即时编译技术), 显著提高了Python代码的执行速度
   # Jython
   运行在Java平台,可把Python代码编译为java字节码执行
   # IronPython
   运行在.NET平台,把Python代码编译为.NET的字节码执行
   ```

6. 位和字节的关系？b、B、KB、MB、GB 	的关系？

   ```python
   # bit 位 最小单位,每一位 0 or 1 例如: 1110 0011
   # Byte 字节 1Byte=8bit
   # KB 1KB=1024B
   # MB 1MB=1024KB
   # GB 1GB=1024MB
   # TB 1TB=1024GB
   ```

7. 请至少列举5个__PEP8__规范（越多越好）

   ```python
   #　PEPE8 https://blog.csdn.net/ratsniper/article/details/78954852  
   ```

8. 通过代码实现如下转换：

   ```python
   # 二进制转换成十进制：v = “0b1111011”
   In [17]: int(0b1111011)                                                         
   Out[17]: 123
   # 十进制转换成二进制：v = 18
   In [18]: bin(18)                                                                
   Out[18]: '0b10010'
   # 八进制转换成十进制：v = “011”
   In [20]: int(0o11)                                                              
   Out[20]: 9
   # 十进制转换成八进制：v = 30
   In [21]: oct(30)                                                                
   Out[21]: '0o36'
   # 十六进制转换成十进制：v = “0x12”
   In [22]: int(0x12)                                                              
   Out[22]: 18
   # 十进制转换成十六进制：v = 87
   In [23]: hex(87)                                                                
   Out[23]: '0x57'
   ```

9. 请编写一个函数实现将IP地址转换成一个整数。

   如 10.3.9.12 转换规则为：
           10          00001010
            3            00000011 
           9            00001001
            12          00001100 
    再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

   ```python
   # 代码
   In [23]: def ip_trans(ip): 
       ...:     str = "" 
       ...:     for i in ip.split("."): 
       ...:         bin_i = bin(int(i)).split("b")[1]  # "0b1010"获取后面部分1010
       ...:         str += "0"*(8-len(bin_i)) + bin_i  # 组合 00001010
       ...:     str = "0b" + str # 不加0b也测试可以
       ...:     print(str, len(str)) 
       ...:     return int(str,2)  # 由2进制转为10进制 
       ...:                                                                        
   
   In [24]: ip_trans("10.2.3.11")                                                  
   0b00001010000000100000001100001011 34
   Out[24]: 167904011
   ```

10. python递归的最大层数？

    ```python
    # python 3.7 , ubuntu16.04, 测试
    def foo(n):
        print(n)
        n += 1
        foo(n)
    foo(1)
    # n = 2981时,抛出异常
    2981
    # RecursionError: maximum recursion depth exceeded while calling a Python object
    # 调用python对象时超过了最大递归深度
    
    # https://docs.python.org/2/library/sys.html#sys.setrecursionlimit
    import sys
    sys.setrecursionlimit(100000)  # 设置Python解释器堆栈的最大深度限制
    ```

    

11. 求结果：

     ```python
     # x and y: 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
     # x or y: 布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。 
     # not x: 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
     # 优先级 : not > and > or 
     
     # v1 = 1 or 3
     1
     # v2 = 1 and 3
     3
     # v3 = 0 and 2 and 1
     0
     # v4 = 0 and 2 or 1
     1
     # v5 = 0 and 2 or 1 or 4
     1
     # v6 = 0 or False and 1
     False
     ```

12. ascii、unicode、utf-8、gbk 	区别？

     ```python
     # 以上为字符集编码形式
     # ascii码: 美国制定了一套字符编码，对英文字符与二进制之间做了联系，这被称为ASCII码
     # unicode编码:世界上所有的符号都纳入其中，每一种符号都给予独一无二的编码，那么乱码问题就不会存在了。因此，产生了Unicode编码，这是一种所有符号的编码。
     # utf-8 一种变长编码，可以使用1-4个字节表示一个符号，根据不同的符号来变化字节长度; UTF8就是在互联网中使用最多的对Unicode的实现方式
     # gbk编码 采用双字节编码方案，剔出xx7F码位，共23940个码位，共收录汉字和图形符号21886个，GBK编码方案于1995年12月15日发布。它几乎完美支持汉字.
     ```

13. 字节码和机器码的区别？

     ```python
     # 机器码 是电脑CPU直接读取运行的机器指令，运行速度最快，但是非常晦涩难懂，也比较难编写，一般从业人员接触不到。
     # 字节码是一种中间状态（中间码）的二进制代码（文件）。需要直译器转译后才能成为机器码。
     ```

14. 三元运算规则以及应用场景？

     ```python
     # 如
     [x**2 for x in range(10) if x%2 ==0]
     # 一般用于对变量的快速筛选, 如上述对变量作了偶数筛选
     ```

     

15. 列举 Python2和Python3的区别？

     ```python
     # 详细区别 https://blog.csdn.net/pangzhaowen/article/details/80650478
     # 1.Python3 对 Unicode 字符的原生支持。
       Python2 中使用 ASCII 码作为默认编码方式导致 string 有两种类型 str 和 unicode，Python3 只
     支持 unicode 的 string
     # 2.Python3 采用的是绝对路径的方式进行 import
     Python2 中相对路径的 import 会导致标准库导入变得困难（想象一下，同一目录下有 file.py，如
     何同时导入这个文件和标准库 file）。Python3 中这一点将被修改，如果还需要导入同一目录的文件必
     须使用绝对路径，否则只能使用相关导入的方式来进行导入。
     # 3.Python2 中存在老式类和新式类的区别
     Python3 统一采用新式类,且默认。python2中新式类声明要求继承 object，必须用新式类应用多重继承。
     # 4. Python3 使用更加严格的缩进。
     Python2 的缩进机制中，1 个 tab 和 8 个 space 是等价的，所以在缩进中可以同时允许 tab 和 space 在代码中共存。这种等价机制会导致部分 IDE 使用存在问题。
     Python3 中 1 个 tab 只能找另外一个 tab 替代，因此 tab 和 space 共存会导致报错：TabError:
     inconsistent use of tabs and spaces in indentation.
     ```

16. 用一行代码实现数值交换：
     a = 1   b = 2

     ```python
     a = 1
     b = 2
     a, b = b, a
     ```

17. Python3和Python2中 __int__ 和 __long__的区别？

     ```python
     # int  long 区别
     # python2
     int 和 long为两种不同的整数
     long为大小不受限制, int有限制
     
     # python3
     只有int整数,没有long正数
     ```

18. xrange和range的区别？

     ```python
     # 1.均可生产等差数列,并且值相同,均支持for循环
     # 2.range是一次性生成所有的数值,且返回为list类型, 而xrange返回是一个生成器对象
     # 3.xrange每次迭代时才会生产一个值,这样会节省内存空间,性能要好于range
     ```

19. 文件操作时：xreadlines和readlines的区别？

     ```python
     # xreadlines返回的是一个生成器类型,每次迭代返回一行,python3中已移除 可使用python3 ,readline
     # readlines返回是一个列表类型,一次性返回多行,参数行数可指定
     ```

     

20. 列举布尔值为False的常见值？

     ```python
     # bool 为 False
     In [50]: bool("")                                                               
     Out[50]: False
         
     In [51]: bool(None)                                                             
     Out[51]: False
     
     In [52]: bool([])                                                               
     Out[52]: False
     
     In [53]: bool({})                                                               
     Out[53]: False
     
     In [54]: bool(())                                                               
     Out[54]: False
     
     In [55]: bool(0)                                                                
     Out[55]: False
     ```

21. 字符串、列表、元组、字典每个常用的5个方法？

     ```python
     # list
     append(): 尾部添加,时间复杂O(1)		insert(): 插入,时间复杂O(n)   extend(): 扩展
     remove(): 删除,删除第一个找到的      clear():清空				 pop(): 弹出
     sort():排序                       index():索引值               reserve(): 反序
     count(): 计数
     # string
     split(): 按需切分为列表             index():值索引              upper():大写     lower():小写
     replace(): 替换					join(): 加入                format():格式化字符串
     # tuple
     count(): 统计数量 				   index():值索引
     # dict
     clear(): 清空						get(): 通过key获取value      items(): 获取k-v
     keys():获取k列表				   values(): 获取值列表
     ```

22. lambda表达式格式以及应用场景？

     ```python
     # lambda x: x表达式
     # 快速定义函数, 可迭代对象的排序
     alist = [(1,a), (2,b), (3,c), (4,d)]
     sorted(alist, key = lambda x: x[1]) 
     ```

23. pass的作用?

     ```python
     # 占位符, 一般用于在搭建代码架构时占位,而不会影响程序的运行
     ```

24. *arg和**kwarg作用

     ```python
     # 传递变长参数,实际起到作用为*解包符号
     # *args: 用来传递位置参数,args为元组
     # **kwargs: 用来传递关键字参数, kwargs为字典
     # 以上一般在函数方法在不知道需要传递多少参数的情况下使用,然后通过* and **符号进行拆包
     ```

25. is和==的区别

     ```python
     # is 判断的是对象是否相同, 可理解为id(a) == id(b),内存地址是否相同,也就比较的是否是同一个对象
     # == 判断的是值是否相同, 可理解为内存中的内容是否一样.
     # python中由于对常用对象等存在优化,所以不会重新开辟新的内存空间来存储,而是默认指向同一对象,才会存在is比较时,返回True
     ```

26. 简述Python的深浅拷贝以及应用场景？

     ```python
     # https://docs.python.org/zh-cn/3/library/copy.html?highlight=copy%20copy#module-copy
     # 浅拷贝: 拷贝的是数据集合的最上一层结构
     # 深拷贝: 会进行递归拷贝,会拷贝数据的所有层
     # 对于字符串,数值, 深浅拷贝均是指向原对象, 也就是只是改变引用
     In [131]: a = 123231                                                            
     In [132]: b = copy.copy(a)                                                      
     In [133]: c = copy.deepcopy(a)                                                  
     In [134]: id(a),id(b),id(c)                                                    
     Out[134]: (139865009108784, 139865009108784, 139865009108784)
     In [135]: d = "how are you"                                                     
     In [136]: e = copy.copy(d)                                                      
     In [137]: f = copy.deepcopy(d)                                                  
     In [138]: id(d), id(e), id(f)                                                   
     Out[138]: (139865012479664, 139865012479664, 139865012479664)
     # 对于只有一层结构的字典,列表,浅拷贝与深拷贝一样;
     # 对于有多层结构的数据,如嵌套的字典,列表,浅拷贝与深拷贝不一样;
     # 应用场景：当某个变量包含有多层结构,且当该变量需要改变,且又需要保留原变量时,这时就需要深拷贝.另外开辟一个内存空间存储改变之后的变量
     ```

27. Python垃圾回收机制？

     ```python
     # https://www.cnblogs.com/pinganzi/p/6646742.html#_label0
     # https://sutune.me/2018/10/14/python-GC/
     # 引用计数
     对于对象的创建,赋值,拷贝等操作,会增加对象的引用计数,计数+1,而对应的删除,函数执行完成等操作会对变量进行引用计数-1,当引用计数为0时,该对象的内存空间将被立即释放;
     优点: 简单, 实时性
     缺点: 维护引用计数需要消耗资源, 且当存在循环引用时,计数不能至0
     # 标记清楚
     标记清除（Mark—Sweep）』算法是一种基于追踪回收（tracing GC）技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收.
     
     对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象（root object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。 mark-sweepg 在上图中，我们把小黑圈视为全局变量，也就是把它作为root object，从小黑圈出发，对象1可直达，那么它将被标记，对象2、3可间接到达也会被标记，而4和5不可达，那么1、2、3就是活动对象，4和5是非活动对象会被GC回收。
     
     标记清除算法作为Python的辅助垃圾收集技术主要处理的是一些容器对象，比如list、dict、tuple，instance等，因为对于字符串、数值对象是不可能造成循环引用问题。Python使用一个双向链表将这些容器对象组织起来。不过，这种简单粗暴的标记清除算法也有明显的缺点：清除非活动的对象前它必须顺序扫描整个堆内存，哪怕只剩下小部分活动对象也要扫描所有对象。
     # 分代回收
     分代回收是一种以空间换时间的操作方式，Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），他们对应的是3个链表，它们的垃圾收集频率与对象的存活时间的增大而减小。
     新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，老年代中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内。
     同时，分代回收是建立在标记清除技术基础之上。分代回收同样作为Python的辅助垃圾收集技术处理那些容器对象
     ```

28. Python的可变类型和不可变类型？

     ```python
     # 可变类型: list, dict
     # 不可变类型: 数值型,字符串等
     # 可变与不可变比较的是内存空间是否改变, 对于不可变类,进行更改操作,实际是重新开辟内存空间进行存储;
     # 而对于可变类型的操作,只是在原内存空间的更改
     
     # 注意:对于值较小不可变类型int，无论创建多少个不可变类型，只要值相同，都指向同个内存地址。同样情况的还有比较短的字符串。
     ```

29. 求结果：
           	 v = dict.fromkeys(['k1','k2'],[ ])  
               v[‘k1’].append(666)
           	 print(v) 
               v[‘k1’] = 777
           	 print(v)

     ```python
     # 这里的fromkeys方法中的[]对应字典value,会对应两个key,即{"k1":[], "k2":[]},且列表为同一个列表
     v = dict.fromkeys(['k1','k2'],[])  
     v["k1"].append(666)
     print(v)  # {"k1":[666], "k2":[666]}
     v["k1"] = 777
     print(v)  # {"k1":777, "k2":[666]}
     
     ```

30. 求结果：
     ![img](data:image/png;base64,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)

     ```python
     # http://www.sohu.com/a/221309678_467794
     # https://www.cnblogs.com/shiqi17/p/9608195.html
     def num():
         return [lambda x: i*x for i in range(4)] 
     print([m(2) for m in num()]) 
     [6, 6, 6, 6]
     
     # func = [lambda x: i*x for i in range(4)] 等价函数如下
     def func():
     	alist = []    
         for i in range(4):
             def lambda_(x):
                 return i*x
     		alist.append(lambda_)
         return alist
     # 闭包原理: 延时绑定,lambda x:i*x 为函数,在调用之前并不会执行,所以列表表达式执行时并未绑定i
     # 函数作用域, 函数内部查找不到,会向外查找
     [lambda x: i*x for i in range(4)] → 类似于[i*x, i*x, i*x, i*x]列表中的函数
     当m(2) 调用函数时,发现未知变量i, 由于在局部变量中查找不到,会往上层去查找,那时for循环早已经执行结束,i=3
     函数m会变为3*x,执行为6,所以结果全为6
     ```

     

31. 

32. 

33. 

34. 

35. 

36. 

37. 

38. 

39. 

40. 

41. 

42. 

43. 

44. 

45. 

46. 

47. 

48. 

49. 

50. 

51. 

52. 

53. 

54. 

55. 

56. 

57. 

58.  

59. 

60. 列举常见的内置函数？

61. 

62. filter、map、reduce的作用？

63. 

64. 一行代码实现9*9乘法表

65. 

66. 如何安装第三方模块？以及用过哪些第三方模块？

67. 

68. 至少列举8个常用模块都有那些？

69. 

70. re的match和search区别？

71. 

72. 什么是正则的贪婪匹配？

73. 

74. 求结果：  	a. 	[ i % 2 for i in range(10) ]  	b. ( i % 2 for i in range(10) )

75. 

76. 求结果：  	a. 	1 or 2  	b. 1 and 2  	c. 1 < (2==2)  	d. 1 < 2 == 2

77. 

78. def 	func(a,b=[]) 这种写法有什么坑？

79. 

80. 如何实现 “1,2,3” 	变成 [‘1’,’2’,’3’] 	?

81. 

82. 如何实现[‘1’,’2’,’3’]变成[1,2,3] 	?

83. 

84. 比较： a 	= [1,2,3] 和 b 	= [(1),(2),(3) ] 以及 b 	= [(1,),(2,),(3,) ] 的区别？

85. 

86. 如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] 	?

87. 

88. 一行代码实现删除列表中重复的值 	?

89. 

90. 如何在函数中设置一个全局变量 	?

91. 

92. logging模块的作用？以及应用场景？

93. 

94. 请用代码简答实现stack 	。

95. 

96. 常用字符串格式化哪几种？

97. 

98. 简述 生成器、迭代器、可迭代对象 	以及应用场景？

99. 

100. 用Python实现一个二分查找的函数。

101. 

102. 谈谈你对闭包的理解？

103. 

104. os和sys模块的作用？

105. 

106. 如何生成一个随机数？

107. 

108. 如何使用python删除一个文件？

109. 

110. 谈谈你对面向对象的理解？

111. 

112. Python面向对象中的继承有什么特点？

113. 

114. 面向对象深度优先和广度优先是什么？

115. 

116. 面向对象中super的作用？

117. 

118. 是否使用过functools中的函数？其作用是什么？

119. 

120. 列举面向对象中带爽下划线的特殊方法，如：__new__、__init__

121. 

122. 如何判断是函数还是方法？

123. 

124. 静态方法和类方法区别？

125. 

126. 列举面向对象中的特殊成员以及应用场景

127. 

128. 1、2、3、4、5 	能组成多少个互不相同且无重复的三位数

129. 

130. 什么是反射？以及应用场景？

131. 

132. metaclass作用？以及应用场景？

133. 

134. 用尽量多的方法实现单例模式。

135. 

136. 装饰器的写法以及应用场景。

137. 

138. 异常处理写法以及如何主动跑出异常（应用场景）

139. 

140. 什么是面向对象的mro

141. 

142. isinstance作用以及应用场景？

143. 

144. 写代码并实现：
      Given 	an array of integers, return indices of the two numbers such that 	they add up to a specific target.You may assume that each input 	would 
      have exactly one solution, and you may not use the 	same element twice.
      Example: 
        	  	  	  	  	Given nums = [2, 7, 11, 15], target = 9,
        	  	  	  	  	  Because 	nums[0] + nums[1] = 2 + 7 = 9, 
        	  	  	  	  	 return 	[0, 1]

145. 

146. json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？

147. 

148. json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？

149. 

150. 什么是断言？应用场景？

151. 

152. 有用过with 	statement吗？它的好处是什么？

153. 

154. 使用代码实现查看列举目录下的所有文件。

155. 

156. 简述 yield和yield 	from关键字。

 **第二部分 网络编程和并发（****34****题）**

1. 
2.  	简述 OSI 	七层协议。

3. 
4.  	什么是C/S和B/S架构？

5. 
6.  	简述 三次握手、四次挥手的流程。

7. 
8.  	什么是arp协议？

9. 
10.  	TCP和UDP的区别？

11. 
12.  	什么是局域网和广域网？

13. 
14.  	为何基于tcp协议的通信比基于udp协议的通信更可靠？

15. 
16.  	什么是socket？简述基于tcp协议的套接字通信流程。

17. 
18.  	什么是粘包？ socket 	中造成粘包的原因是什么？ 	哪些情况会发生粘包现象？

19. 
20.  	IO多路复用的作用？

21. 
22.  	什么是防火墙以及作用？

23. 
24.  	select、poll、epoll 	模型的区别？

25. 
26.  	简述 进程、线程、协程的区别 	以及应用场景？

27. 
28.  	GIL锁是什么鬼？

29. 
30.  	Python中如何使用线程池和进程池？

31. 
32.  	threading.local的作用？

33. 
34.  	进程之间如何进行通信？

35. 
36.  	什么是并发和并行？

37. 
38.  	进程锁和线程锁的作用？

39. 
40.  	解释什么是异步非阻塞？

41. 
42.  	路由器和交换机的区别？

43. 
44.  	什么是域名解析？

45. 
46.  	如何修改本地hosts文件？

47. 
48.  	生产者消费者模型应用场景及优势？

49. 
50.  	什么是cdn？

51. 
52.  	LVS是什么及作用？

53. 
54.  	Nginx是什么及作用？

55. 
56.  	keepalived是什么及作用?

57. 
58.  	haproxy是什么以及作用？

59. 
60.  	什么是负载均衡？

61. 
62.  	什么是rpc及应用场景？

63. 
64.  	简述 asynio模块的作用和应用场景。

65. 
66.  	简述 gevent模块的作用和应用场景。

67. 
68.  	twisted框架的使用和应用？

 **第三部分 数据库和缓存（****46****题）**

1. 
2.  	列举常见的关系型数据库和非关系型都有那些？

3. 
4.  	MySQL常见数据库引擎及比较？

5. 
6.  	简述数据三大范式？

7. 
8.  	什么是事务？MySQL如何支持事务？

9. 
10.  	简述数据库设计中一对多和多对多的应用场景？

11. 
12.  	如何基于数据库实现商城商品计数器？

13. 
14.  	常见SQL（必备）
     详见武沛齐博客：https://www.cnblogs.com/wupeiqi/articles/5729934.html

15. 
16.  	简述触发器、函数、视图、存储过程？

17. 
18.  	MySQL索引种类

19. 
20.  	索引在什么情况下遵循最左前缀的规则？

21. 
22.  	主键和外键的区别？

23. 
24.  	MySQL常见的函数？

25. 
26.  	列举 创建索引但是无法命中索引的8种情况。

27. 
28.  	如何开启慢日志查询？

29. 
30.  	数据库导入导出命令（结构+数据）？

31. 
32.  	数据库优化方案？

33. 
34.  	char和varchar的区别？

35. 
36.  	简述MySQL的执行计划？

37. 
38.  	在对name做了唯一索引前提下，简述以下区别：  
       	      select * from tb where name = ‘Oldboy-Wupeiqi’ 	  
       	  	  	  	select * from tb where name = ‘Oldboy-Wupeiqi’ 	limit 1

39. 
40.  	1000w条数据，使用limit 	offset 分页时，为什么越往后翻越慢？如何解决？

41. 
42.  	什么是索引合并？

43. 
44.  	什么是覆盖索引？

45. 
46.  	简述数据库读写分离？

47. 
48.  	简述数据库分库分表？（水平、垂直）

49. 
50.  	redis和memcached比较？

51. 
52.  	redis中数据库默认是多少个db 	及作用？

53. 
54.  	python操作redis的模块？

55. 
56.  	如果redis中的某个列表中的数据量非常大，如果实现循环显示每一个值？

57. 
58.  	redis如何实现主从复制？以及数据同步机制？

59. 
60.  	redis中的sentinel的作用？

61. 
62.  	如何实现redis集群？

63. 
64.  	redis中默认有多少个哈希槽？

65. 
66.  	简述redis的有哪几种持久化策略及比较？

67. 
68.  	列举redis支持的过期策略。

69. 
70.  	MySQL 	里有 2000w 	数据，redis 	中只存 20w 	的数据，如何保证 	redis 	中都是热点数据？ 

71. 
72.  	写代码，基于redis的列表实现 	先进先出、后进先出队列、优先级队列。

73. 
74.  	如何基于redis实现消息队列？

75. 
76.  	如何基于redis实现发布和订阅？以及发布订阅和消息队列的区别？

77. 
78.  	什么是codis及作用？

79. 
80.  	什么是twemproxy及作用？

81. 
82.  	写代码实现redis事务操作。

83. 
84.  	redis中的watch的命令的作用？

85. 
86.  	基于redis如何实现商城商品数量计数器？

87. 
88.  	简述redis分布式锁和redlock的实现机制。

89. 
90.  	什么是一致性哈希？Python中是否有相应模块？

91. 
92.  	如何高效的找到redis中所有以oldboy开头的key？

 **第四部分 前端、框架和其他（****155****题）**

1. 

2.  	谈谈你对http协议的认识。

3. 

4.  	谈谈你对websocket协议的认识。

5. 

6.  	什么是magic 	string ？

7. 

8.  	如何创建响应式布局？

9. 

10.  	你曾经使用过哪些前端框架？

11. 

12.  	什么是ajax请求？并使用jQuery和XMLHttpRequest对象实现一个ajax请求。

13. 

14.  	如何在前端实现轮训？

15. 

16.  	如何在前端实现长轮训？

17. 

18.  	vuex的作用？

19. 

20.  	vue中的路由的拦截器的作用？

21. 

22.  	axios的作用？

23. 

24.  	列举vue的常见指令。

25. 

26.  	简述jsonp及实现原理？

27. 

28.  	是什么cors 	？

29. 

30.  	列举Http请求中常见的请求方式？

31. 

32.  	列举Http请求中的状态码？

33. 

34.  	列举Http请求中常见的请求头？

35. 

36.  	看图写结果：
     ![img](data:image/png;base64,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) 

37. 

38.  	看图写结果：
     ![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAACjCAYAAACT4RIjAABT2ElEQVR4nO1dBWAcxfr/7Z7H3ZomTdOmTt1LqULRllKgyB+KFrfCo7g87OE8tLyHPpyixeruksaaNO6eXO4u53e7/2/mLqmlOL2S7q+E5PZ2Z2dn5zefzMz3qTMGpG2DLIyFAgUKjilkQd6hDnQlFCg4kaEQUIGCAOK4IKAHEmT6rYH4q85n5wq/oXxBZuL+99Ts94Pd0+XxQhREqNSH3lym74Q/oT6/VI7XK0MUhc5zZK8Ej0QvXSP+pvY71pAlGR6qqFqj+lXtdLR28FIZVBQ0ml/XrwKBgBOQkamnHErk86BScOCXqMWoyn7Uv5Ks8NJ/dBPxGD4p6xAqlYi0nmHw2Jyoa3FQB/E9F+9cVKE/2il85fg76VG+1/qJ5qG/ZapUWFQIooNF1NS3wyX9tkHsWIHVMyhEh8RoHWpq2uGgtvpZEna0g1rsbGNfOUBij1AEa4DK6nZ4ZOFPGfT+bPymbskah7029iAy/+eDwP/5zwE6vzn8OI74TgZ1TSyUhyMZbVgo7CUaHqjS4eU46fM4uQeGEvneFarok/CznUjyACnjVEjpCWz/2ksSgQ6KR46Y7HMHHaTO/9E5qgPnMIkmSbwyEH6BOxKdKAQH4fqbx6E9txiPvVNEUlDFR+S+QxIxdXgYPlpajHa7REQVOusgSb7nFVW+55L9jdYpwfyfJepwaf3jMXNMJD5ZWgizTT5EynpcXvQelIRbLuuLT97bi637zPyRRp6cjmsnh+DWh7ai0coeWuDvlD2XyC4Xf/6+/L0ffL4gHHJOZ/1F4bD2PXCNIAqHlkl/8AHSf43XLaHP8BT88+o03HHHWhQ0uvhAwt/ZYedKdG5Uz0jMm5mEn34oRkWDi7cDnQ2bW8S8i4dhVLwHN967FS43u7/sr/Pxw8RfJiC1nNvj5g0QGhEBleSFxeFAOPRIgA52wY1Gooab04W9ZhV6IhhBdH6NYIeVjrHXaqBm8dLfEXIQQuD7jviBaJJ9PwklUIt2uoevZxv8dIiR6S/Bgwr4JGMInTsMiTiTqr0MDXBRg1plDxNyRxCRtbEuWECPoWoMHSogZ50EFxXjcZP01Aj0t69TsPO0OoG/XFZTxofgGGoY+q6lVvaprnQDUQ/EJQvwUBltdTTqUjt4Pa7OjtTZoGqNn7kC9DoV3FqBE5rJIp1BjYyBcThjZjxWrKYBRKS6E1kc9KPWqtGzZzBV0IOaWhskqlhosBZOhwsOqjPrt4YgDe9cHg9J137ROH1mMlauqYKX3oHH7YWbCCBShTx01uln9kF6nArlVJZaq0Iw3btqfx2W1Alod6KzI4aE6hEbpYGt3YXGZge/b3CQGi4nlef1Dac6ul5FFXCQ2Aym8+PofJfdg9oGm29QYm+dJHFyQhC9IRlNTXbYnBLXVDweGZGRQYiP0aDN6ILR5OQkYmWyxlPR73iSdsYWO9qsXoSEaGGsacWr79jRRIOEhl6IhqQbe349ScboEBWXjDZqEx21b1JKJM46vTfysurQ3E7vkEZZl8c3dGuoTYP1/s4higgPC4G5zQgntZWaBkSVOuAK4M8QkDqYw+mghjUguVdfTJw8DeedOwsfvfos8leW4HH1cESQKGAd4h05F++JNUQQA26Rh+FURHLVoEJsxv1CFlrotTwmjUaoICGeCEg0xntCJr4S2vGgNBx9ZD02S6XYKrTwhruOjk2i0tT0L4xI+b6Qh69hwsPSMAwQwxAhCVgiTEQdjHhQzEYTvWr1QRQkTsLQQ8RZt+jQo7cIg0HGpU/oYSz3Ys3nHky/QYeS71zY8qMX+hgBcx7Uo+IHGj3TiKxjSKXTMDVIROZXTqz50ANDsohZN2jRM03gRMr+3olt30WiV0oPrkrKfhaK1HnbWhpRWl7ja0LqnV5qBy9JLEae224ZiaH9IxEWqsbD90yAudWCV17LRJU7CLddNxTDM0KJQMDGtSVY8nkZLr92OA03djzy7B4kDUrG3df2w4pl+5E8OBnjR8RRh1LjwcXjYTHZ8Opru7G/xsXvGd8zCtPHROHr/+1GdZMTMekxuHPhSUiN06NyXy2ys5rRavPglNP64NoL+0BLN1VTD9+6rhTvfF2Ff9w9DuV7yvDmZ+VQUQ+++fZRsJTVYlu1jJsv7QeditmWKmRuKcMr7xVANgTh5huGY3T/UBqYBNSWNuCR57LQRoPc5Jl9cDXdw6BihriEt17fg282N2H2/JNw2ohwUKsjJSkI5bl1ePiZTMz9vyGYOjIOxro25GXWo8HkxfDxPXH9xRkgziCcSJiXWYXn/7MPM+YMwjlTk2lw0eC6a0fCYXfi7bf2Ykuu2dcP/OqpQH1Z1sTg7kefgcZUimU/fo89WbloMZpIA9ESUTV/HcN+AV0SkHUonSEM46fMwllnnYlRwwbDZmzAutXfY2deEa5QDaEX0I4bxByEEKFUYEOqiHOlgTiPyPeYuAeFajeGSuFcqjB7LQ1RiIUFDxLxrAKjlhM22Y6XsQ+LMRIDJOp8Kp8USib5Gk+/7xB3or/cGzfIQ7BX2IiniWzz0B+n0Mt/DAWwkdxtJ8oebgXR13C1SlizxIkhszUYmCHix9ecsFuBpmoJVpJiI89QY8dyDxJOIqk0QI1t9P2ASSJi4wR8dL8DIXT8zEv0KMq0Ysh8HXolAl884UBoigqnX8VG5uGYN+16xMdqOMHYMGvQabD2m0/w5L//Q5LSgfffyYTb1A6NTg2P04MP/peL8hnpmDc5Bm+8TQNTqxNVbRIW3j4cY/to8exLOyCGRmDxLUPQUG3C0q+K8cKj43DnDRJ6DEyCtaoeKzc3Ijy/HdXNTlwyIwFvUjnNJhcajG6umrlpwJpxWjrQbMQP6+uh0avhaG3Hf9/KwvRTB+DMkyKow/mcM63N7Xj//RzU1rUjY1QKbrqwPzbtqkdFkwenn5qCj78sQ2z/OJwyKhZL1u4nCSbggw9yuARKzIjDPdcNwvqtNTAGkTSeGIsnH9uE3Fo3+qUGkdT2omefOCy+aQi2/FSAD7+vQXq/KFKXvVzriI4JxsihsXiP6v/am63omWjgisOP3xXCahFw1ex4BJH2wBxJQSQVB9O1rz23BZnNAp64bzQuKDfh02WFaG5x4uZL0vH553koqLCjmaSvSPa3ngaVH77OwzadBKdMw7PbhC+XfoILzpuLBx57Fu3NdVi58iesWr0axeV1pOkERi3tkoAeUpjHnnoeXvnXYurIJXjttWfw9Q+rUNdoZHoQ6tU2pMhxuMrbFzuEBqwQWknGqTFBjsFasQxfkWySqCPkC0YwZSyIVFWBxNIyVTGWyfWckDpOGwmZYgtqvE6kCgd0OZFGyiyxEatIzSwW1bjS0wOpdIflqkaMkRykdqqwi6Srh6l1R9DP5/Ek7RDV+yQkjpXh7OFFeTap0n7HQw4Rb+AdWiT0UqH/JA1aCzyoKpYwhAaAqmwP8nd5YagFppyrQtpIFUlRgdt9Ey/WQiT1VR+qgs26E/f+Yz81h9ip/7JfVguNqjo9V4Uyd9dzm4fZJcxuKyxoQXL/RLioffPyW1BHJIpODMOQvmHQar2YPbsfdUI1l6rpfSPx329y8OK7BXjm3pFoIMl1yxt5MJGa1tzaiuj0ODipnFwqp8HoQUgwe5Wk7sWG4ZzpCVjxaTZqSeVTE/ndRP78/FakDLbCMyjM18bU3kYaAKZOSMfsMwykh6tJ21EjmqTJuo1VmD1pKAb0CUXv4XHwtpmwJasVcmQI0k/pibNnBUMi1VBNzxVLKmlVkw3tbgFnz85AUmYT1m6q5kQb1zcKIo16731chNJmN2kG1DZqkf8wlbIkvxHvf1qIRruMfQUif+7GsjbkpFjI7IntVO9FUh9rK5rxw8YaVFIXzC0egMEZ4XjxPWr/0ijuMS0qbUPmPgtvB25n0n/79zVyo0hD6rGK1PSNy7/C1jU/IH3gUCy4+nrcetejmDlpNBZccztMzNnzZzLrV6JLAjIPXkX+biz9+htMGDUY5174f0hI6oXlq9Ygv7gYH7qzSfL0wkQhFovksRhBUuyfZMcx+8lGNptvSoFGr0PcJDLMRCw9kU8Dlf8I3Uv2qXVMayeLil/D4KZzmQufW5bUWUQ/2XT+8ny0O7o3hA1oGh1rfJ/jSKXy+VaYdKzK9KC+UY2x55PdNZjsw8+ccJC6xEZgj93ndRO8TAv3kYddW7nbg6zNXqj0AjZ/YkVw8CTcdd+liCSbxCv57qGnzr515fdY8t5n7MZkex1aP2az6LSCrz70lZr+x2wrDd0jP6cBX6+ph57K/5rUzPp6K/1NbeUfmflVasFvs6qg52X76saIwE5wk412yvTepGt4sHwLI79/cBJ89qiuw/PKPMP0sFddORQje6rx7kcFcIeGoHdaBEKIgPt3NKCk3oUzTu2FqIwY7N1egVqzhPvvGIbxvXV458N8tIta9OlD6jR1+NL1NXjgyR2YNiER02Zl4JxZPXHTnet5nbwkCZ1uv9eX1GOpw5NFcNLA4KE2DgpSdTp/mF2q9juUmGbh5V5QkcrxcNuRnckIxyS4luxHnU7kbSL62/Fg7w+zSzv8aDL1s6SU3hg/YTJOmTaVJGov7NyyCsu/+wl274E6HWt0SUCRjNO68r145L69SExJw4TxEzFz5iwsmT+fRuPFyFm5D9u1FfgGZbhbmIDRZNVpqHvvEtpwpZRKErEB+dQJhgoRyBOaYZd9nfrQ7iiTxahBuKxFMH2jpaokyQa0CjKXbEOFOAyQQzBISiA7UEa1ysGvIvsaPUhFHSyHooZUUAtzQOAozcfMDhqZIxNUSEwX0doiwW4BqWQyMld6MfdGLdrLvMje6IXIiEFSO2mggMRUAWGDVAgNFVGV40HkEA2i40XU5LpoYJARS3albGvC7u3bEEwS0O/844Z9SVklFSN0WSEmmanPISoiCP3SwohQVlhsLhRV2zAgzoDK0mbunczIiILTRqrcyBQsuro/vnh3L3oMTcX9tw3F4sf3oIWkIHNuRIQbMICVU03qvNkOQ3w45p3WA+tXF6C0wcEdO102Cz2DSHZPQkIwivMq8f3qapwzfxgiQkh60KBgNbZj3bZ6rpK62m14dEktBCqLnV+yvwbfra7ChKl9ERWugZsIFN8jDB6TFS+9uhsjJqbh2bvI3ozRorjUBF0EmSWzkvHhTzVI7RMLUD13F5l9g5x4MF+IpNR+4bFBiCEbmRExKsqAGIvMyReXEo2xg6KRWS+hX+8Q7FpWyu1NyQ3oDVoM6hOO2lYPnA4v7DQQHaxRCjSYQxeN+x//N4alGrBh/So8+r/XkUV2oNnmhFavCxD9fsYJI6o1ZOfIqKssweflxfjhu68xbMRwtNRU4nSxH+bKkTASAWJIpr0vFJF15yVCFmIy0fFpaRJ954VbsGIRqZhWalwr/yx1zkdQu+EMuS+uk3sgVNZBLeixhMr8kqjroG8T6O+XMYlG82CsIum6hyw+PfXgPWIdrFISnpMnoQJNuFfYS4rqoU6YzmcQmLTzwna2Ghc9oUf9fi++etaJFiJhyU4PHC4tKvd60NIELknYyGqIEXHB4wYE0++SzW6U7JFgkpyYt0iHa14L4mqslqTq5/cW4p3/5EKtZw/EhhbJN53B2u0o3jWmSpXk1aOgrifuWTwBdVVteOGlnXj73Tw8ctcwvPTcNOoQEkL0wFtv52Li6f1RRarn6+/lIW6IGS+SKnrBWT3x+iclKM5vwP7aXrj7HxPQUGfGU89sQ8YpqUgMkfDUymr+QAemCGTu0WTzgR2S1NvuwsbNNbhiTm/8r38CkVUHR7sTbnpALX2/fUstFpzfB7X7m1BQSpY2Hd+4pQZXndsL/3sjjhPYQWXY7C7Ep0TgkTuHwWJ0wED2WtbOahTWuNDsasIH31figotOwoTp6QiL1OODJbuwo6CN1HBGlgPvjEnv+PQY3Ev2byydpyLC337XBFJTG7B9vxkOScQ1N4ziktvR0Iqlq2u5et1Q2YzteW24dMEInH2OFW8s2Y1N2ZZDpmWYfSfSO/zsvVfw74oClFVWkYrLvKRa6Ih8gcTP+mHZKKTV+SrocdmxfdNGenkqfKRtQ5YUhjiSXuVk52UK7dxj2SqYcBM2Y4wQTTJRQBZaUc2d4jLuFjcThZx0lsp/YwFbxAqUyHVETN9EgoYkEMlL3E1XbEIpPhKboKXRaytJUTdT8eh4KRpxpbieiKmFh9Rds4wurEAfRA3QUujF+7fZERxBnc5J0s9O96ZHCo+mWtHnnLUeJvh4CYyEpUS6LSsk0LtF8W4vd8s3EInfXeRA76Fku1BHbiiT0VIrwhB25Mv7uTkmNufXVN2GBx7chIRoHalXXjSYiOC19bjznk0YPigSBrWM0jITapucKKjaBWOLDQ5Bjeq8OlLr1kHN1HiqnLnRggcf3oT4aD281JmbXGosHB+PrevKUFhp5xP0ne1AI5GO1NmEBAN1fC/90Hulr7/+LBeFuQ3oGatBPiMFvYZ2swP6IOrY1S248eYVcJEkNjGvMtm+3y7NQ1FuPVLjdSgtNcPikNBucsDmNeGBx7YjNTkYDosDe7Kb+Hd0Cd7/7x7s3ByDPslBqK+xYF9xG0Kp/G8/zcNKjQSX6FsswCbSjQ0mvPByJrdPmeqpIWlsoUFh4OhktJQ1YMkHRdwhszerkdvPTK11We147pmtSIgNhkakd9Ng4/Ooh70VSB4bNm9cywdBUa2HXnN8zAX+6okQgSreYdO0yTasJdIxlYp1/o4lZMyaswkOrEAV/8yOi9zVItERC6kCB6bm2f+NVE4zyUYcNJfGrD0d2S5u+vcTKZkaweewETuvE4iCNtTTdcxlL+AXllVR1SxNZH82+if16fOMWwwYd5qA0jUuFObJnHjMDGCEhZ3ssTVeCBofUbmaRD+2RglZP/omvZgdya75PRO6zEFgITXM1Gbzl0V2HrWrpdWK1Wss/BgjKutEFouLk6djsr621gKf3eezBRlZzG12rgIb9Cr897WdMDbbIKt8QxKb22Qj/QUXD8aZU5KQGK8nKbAXRlLTROrwzDG0N7MOmZLP7merDXyT3AJ34VdVmrmOyO/PjtP52VkNNPj66gi/7cWQm9eInByfSslX57BJfvYs9P+8nEbkZsn8GF+xQr+N9LwtMjqfjR1zOknjKDUe0l4OJ6mcY0Q+H5hLdnI9DVjMlmaOHN91IlfXS8uMne15tNei0QRuuuFo+F0zkYLfIfJbvhO7cJgIfIrisHWS9PO2kMPXyITwb7tQLX+ZdofeR3XAJGNqYukON1r2+dRQt9v3PetHuz50Q0u2lS6Ym4NHlKE+6LEOm3//TeCeUVE44hhzrhyMw9eQcpJ0UQ67iq2y2V/Y5vMydqyuEXxOmvzsBrjIRmtrsWJnVjOflO5wzmg0B9/zsPupD7Pajzj/AI52nGs2XUgbwV/vQ44JwhHPHER1zd9di+drWuCUVGTvdeF466I9/y44KgFl7jg59g/F7piJRv/84Z9/f/ZIZds8fnvtwHIzdrwux+eDPZbrRv8syMKRBGZg0js3rwnZJD0gdEigAFTwd4LVtanegjpSX1Wan196+HfE0SfiyUBlNorH6z3mRBS7lJd/YvlH0UQE9fG5QPmPgk+lHEVj+VuAqa5/o0Hjt6BLAgpc1dD4FhUfRwtXFSjobvgbKlsKFHQfKARUoCCAUAioQEEAoRBQgYIAQiGgAgUBhEJABQoCCIWAChQEEAoBFSgIIBQCKlAQQCgE/DtDkuByu/m+to4VSyyciG/R9JGvVpbpfKeTr4PV6fSdIQIVBA5HXQvaEenrWCzKZjuWZepIEg9DoWY7Xv/cG/iX1B0eeKfjvlDR/VSBX2woe32xR1W/4vEZmVQaHTLSeqGxvg5WB9vizMIupAJOMxpazHyrzsHns0hmA4eMRHx0MPZl74Wx3aWQMMAIuARkJBB1IYg543xEnzQIrrpCVHz6Fo/b+XO8Z3vduopkdehxX6wWdWQcBMkJj9l84DvJQ8d7oucFl8G48WsYc3J5HJeO63zh7H+p/F/7jIeGxu8qlLqX+JM2QYV+fUSs/8zNQ1ccHjz44PANLNDSxFmX4I5LTsEdty2C1e7kO/qnz7kCpw4Jx4233gmLU+rcwsT2/s264Brcd8NlKM3fjSceL0KL2fm33cbTXRBYAlKvc7dbEXfBQvS5+Dw0rf0e9poaeB0uyNTBRJ0BrLNJLgcEtdYXOZlF12V7Jfyju6DR8qA9rCyJhT9W+YL/iHRcpnMlTQj63/YUnLnLUPjf96AJC+W7ab12K9RxQQhO7Q3zVveBOrmd/sBB4EGhoNXxuJIH35fdWdZou9QMGNncDp56yh9J2r/3TcUfBW63bwMwk3YsNASTdjyPhJ34HyoiNtW38t/JnxU8mrfAyhL9++U0Pq1EGxqDuRfORd7Ob1DZ0MojUKlEL9atWYMr5z+FySMH4pv1WXQvHR80RFGHSSdPRsGOn3DbfU/B5pKO2O+n4NgjYARknVqTkIboviehx/TT4GmtgSl/L8wFOUSMNESl9IAxayeppWpEDptAkrEITpuMqIz+kNU6BPXqBUdJNlp37+QRqlXBEYiZPAXByT3gaq1F644NUEWnIrzPEET0HQCbtQjJZ8+DpTAL9uZWOvcc6sTBaPjufRgLyokMaiKFB5qkvogeNQnqIDXas7eirWAfxJA4RFKHhkqLYHbfqgK07tzKczwcQkKW+MQgoPcYEREJAkjowkWSLCRIQO46N7w6ESeNEEECGbYWoHiXF8YGmZNq0AwVQtQy9qyQ+CZhVlbCABFh4QJ0EQJi4gUUbfWgpljmseP69BuGEb1j8NDzm+AkkuoYkUU1aksysbuwHtOmTMGPm3P4AMDjW8sqIrYWbW0tsNkd1Ibabrn16u+GgBGQ2SSa2J5ImD4b4b2T4SxvQ/SUOaQmtkE38GykTu+PXTddDCEyHRm3P47K126BVeyDIQ89CWvuJrgQioi5FyPr7kvQ1uBCv8XPITI5CqbC/dBPnEEipA0ubQoSZp4JnV6GLSQJMZOi4Woqg73FhNChJyN5yix4anYQmTZC9nhh6D0KA+97GkJ7FVxSENLmXIi9d/0fvDHDMPixl2Et2AGXU0TU/AXIvf8KNGflUc83dD6Th4gTTMSbvVgPt5HKixVhb5ShjxIQrJNR5xUwYTqLOOdF/ylqjJkl4ZOHnGg1k/o5So2Bo1WQWyVUZntha5cx6GwNpp2lRsVeCVoqY9Q0Fd6/24mqKi+GDBsKydKCwoo6iCr/Xj+RSdJ2bM/Mx9XjBiE+WIcGO4sZRwOFVougYD1spIoe60xRCo6OwKmgNOxb965BYasRI59+DVUfPIuaHTkkiTToe+4iUkVL4bLYETKoL9RqCe3VdQibch48TfuR+8St8AYNwPCnnyOJE4yksxcgOqMHsu+5HG2FZdBGJpBkIjuqZSVJNTUyLpiJ4hf+AWurnYfdE8j+q3zrKYSkD4LYXAOP3U4SIRxJF94Ajbsaux+4hlTXXhj1+v8Q2qcPXGGDAFMlCp+5nWytGIx+5b/QhYXwQaSrvuy1y1j3Bg0K8/SoX+NG0EkqJKSL2PiSE6Z9XuhDBTQ1AVPmqhGfJqB+q4SfXiAiXqzF5GkHAv0yophqJHx+j50GJRWufFiPOFJRy0pJwoZHw2FvI1XS4VOVOQR6NgmtVbUIOTsDQWF6uExmzJ5/Kc47dzaG9A7Hw69uIcmNztibCgKLgNqALF+dPj4FKtmO9oZmbueodNEIiaPOtWsV2XRehKT0ZoE8qSPZiQy90Z67BbbqWoRNnQm1xwqHRULiqDEwbfsB5qISGumD4bUaud4lkv0TmtYHzuZaOC1Of0ofXxYfVVg0DNFRaNuZx9JgQNMjBZED+6Dxu5fgaDZDnyT4PKReEcHpvWEp2AlzWSUMI4ZRo7lhbSQd8ij79pkJyQL8emwSrFZA76aySAqnTdLitMs1ZPeSpJJ8AWdZYhgOf5xhZhsegABzrRdmOj+4TeYquI+cLFami55PS2olk34H2bCkEutCgun+TnidvnD1JmMraqprkJESBz1JQaHrsKUKAoDA2YAsGxHZJEEp/eFuqYGzqdlXofgkGMKD0FiUDxZHO2L4ODhriuGWQhGcGA/Tyi/gdQkITR0Ej6WOpCTZksHBsNZVkORx8xDkIHWLsUrWh8GQmgHb/q/pPAtUhiBuD0lOB7TR8dAGCzDmF0AmQ00dZOBR35xN9VS+CyHDx5Jd5YSl2YpeyT1hy1lKx2W670DI9mYidSMR4OjzBdwB4w8+ywgvkm04aZ4a1dvc+OJFN5Inq3HZfb4Q7SxSNZNKzOHCIneysPqS3wsquX0R0ISDpKJKJaOoohyh4ZMRHxaGhrZGnv6MTxmRbTeQBpKaiiq00KDDknFuWPEN1ixfhdf/txQnnzwGX6/eGrCYPwoORQAlIIvObEBwRj+4WsrJtvKN4jysXFAYokfPgDr9NCROHIX6j1dAF5dMEisEdVVlRDA9QgYPgbe5iK6tJjurCTEzLkSPRgd0PQZAdNWh/ON3ILLwdUTOoP7jkXK+B+asrXA6NIgeORLBfYZDF2xA9JgZdL8omEsbSDK5ETfjXHiC0pF6yXUwbv4YLocKIT3jUf1DKQ8mEzpoKFzGerjNNhZs5Yin4mH5dD7Pp0Yr+EIYalkwJJknh4ntJWLINDVGztMiPFzgTpKIFAH9J6iQNpwGljgBY+ZpULvfw9I10KDgJwkRWaP3OX9Fum/B3m1ocF2FkcMHYG95ne/epBKHRCRhzPB+2PLhMzA5iIA6NrDooZJUcDptUHk9PIuQOkgD9RHxMxUcawSMgDwaP6lQrspiNDZs5ceYM8FRU4Tq779G/KhRkKrL0LDiCzTv2kXiQY+WjaRmlpaRmhoMZ2km6mt3kcrWjvL3XoR42TVIvuBqSNY21H25lccXhcOM2i/fRo8Z0xE1ehIcFftIdYsi0k3h2Qqbd26HvvcwhJPIadmxHaXvv4Je512M5DNTYd76FX3+D4TwQTBuW0W2ZSHU+mC4a/LRVFDIUz1DdWiULkYOr0NG4SYvTK3gzhRjPamORR6e4bCs0osZl2sx5TIBdSVe7FxG9loDSdVEFfqP10D2yCgpkNB7lBpqQUZjnheuEJmHSPSQGpq/gcptkXkI/GaykX9avQNnz5mDZWu3E9m8PDTh1Olno4fejhVrt0ESfHHl2A9ZxKhpaMDssVMx/4IybNi4GS1muzIRH2AETgXlupkN1Z886zug0vimzV0WVLz1GGo+Ybac2aeXqTVcXcp/YQePbCyoRVS8/Ti404FIYSvZhtxH90AbEkq2j4VsRxcElpmFaG5c/wn9fMYnz9nKEKbC5Ty8Dgcm2/110ajpvC/IJlzB06R5Le0+RlmzkP/8bvqTmkojoOqj5/jkHnMWHQ4Wbc1ukrHsBScPd1j9kcvX+/N8UwHM1nw/18M1ZJsJB4VAlPDB3Z7D2oc/Hg+6ywSts0HCd886Ifulopfs0y8/eB3ac09FSHAITPY2XicNzHj52X+hoLoZWv/CAv7sdI/P33kDocLlmDZtGvZl7UZTm02ZiA8wAr8Sxj+h3pnCmnQ2lp6Mk4+IIWhUvAOx2S8mITtWoQj+4J2ctIyg1LtdJHYETtAOcggsAQC3N3n2HcGXh0k4aNlZR7xtfgZ1WNnRTrJR8M0L8nvJXOXrvK/g81L+XGBeHgjYl+vFZ7/55+J4BG4nkdR5IARipxnWEZ/UX3DHVIF4kO3HyNdxvorq2lJXhpdfXULlqvhzsyKWf/URT40m8kHrQJ3YObUVBXjsoXu4BOV57JWJ+IAj4ATsalmXzN2hhxKTk+TgpVmHXScz4olddajD14AeuSb0EDCyMTI7XdDotP41pD9f3yPuKBz6Wz7I6ygcJTyn103Sjb7sWER98F14fUiqM2i1BxZRs/RjR0aXFo9KLJV/vrAjNbeCwCOAKqjQueD7r4Yvd9GRYDnMWbJQHtrdn+Fe8ngQlZSGsUP7YsvGjTDbXf4lZWRjSW76W01jw+9dLC5zMkkS27FAdp7fi8qk76iJMyDa6rBzbwFPlNl5BbElOCwa551+NpJjNPjqs09Q3th+RJj63wKFfMcPAkJARrwggwFusmPYdpq/zh0ug6wx3OAdhn6CHfeJ+3hOcr/1hYvk/pgnJ8Eu2PC4sBdZcjupsiIWXL8IE3tK2LRmjb8UICr8JAxMHA2btRjZ1RuIsL890jQbb6LCB6Jf4li4bZVUzjqe9cnj9qDf8Cm4ZGoaLr/yajRb3J3TCh4Sn3MX3ICb55+Kn5Z95U+GcmwGLgV/PQIqAf9qsG7qhAf1og2h8G3XYXe107FYROEqKR2bxWKshRENAlHB7UVMSn9MmzgUX738AIw2oqtGRP+0hThv2LWIJUlUU/UN8qrWwXMUXfJo9GBSr2/qAswbcTPiwqLQWL8CBTVr4SKCqQQJq3/6Bhef9xKmjB2Kz5Zv4wRktqtabcDAPv2wbfmnuOfhZ6HSGjpVSQV/fwTcBvyrwJw2IdDjDrkfokla7ZMbIAk+tfM8knyz5UTEEIliiZpjSRqWSUbUyBJGjZuKUHcz1m7b68tlTv/URNj12U+hd+pliJE73DZHz0vYFVjWX5YkaHPOswiPm44BwQc5gohQ9RX7sDWrEGecdiq+XbOTZwIm/ZN7Tpkzyuth3lMtt3UVdB90WwIyMLuujpTOqXJv9KXPS1FJElEFE/2/QXAQKSTYZA9Pc83lo6BB/4w+aKguRaPRzNdYMsdOful/eYbWpOQLue3lFDzoJSfjfiJ3BFiKan/uQSJYIcxE6mBEUtN22LhaKmezUIFnKt6Fgwh1ahhRPiS0s57MN+tyOlBQWI5pM9MREaRBs02CITgU4TE9ER0bhfr9Fr72VEH3QrclIFM27US018U89PBEY5T/OJNaq4QyVMh2ImY0PlYVYoNs4rkItdAgSB8Ku7kSHr4n0KfqMa+sWqXrXPSsIV4Z0Y4vhVIYZCKgf+6AEalZcMJAZQXLqs7jamJmJRGTJ9cUNfRzqArJpxiIXLYWI3Shw6DTa+E22TH/oitxyYVzkRQq49ZHtlKdRHQRaULB3xjd+nUyBVFPRNAIvom7DtuMeT59SUQF6IhAwZyWAt9nZ3VYEJQcBY2oJvpK6JgQkA7y2PLcglRmMCOsIHSWyya7bVQWOx4siJ3HWekG+OYPBelAOd4Oycl9QiqEREfBaTbDwWxPtYAta5fD3NqCG6+7Bied1Bcbc4v9e/wVdBd0awIyO9Dj247KP3v5kSPBaMZlm+xFfmERLpx8GuLDQ2BuNHXIwEPO9whehCEI0+UeiCCCezsloIz9JOni5CBEClpubzLoiDKb6Zp1aPBLu46VLjJf6sKnQ3R6DMjojYqyIhjtbj75X7o/B0WFFThlxhz07ZsGocPDozCw26DbEpARbyQR5Cw5HmOJLrFCEB6RRmGrWI2viAg8lbagOiTVNfsrZ+cmOG++FONGDETBd5tI0kmIjRqNqQOvQkbMAJJsaVgw6TVsKvgPbmhcC41Kd8h9Zb/UPDyXq1dyIjJiGKYPvBq9YscjSqfB/IkvIbP8c+wqXY3Y3oMw8qQ++OL5N+H0eKElAmo0OlJ9WS53B598dzvJgtWrO1NQK/j7o9sSkEk0G9yoEaz4CAWcFkH0uG10TEPkaBBN+KeUhRI4Or2ZKo0KdWX78MO6vZh78cX4bt0OmJxuON0m1LXuQXXTVl6yVi3C5rTAw5azwnvYnVlZhztLfPuJPG4L6lv3or55N9jKT71ahXZrC6miapw5Zz70llL8uGE3Ecy/Goaucbvt2FdcjFvmX4yn5RC89dabKKwxEfGVqYjugG5MQAH7hUbkkrQ7GCo+raCCWbZjqVAJLT/zwDpPjejG/5Y8i8Jh/SH7IyaZ24uxLm/foeWIZEUKR1sR04WEEtSwWMuwft/+Q8shVVWnC0JB5lo8tK4KTRYHX+fJwJa9MQn89fuvw9laicRwNZFYOkRqK/h7o9sSkEHkzpauwVXQLjoyW8TcWleBZdVlUGs0/gUDKlIFDUcW8hshCEcrx4sd61aCBbjQaA4lNZt0t7Q14sN3lnDbka0F/SPL0BQcX+jWBPy9YBPjx1rFY1LvaHdki661OsNR17QeL5D9IdgO3mPYcawDPm+zxBeEy7JAg5xvTbDHzVb9iBAOGlu8XpnvBjl8z+LBS4hZCEnx4JABvpsctpjd5/U6HtfAdlsCqkQRXul47q6/Hcfz0zBOREYE0SAiocXkC3+vUQsID6OBQ/RHWWcPoFHjtKnJsNtdsDS3Y/n6OgRHBWHCiBhk7alHdbOT1HIBLo+M085MR1C7Fd/SOWxVEiMo3yMp+eIJqYN0uOaSfsjfWYX1mW186oaBE1L0EVVLdn1khBZWsxPtrq6DaAUS3ZKAbETV6/V8C89fudi7qyjZBx9jexTljo2AXV3L1pkJB4IMH47OuC3U47wsroz6wOI3mS9Tk3wblDv2VHJp459bhG+e8cC6UZkkCl/X9hesJaWyZRWuvWkMEiUT7npiD2wuGcHhIbj22qGIC1PzJXWC5MYPm+oxYUwitu6sxTkXD0ZrvQX7jCqcc+5AnDutJz78tgKxsTpOsjNmZ0DTaoIuKpiTedu2OkSmxuKcU+Jht7nhkUWcflpv2EbFYURmE2kJauh1KpTlN+DzHyvh8ABxdP5LD40gu34HvtnSQuUcHK4/8HFxuiUBGY7FVie+07yTcHLn9nUW9pBP1odG0kc13MYmX4gM0Xc+eEAqNTRRMYDdDK/T1XUYfBYd2+uB3hCK2FA9GpubfeXIvnnD6IhwWNtNMFus/gBRMkJCQvmCACdJkCiDFi3GNn5ckkRExyVC8DrQ3NLKzz9a35O7mC89cmLlUDDZEhykRRg0vO01JHlio3XIyqxnkTt4e3B1UatFcKgGxloT9paEYdDgGGxbWo7Hn96G88/pi+GDIqEN1nApFqSlASdEj4z0SOi1Agr3N8PYYkdpZTvOPLMvDG4rXn1lJyS9FvPmDUCEy4KvVtagjqSoj1gS3z0SGa6j68UjV8kfB+Kw2xLwr4XMJvaQcsXd0HjqUPK/d+ldi+hxyZ2I6GFA8YcfodeC2xCSlABRp4M1dwNK/7cEtsYWRM24CKmnnsojrAX36g1XVS7ynrkfTrOV78LvKN/t8uD8q27G6WMHAoYIpCfFYPnXH+Gpl/+DUbMuxh1Xz0cIjfgsfv1XH7+Nr9dk4Z4HH0L/tESSDu1ot0tIjA7CS0/eh5XZjbjx1kU4fdJwIqALq5Z9jtfe+QTuLjbmMi9xHPR8qubACh/AATca4frZVunc/U8DkUzkmTIzDWMzwuD2yJ2LCPQ0KMRFGTB//iA+SBTZrBg2pgeuOj8dSz/Jw479VowaFoMQvRrJfaKharIiJ68ZVosDpRVWGC1tyNtbiw07WnD/bSchNUEPZ1AQpDYT7nluO3bkmqGla4OC/PFwuO0ndLw1Di+9u9lX3IYrzhiJV55+HCu27+sym9SxgELA3wWBq3+yIQGRvXtCePdNqFLGIHn2PBi/eo6/YEfVPrSu+wLq2H7oc/kCWHK2oXTZKoQPmoTY8ZNQ8+VbqNiyAtroSJ9kPIgJvBOTipmUlo7x48fjjef/hdzkobjkkgVYteJHeNxOrF++DPsKijF02tm44vqbUdn4FDL6D0T+1uVIn3AG3FkrUa0ajBkzZyBuTBQuPX0cXnmR6hbcFzddeyMaK0vw/vebSW3Tdt6XlFqE0L/HpFHoBS3RzWd1sqV7e1GNxWIuPEeZBCElE6tXFCFUdnCVWyB199P3c/B9kIoHy5lzTho2ry5BcaOMpx8Zhx++zMH63a088AFTX4vqeuL6qwej7T/FuJ7UVnOTBbExeojBpIpGhiI1VsSif2yGLtSA1B7BiIo0oN0hYe75A3nkuf1ZdUhJi0ZEfDjayd4rr7Cg3SOg3WjBux/tQ175gfg3TFHpkZqBwUPHkpQOO9Src4yhEPB3gqmZ9uJ8aIZOhZpUzcR5V0Gu24Oyb5dCjOxL0iwE0VPPos4RzHNXSB4vxKAQhPbrz4M/Fbz0BA9lr9JofenYDrPLOparFedsxctvLEHssBk4e+Y4RMZEY2PWHowafBHOmzcM+vBoaLXBSIxJgMdpwqYV30OK7oe89RuhTtdgxtD+iAlOhUhG2JgJU0hQB0NH9Rg7YRTe/27DIVmXBCKXHTY8LOyEgSuyHccBm+CB9yiBiPmVNGqsWlnCV5ZrmLrnITqrNbj6ykFY/mUR0jNiEaGSkJnPonl7EUW2msXiogFAxaNVvflGJvZPjCeprIKt1Yon/7UFcxdOgLasBu+sNeKFR0ZytXbWmemYNCgCOp2IguwmXPXKDqhIBZ0xsxcWXDYY5jYnjETeF1/LRrtTgsVoxXsfFXAnTscKIjURccXSt9Cw5zvszirmMXICBYWAvxNsP66jpQKSKggRp8xFwojBqH5jEfW7KJx01zPQOKtRt3EddBmToJKdsDdUQRWRguDIIDSu3MyDvbGYpT+3u51JRZvZRAKE7cRQwe12wStocdMd9+CssT3x6UefwRmcjP69U6DnaZN8iTkltvuQPmtEkXcunV6Dotx92Lx1JzTU4TdvWoXyUlK7WOang+Pd0D8d/ZsnpyOBlFG3v24aWUSx0IS3xUq+r/FoYATpLIs5gLRqpPUMg0EnwOWVkd4nEu02N+rrrOjVJxyaVbU0OPnGHpVOg7HjkqHb1cLDK4r+8N1sgPB4fEMBi3v63VeF+OZDNy66cjj0dhuyC4zc453WPw5poY145tVcuNlKJRsNF/6wkZzkB7crEbCiMAf11AZuGgW7jiV0bKAQ8HdCUKnhrK2HVwxBn0uugb1gPRFuGwzDzkFYrwQU3HczGvOb0G/U2XC31aO9qgLBfU4liedFe3WlLyyar6Sj34O70wUud9gP20mhIunVv386tq1eimdeegMXXLsYOq1vuYEoCP6Nwr7VPWw+02pp5yELU3QerPjuC7Q6ZCT1TCGR1tb1PWX/fYl0gnBgcJAP2vXxa8CJ4/bC4fDASZJIcjnx4Zf52FfuxFgaPOaeHIW+vcPQMzUcG9ZWof/QBAxJC8IPP1TxqHUq7uBipBaRGB9MJFbxNmglm9BBdUtIDIGjtNV3nAhk0PlsPovVTfaqwIMOH61lPWQizF1wK26cNwWvvvQ4vvh+Iw1Gf3JS2F8JhYC/FySRvKZKngswJMyNgi/e5+nK3M0s+1I70hf9G8kmO8L6DEDbts/hNLkQmjII3vYm2Kqok/0Ko9+XqZiN/v6uTx3NY23Dhk1bcOtFV+KHk6YiIiGV79jn0xIs46/s2/XP6MKmLeBow5sfvIxHn3gEny79Es1Up8SEaLz8yD34fM0OvvewA4y2VsGGf2EPjx5w4Fl9q4o0v+AJPVBvtqJIRHJSKELDDTjjrD4Y1DcKA68fjaZ6C774sgTtumTctnAYggwCdu9qwDmn9UJxVg1K6x2+kPxsl4gkIYZsuisWpKC+rAV1pF6KJGXnzh6Acf0MeOqzJl+IyYNGBqZe/lKkAtauPXqmold6P4TQ8x+r4GBdQSHg7wQPnehqR/EzNxMvnLCWl/FMTe76YuQ+eQeiho+Cu5HISFJSshohaPUw7/4W+wp+hL3NxqXT0csWSG3S4Iu3XsZyspugDUJbdQHuWrQIVRVl2JL1AuqKcpGWGIbM3Xu4TdXa2IStedloqq1GZu2TdI8WiJmFWEsSt6CoDLfccAOmTpqIUI2Ewv352Judz+9xJAS+VvYPgcijDzFg/ty+CNbICI/UYs3KUhQWtqK4zIzyKgscURF46MZBWPdNLkISw5GRqMF/P66FqcmOZ1/ORLXRCx1JP1OjFe98XAi71YEmsxcz5gzAzfPTsOyzXGzPM3MJ6XYemGCXf2G7FlNjNfoIDB3YD7X7t2HbzqyAxthRCPgHwKSOtSzP90Hlj7RLqo+jZC9qC3fzSXa5ww1O33saymFmWZHUv9zsbGF4bXmpf2qR7DG7BdlZ2SRZ1HwuccWyz+k7gdszTPVkalhdUyPPA99k2u/bvd/SglpGKFKvGsr248OSAl9KNZGtSVUdNSz9H54eo3I9TifefHMXaQhutLd74GCrUFhd2Q9Jx00rC3FDaSMsTRa02IFHn9yGqkoWlQ4oKjfzZ/rpm0JS322oqDLzbVmMJ/l7anBXXjUKik0+byuYmiogc1c1ynJpTPyFyjNpZwgNRmNVAdat+RylVc28TQOFbk3AzpUhf+Vqhy4StPBjHVuKDq6PqDpkreMvgUnJznUsPD21X2IJjFRHLjNX+Z0JqoNea8f1rJMdK1cDX0BAI0czSTPfzYUjHCHsUxFJRE5IOj+/sK1zLajKX9PszHruIDnYuVNbbUKtf1DqvB8VUFnRhnLJZzP+7Numd2A31uO+RTdyG1NkC+7/pOf+PeiWBOTeQ7sdeub2Dw6Csa2NW0WB9HadiPilxC8dEbyZ1sik2OFQa49UDY+2E0Tll5C/FkxTOB5WZ3dLAjK4PV6cNe9KXDX7ZOzauAKvLHkPbVankg1IAUeg14B2oNsSkM2BbfruU8guGx6982psW7ceP+3cx4MtKVBwvKD79kaSdLUVxdi0aQtabrgcOk1g5nkUKPg5HJWAx4uI/iPQaNX0o+UJVdhSLKvNhvCw0G7xbAq6B7qvBAR4cCNTbSXy8itx6XU3IThlOVavWo1Go8U3Sa1AQYDRrQnI5sYcNjNq6+ox5ZyJmGo2Y/uWzahrMfmTkilQEFh0awJ6PB5Epw3CyRNG4b//egAvf/Q9RJUYsHV/ChQcjm5NQLaWkGW51ekklBSWESG93DuqQMHxgm5LQDa5GxwWibTUdIQaNL7wuYrzRcFxhm5LQJZ1dt41N+HG+acjZ/1y5JRU8vWEChQcT+i2BGQbUVctfQ+7l3+C2ppa2F0eJaCtguMO3ZaAbK6vtbEWjXUss6zumJOvY4/ZH59zPDg00h8D20XBNqMyR9SxmgtloRfZrg1l8Osa3ZaADDzadABWwEgeN1xuF4/8rNHpf7/q63VDcrNIZCJEFjvmD+xbk/3hExMTE2Axt8HmcP/lJjEbgyIjY8gecKDF3K7ktu8CXRKQjY5/3gh+9PKPh8Cofza8ZHsOHnsaLpo9hf52YPXXH2N9VvFv73xuN4IHTUPPU6eRBHGhZfVStOTld7396VeA2cRjT52HOy6ZjgfuvR/FNudfLpXcLidGz5iH+VP749577kVtm12RhIehW0tABhYNmoUQ5BCYbegLYMvmCDu0O2Yvsq1KTHJ5ZX9YQICraow4PHcBnc+P8zAtIt+P1nG8I2km2+TKfjsddljsbpw6axasJduxbk+hb/MoVwG9PNwCDiq/K/BEni4H3HYHYk85HXJNFlpysn2Bf1lgXypH6AilwMpgEbL5cV89O8oQRTUPL6HSh+K8iy5CY9lGVNW30HGNr20k6cDzsnAOajVkOu7xHgiE76unSGOC51CNWGZtp+Y7TLzUDp3P5S+HRaHO3L0Ti268DGdPH4dXPv4JKoM/OQ3dl+1Y6Tj3REW3fnIvESosMhGnnHIKYiMNKNqXhZ17c2F3yThp1ASMGjIQrXVl2LBlM4ztLqT17Y9wgxZJKX0QE6rC+vXrUFnbwjvI4OFjMGrYYLja25CdtQf7S6q4bTN4+FiMHjoEpqZKbNy8CS0mB4qyNuDJvL2I6dGX72z3QYaLOlyvjCGYOG4k4DBR+WtR29jWZQcUaKCwlWxBSUkmVPEZkDq3Ucm8owf3GYaIwcMhmWrRumcTnCYrZCJJ+EmTEZqeClv5fkgOF2w1JfSdCckZEzChfyIef3MF2l1e6HRqJPfqjehQA8JikpGeFIFt1A77SioRFZuEwYMHo0+vnjC11GDH9u2oa7XhJHrOnj17Qi050GB0Iq1nNNavWY3aJhMSUvpiyuSJ0Ktc2LhuLUqq6oiAGtQU7cWmvUWYdtoZePfLVXBLvng1QeHRGJjRB1ZTEwqLy3i0te6lC/06dFsCyiQJIpPS8dAjT2J470g0tJgxb/ZZuPOm6xE08BQ8ff8imJtrERufiMnLP8bif/4bF1x7Gy46ZRhKy6oQn5KGKROG44ZbFiNj7Jl49tE7YWmqhqAPw9jhGbj17kcx+vSL8OR9d8LRWovI+CRMXfcVHn3iJTS1O6Fji8CZVO1Ij81U0wmz8Oj9d0LjMELUR2DW9El48MF/ooKlwu5ibarAd9Br+ZK6zjSgVE7oqFnoT/WiG0MTFou43FXIe+YxhI6ejf433wEvPZcYejX0oSJyH74WNduaMHD4SRBsZhSV1fLynE4nzrzgMiy84ExUV1QgNCYJc8+agSuuXIiRM2fj9gVz0Vxfg+jEFJx3diYefWoJHnziBSSzOLbaYDjNrQgOj0LPcOCtH3PwrxdfRLzGBatXgzlnnor77l6M/IomiJITe7IKMP38MYiPCEZlq53ejQsJ/cfgv2//G/mbvsSC6++Ey3tiZv7ttgRkEcpmX7oQ4zMicfWCBcirakYqjd4mdwieu24hKnZ/j4V3PIQJc6/DC4uvxYhPvoSKpFVTVTGuvfxKDDnjEvxr0eVIiI/GkHFTESZaceviO1HeaEVEqI46fg9cc9U1aM5fgytvvA9DZ12C1x+9HaetWYu3v98EXdCBziRRh1OHxuKmm29GmKMejz/7ElThGXjqscW45NztePjlD6BXGyDK6DJHRAdklrFEY0Dy3CshtGQj857bYBg+B0Pv+gfixq1HxBmXwpW/GnseeQAJc+9E/wXzefwV2SsgKTYOdnsLzDYbJzZTAZmUddNgcNcNRNYBJ+O1p+7DiKH9sHXlN6jN2cJV7T4jTsai6y/G8CEbIBCZ3v73v9Fv5uXQ1u9AnikG40dOxMWx4zEwAnjosWdgdIfRIPQErrlkDm577DUWCwP1pRXQh52KqKgwlLVYea4It9OOiopy1DU08WgFJ+o+6W5LQBZPZUBGCvJztiJrfxlErQ6lhfsQkjoUseEGLN+2G0aTDdl7cmF2AfEJkWTTeVFZmo+6lmaEkQpldbqh1YjYtfZHtM4aiVeXvIvq8hK89/Yb2FJqRUxkELb/uAdtZivy9u6D0e5FYnICV7E6nFjsFwtVHx4aisSYUB5A99ob7+ASr6WpCjaWrYiFpie7i+exY0vljpJNiUVoEvRBCIoMg3nnT3C2tcGTvw/OFgtC+vam4wY079gLN4sFWroXTvscnjSFBdxlsW2Z3ccDRaHDVhNRX1aAkppahIXUwUjPIQkq9Bk8GotvW4gg2Yl2N6Al1TZMH8K9slZjK4zGFqiNZpgsBoSE9UJGqh6SNgT/d81NPC6Nq72BJKHUmSJOZdDz52PRwXncKq0B1Tkbcf65Z3Fb1gP1b4qV053QbQnICGB1uBEaFA4WWsTqdkPF+jB3PADBoUHUIVzQ6Ema0ZDscnr4dR63i9tkauo8vvxyWmzf9B0WLCjG2NFjMO+Sy3H/vXfh8tv/SR3cw8thoefVZFNpVEy1c/njQHUEl5XpPDscDieY52LHym/x2CvvcWcE+87tdJCtpEUo2W7RI4bBvGc1jLl5JAk7SOiLZcOzMDlskPUunriSR9WWqEPrSNXVqOC1OuBxSdCGhfOELSpdKHeeMKhItJZXVSE4eCKiw0NR12bzlczy1lN92bNy7yRz4JB6ecmlCyA15ePaxY8ipv9kPP/YvT4HE3yxV3ggJVHkP8ypxMhdsH0d7n7iRXhJqvLn8jh4tmEWHa1Xei+0t7Wiudnsi9ZG9dZFJWLSmBGwt9Vj+y4aNLzdzyP+a9BtCSgQy9auWItzH7kFd9y0EJtzyzFixEn48YtvsH1vEU6fdzF2FzVgwpzLIFsbsb+8BqNISqplfzQzATzMu5NG8plzL8PgWGB7dhGKK2rRm/Qte1MtduUWYt6cCzA3rwLDTr0QGk8bsvbl89RfXo8dzW0WTD/nYlTa9cjJL8DKzXtx0fRZOI2uq2zzYPSoEchc+wPWbM1C5KjTMeDWi1D2ihmt2TmdUlAitc9tMiFm6vlIblfBXJSH1pxs9Jp+NpJz8qAbegaIa2jeuQneiOFIOe0i2JqsiJx0Pg0uWq5qsrDvObs2oVVegNFD+iG3rAZsbpHtl9RqOp5X5OmxGcG8RFi9SouUXv0w+/x5SCbtgIHNqTLyqWlwYN5b9tnrsGLDuj0kMS/GmafuQW5pE8ZMmIj921ZhxZbdNNBEYPL44SjM3YA6cztEUqE9LiuS+ozAM8+/jPLctfi/yxfC6fJ2aQd3d3RbAqqoY2356VP8MzIEV1xwIabPEdBQvh9ff2DEGy89gej778M/7nsQjvY2vPDsv1Bc04ra0mKShOXcdW+3GJGZmQmbnSQUqV9nnz8Xc+aLcNtMeO2119BkbMOHS55DYsQ9WLT4frKl2vHKs09hS24l9EF66mQWfPTO60hadAvmX3QRDEvfx1sv/BMGYTGuuGkRV8faGsuxbaUvUJStuhCNm3bCVlXduWicBf+Vicg1Xy6B7sqbkXTmfKhXfoDqT5+HPuI+pFy+GJKrHeXvPAdzSSmph2Rbam5A3NQzqT4WuK02tieLP09rdRF+JKKcM2c2vl+/A40mO6roebOcIiSRPZcZe7Oy0Vxfi49IxV5860147LGHUVRWifXr1qK2vg55WXv5XkqhdD9UxhrUk3QrNmiw6psPEEWq9/mX34B5JEUdthbkbvkRbtI6Rk2diaEp4Xjipe944hU9PStLi8YksZY0j5aaKp4tF8KJRz6GbktArs6QGrT03X9j/Y9LEUYdpaGxAQ5SNaWWItx96w1ITkqAhVSjphYjdHoD3n/1GTA3v9oQgtr9u3D7Hbs4F+q/eRd713yF6OgImIzNaCb7R0PnN1UV4f47bkKPHoloNxvR0NzK5xl9wWI1KC3YjZuuveJABlvqnM8+ejc+TEyETpTQ0NAAF+lvuhCy3Va/h5ZV7/O5OxwUOIo5Suzl2dj30LWQO7ZSUTmFz98FQ3wPSHYTnK0tdFBLkk4P49ZvUft1I2KmXIqwlHi4mptIIpOKKnnw9cfvIvmK2YiJjiR71YNvP/wPljHHj8oAc+1+3PuPO9gdqfgyLMzLRGSYAfW1tTyPH1Nnl61f62vXzPzOCNRrmY1JUvat5/6J7z9OQpBWRGNDPWxkP2u0emqbaPzwxftYtyefp0ITyM6WBQ2GnDQUTlM9ln7+GWykOrMEMiciui0BOVhQV/ppaaxDE8sqq/JNuKvY5LTbgZKSEt6x1P4NugdW/3TMNvt6mUAjtdnShra2Vt+GXv/yNmbjeD1OXznigeMdYCpex4ofXi591tDf9dWVPPWXmk2q+0nlu+VR4qozdZStGupw7NB1okySprrUNwFP9ZCddujieyPt2lvI9iTCUEcv/99LsDS08cl7Zp9WF2fi3gezedTpjgUG/ifk9+4glYrKM7c1o61V5hPt4mEuSvmg5mEl8OC5pLY21lXxSN6snbmKStVe88W7WOFy+xYiCL5MuoyI677/CNlr6Cd7H30+MsjwiYKABWVixrvT5SSVz8Wlxl+5S505VY5QcFin0R7qejv8mQ98Fvwdqgs1qYtyfq7MjgjXh5f0c9MPXX3Pc1NoDtxX0Blg27cBOfdmkyTUQbJZ4DIZiRzqzsUrnHQkrSRB9GWzPaRM4ZC1oWzwOOJx/Sd03TcETtzDL/F6vH7yHWhL9idbFMGcYWoyFU5A30snAiYBnQ4nBo8+Gf0Sw5G5Zw8qquv+0GJjBSwcvBdSaxM8HQcOIl8Hjnl0cLHrUPFdkfVERMAIyFSRHr0ycMHFc3HDFWYsvP5GFNebTsjVEH8mZCXkxt8KASMgm3b6/sPXUFZWgfdefwIpsTHYX9vKVR8FCk4UBLS3M93faXeQLejiNmEgEyUqUBAIBJiALG6nDW63GqnJSVDtKwtkdRQoOOYIKAE1Gi2aKguxZWcBFj3+HMaftgZPPfE0KptbT+g9YgpOHAS0l7ONsoawcCQlRmN/zi6sXr8B7U4nn1NToOBEQEAJ6PG4EJWcin7pcfjnwtvx5ZYchIeFKIk0FZwwCCgBWYgDtl1FFtl2GRFBQYYTckW8ghMXgZsHlIGxM87B3DnnweBuR6vFoqieCk44BIyAbMIhPqkn1M4mPHD3uyioalAiZik44RC4iXjSNFd9+R5WLJX8awI1J2RQHgUnNgI7Dyiq/CH+FOopODER8Mk2xemi4ERGwAmoQMGJDIWAChQEEAoBFSgIIBQCKlAQQCgEVKAggFAIqEBBAKEQUIGCAEIhoAIFAYRCQAUKAgiFgAoUBBAKARUoCCD+lgRkOcwlHq36121fYjkZJH906w54vSx8rXDUHO0KFBwL/O0IyCIXJvRIhRZOVNc1+EK0/wxY6Puhk2ZhzimD8Marb6DV6uQpsv7vypvRVrIF36zadkROBwUKjhUCtyGXmCSxPAX0w5KFMGaxhCWMDPw7JrUkXxbXjrxxguSBzaXClbc9jD4oxHWLHoJLE8ITPjKw2KJsp68v34DAJZ/KEMajbmurN8NosfFEJS67DQ45CDffcD1278lGrcnJs7kqUHCsERACst3wLIOOISQEkZGRsLZboNaFQqdyo7KqhiSUDjGxCYiNjkBzYw0amo08vbJKpUVURBBWfvM+NrqMkFR6XprBYIBMJIyMSUQIHWLRtj0yC/rkRf9R4zG8dzjuf34pXLIALctaCw9W/vglrrroPzh9ylgs+WItVD+TYEWBgr8KASGg5HYjdegpePLRfyDUoIHVYoFKHwKt24g77rgdA2ZcioXnzeQJHlVEls8/eBNvffQVInoMwiOPPYy0uDBsX/45tm3bAS/0uOqO+3DK4FSodGFE6DAs++hNPL/kA7CM5CNGjoKtuRL7Smqg8dt7jPzG+goU1bRg/NhxeGfpSjqqqKEKjj0CIwFlCcEh0UiIMODTTz/HORdcjrVfvYf0k8/BmBGDUVCyD6++lIXymiacecl1uPyKa7B85XrUt1TjlRdewqK7H8KAfumkukrcJkzq1QcpsRH4xz2LMeyM/8N58y7Ep198g6I6K1J79EBDdRlMDpaF1Z+Lj2WEdThQXlWPaak9ERKkQbsHJ3SaLAWBQeCcMMQFq6kVmRs3Yfz007B5w25o0icjQh8MY2sTzr3sYpwXFYzgyHhoDWqEkbpa2ViJPbt3oZJU0v4qiRfD8uaJJCX37FqLZStWoVmfgrNPHgidXkfktEEj6CGTJBUOyTshcLvR43STvaj3eUI9XVdTgYK/EoH1gooCd7BILKMrT1opQxfZE/fedx307cV46713kDZyOq6ccwq0JLVYKEPmXOEOFkmC0+2FpJEg0BdOq5VnXmXM9rJEL8yvI7nQZGnBqN5J0DLni1vm3GMSWKRzExJi0dpYCruNpKPaZ08qUHAsETACMhKpRbX/t8pPLJDEi0ZSbDi+/fZHrFizDXdNvRhBWg0kIpkhKBQxodEIMejI8gtFYkICWuxen6dUJfrSPBOpWVplFambkuRBZtZeLJh1GVLjI5Bd1QKWK9frJRU4Mhb9eiVizzdfwuoVoFUr5FNw7BG4wLwuJ8xmMzxuD9rNFiKFGzanA6ayffhpdRD+77p7cOp510IXEo6GhkY4SI2cNOtS3HrlOQgNjYAGkXjtv+/im3dfh9lkhNdm4ySW3C5YzCZ4SEJqVQJyt29Ate1anHXaFGQt+ZRn4fV6ZYwYNxWx2nYsW75OmYxXEDAEhIAqjRbFeZtxxz05aGlswSMP3AdTawv2v/gIPO1GtEsrsXPzGETqZeTu20+KoYD61na07FiBhyp2weV08mM6UiNbG2rh2ZUPlccBXVAIyrM24tbbclDfbIHeYIC5qQqfffU95oybjNiPvoXR7oE6KAyTTh6Ptcs+R25ZPUSV4gFVEBgEhIBMUtntFpRVmLj6aK6q5L/brVV+T6WM9auXc5NMFH2uSZHUSmdTLRGu+pCyRG4bynwyn8UZtdvMKCtr4+czb6dWp8G3H76GbSuiYXUL3NWpFjz48PWnYDU2QebqbwAaQYEC/AwBvX9xxlpGwg7Vr1MF7FQFBWi6WpnCbL0ujh+sQAo80K940GcBblJ3q6qq6XKfrclW2dTWVHPyKpmYFAQSRyWgg9S87oKDyd4Bxe5TcDzgb7cYW4GC7gSFgAoUBBAKARUoCCAUAipQEEAoBFSgIIBQCKhAQQChEFCBggBCIaACBQGEQkAFCgIIhYAKFAQQCgEVKAggjmsCdiwFVzYrKOiu+MMElDxuuNwe6PR6vuj5z4Tsp6DwKyjIzvXSjxrK7gYFfx/8IQKyuCxhMYlIT45D8f5CtLvcfxoJWYykWXIaIuDAl0ItkUs8Kg0ZTQ3QwEAnmGQPpD+lBgoU/PX4VQRkEcUkWYLHI0GtVvn30LHI1gIuue4eTO7pxk2L7uXnSJyAMs/FoIHQSRv6hksoXh7LyeD/poMuLLa1SN+r6J9Av+30kyHHIAUWfCXUdJbhpuMi/9tXPiujna4+Vc7AWZIWN4tZdI4IreSrr6gSffv+lF23Co5D/CwBWfQwt9NJxBIQGhWLyWNHo7l8P3JLKomUEmJ6D8Oc08bjw2f/gfo2C4L0YZgq98BghMIi2LGWJFexbOPkSkcUpsnxJNEE5KMVa4RGOq7CaCGOjniRIUUihv5aKVSjnCg0AwmoRxN2C208/ATDEMTSPzVS5XBo6ZzvhCo00/FzkIyp9E1/QY0LhTS0etpRnBqD9H6JyN69E3X1LZzmWq1O2YCr4LjC0XfEk20nySJS+w7GhMmTccbMmRjYOx5P3nMXsovKIXllnDnnfGhNlVi5YSfcKi1ORwbuklNRgDaEynFQCS7kC2VIQzxekcYS3RyoJZk3kchSKBpRKauw0DMM46BDqWCGW1ZDJdrwrtiKaVJPTKPr8uUS7BFa4CSp9n/SYJyLcOxAC5UQQdeF4wEUY7qcjCFyCMJIyp3jTUW1ux7muHTccvc/oGqrw08//Yg169ejoLiM7FW3koxFwXGDLgkoeTxI7Tca1y+8AsMHpsPc2oh1637E04+sQWlFLUSys+L6jMIFZ0zHDx89i8pGEw+AdJIUh0bBiKfEvWiQ3eDpv0hRvMjbHx6hFdeIO1BNsiiJLDYzfc9CBDJVMpsk2Q2qvXARIUOJaBbZhUXCNvxLPpmk3QHVkSmcOUIDrhK2oLfcC+/KQ0nqFeMm1SZcKY3AXJKLVwq74NLRuZklWHhFPiZOmIyZM6fjrHkXoaFiP15/+VVszS7gMWMUKAg0uuyFXklGQupgzJw6DV5zFT7/7kt8/eNq1NQ1Q6PTwusVcdacCxAht+CLZaug0mpZOFxSH0sxTh6Etz1TUAcznlflYBtZaOlEuO1CCSpIbdQS6Wph40plCCOoIGOr2IQm2UtyUCYZyYNm+72awEH84zZilWyEUfCgXjTDInlJsdVwy5LFBGXXsCC/LLCT5HaitCAXzU1NaLVYcNNNt2DMhBlYv/wHbM7Mg8CCNh2DBlag4OfQJQE1WjWyNnyBhdeX4axzzsb5V9yCeRddgY0b1uLD995FrTMY58yajPU/voXi+laodTp+3VahAhejEYOFKCyUh+A2uQ+uFfaSwuhBDwSBncUcJgaikuqg7s/cMepDHDZe2OhPL3P+CBJd46YSWAwXAcGCnjtjVHSFllRkt99CZFHR1DxIvRftXi+S4lJx9fkXYPrUyYiPDEJ+1ka8/dxybNy6EyqNRiGfguMCR9HDBLKVrNi2aRV2bFmHuMSeGDN+Mi6YdyYGpW9EevIYxGtacf/SZRBUviKYb/ISeSDZZg7kwg4Xk2CkqrpJWi0Xq/E8BuAB+pxF3wyVw/CBKh81ssy9oSoWUtA/6y7Rdf3JfhwlReIkIm0UHbueyt1DUtJO3zJ772ayMftIKVS+HdlqK6nEAlrpvn3pu8UYjFxPE2rThmPC2KFY893HWLl6LUoq68iu9UCnUxwxCo4fHNUQYuH9dHoD94Q21ldh2Rf/w6oflkIfmYAlD87H2u/fRX55PUSNnp/PJh7aiWCz0RPTSDI1ky34oljKlc2NpJr+S9JgnpyEUUS2IjTz+TqmYu5ADSokK/zhP7m3Mp4IOgkx9E0rqolcI+V4GEkOgtTUJtGKqXIK9FTu02I2CmUnqbIitpH0fU82YLAcDb1GxKt7V+KahT/BZbWByVgWrl5xvig43vCLnghGRI3GJzFYROqEyCg0FGXis69XwCOreMJLBnbGN2IBlsvFCBFUMAsuPpnuS7ki4RNxH76Xi8DSp5gEn4NGIAXyNXEvXev756uQgPViCVah+LCaiJgkDALJTdwpFFK5IiyCl/9maCcJ+Ky4x38mqaNegc/ma7S6P6OdFCj4S/CbXIHMdqotycOdty/i0ah92YgOLoxsMiJFK0+NKXQuChP8k+Z2Ukdt/POBVS1qHBmfk5HxcNowyVgjW6Am8lo58XDIsjN2D93hZSmGnoLjHL/ZF89yurOsmEezo4SfWbn5c9/9EtjdXlNlco+n7vheQ65Awa/Gb+7JfElXgJZ12f3L1hTBpqC74G8lShTiKehu+FsRUIGC7gaFgAoUBBAKARUoCCDU8Ko+A+Qdga6IAgUnGgRRrvh/LD1GBibQ1noAAAAASUVORK5CYII=) 

39. 

40.  	看图写结果：
     ![img](data:image/png;base64,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) 

41. 

42.  	看图写结果：
     ![img](data:image/png;base64,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)  

43. 

44.  	看图写结果：
     ![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPUAAADHCAYAAADBAxXDAABovElEQVR4nO1dBWAU19b+ZtY37gkxEtyhQLFCW6hQ76u7e19dXl2g7qXuLdShQKGFAi2uRROIu7uuy8z8597dhASCvPfTFNL50pTN+Ny93z1yzz1H239gqgIVKlT0DAj4Q/t3P4MKFSqOLP42UnshQ6Rhhf0eCjIUOko4jCNVqFDxX5Oa6epdkatNhz/0PgU6xYwnlEFYK+ThD6EZOmgOcn0RyYoRVtGFRkVSia1CxSFwUFLLXi/cHhcMBhNxS4ALEtFPoP+zE0X69VGMbRfbzqFfAx2l0I8TUicJq6OjZPpx03a9oIW+neYKv4bCryvQEQLtE2mLF5JiwqPyWKzEbrwnViFc0UFweyDRjfR6uoKo0lyFio7Yj9SKLMMrEcFkBXHJfTD99GnYuW4FynLrcJXYD/2IZM2iAz+iCJmClc7Q4BSk4EwlGhqSpGuEMiwWahAiB+JqoRea4cE4JQpewYFPhRwEKeE4DTGoQwsqBC+/ZxBJ4ssRjwAi+kA5BLl0/ldCKVKVWJytJGKwGAST0he9pFjspH3CuSchxFuDVes2oaHFCq2OhgCRFHlBJbgKFZ1ILUleGIxmjBw5Fmefex4mjRkJ0dOC7M1rcJk8FBcLIVhE0jIZwegHM7ajFdOVfnhJHoRtQgVaBA3OQAKWoxohQgBuVoaR1HZgLVE4VglDf/qrliRwHIJwmhKJGtTjT6EFgTDiJmU4DIoFK4VGXKWMoC0KfqdzQ0i+M1luUDSIoM96RUBIQl/cfcU9uKG2FCt/X4rFS1eguKwSCh2jSm4V/3S0k1oiVbvfyBNx7+03Yli/Xsjek4ZP33sN6zdsRE2DHRdrU1AltGIxSlBL9q2FpHIwEftCuTd2ioW4S0gnmSwiWjDApTBikVItyPgGe/CSUEw0NhBRASsseFSxYiAmQ/Qb0Owfkc7+TNiNV8UKvCgZcTYS8bm4Bv+RrfhenowVYj5miZUIljXQfPYq0tf9ihOmnIgTTzoP515wJdav/gWz3voEjU4XEVs80PuqUNHj0U5qpm6HRiRixHCSrt5G5OVkYMeOnSivboCi1eA7MQsPC4PxuXwSWiQ7EXUXdggukrpaInoD2ckCkVZEk+ImevrY6lU82KlpJumqIftYgo3b1yIdp9nHl83sZxcKRRt/oGrBRpI5DIGKluxyERqBKfkaug77LMLrciA/Nwc6czD69h+E0cMGY/jgoTAZtJCJ1Jr9XlOFin8O2kmt1euwc/UPuPjijTjl9Ok447RzcNaF16IoZwdef/lV7CquwHXaaiQIoXgcY3EjqdnbkINaksYjEUpEKidailxdtnJXmg9tU1ZtJPZy+vqcYl461yswZ5jCKIs4ste9QjPC6V+ZNAEXnSLQgTqBDQQCPHS8S9Jg+r+ux79vugKhAQbSKLbiwX/fhE3bdqLV7oRGldIq/uHoZFMzdbmqohCff/g25n3/DUaPn4R/nTcdUWHRuKkoBrGyhFLBg3CiYDrspEg7sVQowwyyq58l0jXQ9iRSvZ8SdwFccpN8Vdo83OBS+iKlPwbQIJBIavoZ6IMwOQwZZJs76VGuVwYjRInChUo0VokZaFRkrpZXyi5cKPRHgBSKzUI9ouMSkb5pGRYs+BnpOYVwuWXoDTrVUaZCBfbzfgvQaLTQmrVw2Vux6refsfb3JdCRFJe1SUTBKIwnmq0iCf21WAodqcO/CjkkeZ1kA0cjUpCw2i+xm0mFnkV0LYCjfeqLkZqFkbjo50Nkkkz3BZ8ITKVW7MgmKT1EDsIP4m7MFkrBlG6ZVPzXxB04Bb24PiCQPf/tJy+SCk62s6ChZ9PDYOz+hlOh4mhFl/PUpA1D0GhgNJn4FBf7XSsUYR2KuTXsZtFgCiMkI6mMJUIhfqd9Av3lFZgqLZIUt+EboYDPZwvt89FeLBDyuHLO5rOZoswiy3qTdA6hv5bQEPC7aOVXRXu0mUjaQQs+QjM/nkl+De0WDSaoglmFiv1xyIiyNk+ywCmL9sCT9v30Y/DvY1JY2+4AE7gk3hci/9kLNkh46Ge9UIsmUv/ZhTof4bPLDR2vJaohoypUHAj/VZjowYj0v5KMEbZRsOIx7GRGfYdBQYUKFf8LOpGaeY5l0r0VRV2NqULFsYq989REZKPRCJfLBY/X2+2eZFWhVqHiyKCd1B1JrE4NqVBx7EJNkqBCRQ+DSmoVKnoYVFKrUNHDoJJahYoeBpXUKlT0MKikVqGih0EltQoVPQwqqVWo6GFQSa1CRQ+DSuq/ER63BEUQoNftXZXGwu69XhmiyNa2+yL7JEmmY2X+WafTQKP93yP+BLqB0yVBq/3/XUfF0QuV1H8TFIgYOiIKGpcTWQWtnNwMbKVrWJiJ51y3O32pmqNjgzFiUBhYsvPC3AYU1zj48tP/+p40YGgNOkwaHYeGyhYUVtrV7Ks9EN1KaiYlZEmCqNHwTtz2N1uzzfOPSr7cZjwDkkbrj0FXmKjybafjWc4yEmG+3r8PFP/1GGQiA5d2Wi2/j1fy0jbfElFBI9IlNHRZibb5JCDr2zLr9BoNfx5Flugc//pu//FHCuw5Fbre5VeNRFB9OR5+fQ+8rAAC3S+udyRenTER5eklePbt3bBKLCFkEE48IREjh0di2Tfb8c78UmhE3/NItF9hvwJ7doGTlEl2UfB99rWJwt9Bpu2GIDP+8+A4rPxxG2b9aINO709g4X9fLWt3lejHNLqN1IxY0BtgioyC1FgLr9NFHVELU1IyFFszJJJK5sQU6CNj4K4rg60olzoZI6YW+rgEyG4XTAmp0OpkWHMz4bHa2qUbA+u8LGd5dGQoRK0JfVOSUF6ch6y8EpJORiT3TkWf5GQIkhuZmbtQUWtFTGws4ug30KRDTV0zEuJjkJWRhuq6FpiCwjBm5EiEBWiRvnMHKmoaiQBdN5eTKLnvYlXBn6PtoG0iCP6EEAL/jxF0yIhYpCaYEaOJQWJkDnKq3SjIrMST2bV4+qlJ9Ax7r+nxyAiLCsTQ/iFQXG6kZzTC5gVSe4egpcGOuhYPtPTMvZMCYGmkv5tI8rPMMaIvhVTHtgsKj0ZcRAjqa6rQaLGri3qOYXQbqWVWKCA8FYMfewGln85EzcY/ETzmTAy5534UffIsdKknImHaSURuNwyhwaj86T0Uzf0e2sThGPTEq9DBQxLawCVN8Vd0jV+XQjSa2q/vcTuRMmwM3nhhBgS3HaaAEMjORjxw1+2oEGLw/KsvIVzrhaQxwlpTgKefeRHTr7gbl581Hg4ik721FaGRkVj508d4/sOf8MDjL2Da2H5wkt3bWluEZ59+FtmltST5O5CBN6AGU5VYhNOnNmpreOIHO7ahEW4cOIGEw+GBzuVtv5ii12H0qCjs3l6GwMhgjBkahszyKogkTZnkZTpF21J3Jo0T+0XhgTtGICFUw7WXPVvLMGtOLi66cjji4cDjr2zHqJP74O7LkvHccxtQXe/iBLbaXHC592Z89XolTDn3Gjxzx2V469l78dXPa3leOhXHJrpPUlOn9FodxMtIBMbGoVprQOJlN0NpzEPjju0wtcrIzVoLN0mJxKseQvQJp6Bk3tcwxA9GcO8+aFr5JXJnz4YmKBpwN0LU6TvfgCkCWh3iEuPx5cxH8NOmbHz21Ryce+ZUvPzFb3j75ZmcuOaoBMycOQNnTT8RpuAwbFr6A8oNQ3FCshfvL96A808cj/MvDcaF04bjpRlPIKvcg+defhX33nolbn/0FSKFoUNuNIVXFJumJGIgyWUX/M4s2pqDGmwXGvz1OvdvCzKa8eUnW6HxeiAxdZ+IFZMUjjH9AvDtJ9lIndgPE8fH4YfllWQWdL4CyxkHnQE33TgCvQMkvPzWdujDw/HU/SNQXNCATz7fjTefn4QZj4xHfJ9w/LEoE+kFVtJktPC0WvH0jA2wNttJ6+mQlorUeb1OA62qeh/z6D6bmkkaawPsDY0wx/VC0PCpCO8Xi5znnoasD0PUtIsQMaAvl7iBif1gTVsGyS0gIKUv5PpCFHz1ERzVTRBrqn02dRc2rkIqpbOxAuu2bkFRcROKyqtJyulJuhox/cKrcfzARFisdlKp9QghSe4mYtVVV6BWG4Rqsx5lxTUwTB+KkQP7QBF1uOCKm/k1AzQuCAYzdFqW9VRBG6sFXizQjQ+F3TDxdIl763u6BA8vcHAgirCsbpXlFm4LMy+3x0uq95AoejYilkHgqnXKoEgkR+mRW+dFB62bq+khQXokxxqJiDKuu3YEtPRsTpLAAWFGlOUW493ZOXhv5gSk/ZGJz+cWQiDCssdmdnNufnO7/c3APOG/f/8+tvzyOewtrUR2VUofy+hWSS15nUTMaoT2G4uUlFPRtOZH1O/MQOItbyCqfySy334YHikMw2a+C2fZbsiiHoEp/eEo2QNHfQtEg+Hg96BOylMHkyTTsI5J/7qJHCeddSmmjYrHA/feh0qrDm+++x50JOm4ukyDA3eoEXlFsj+Zg41OQWVOGh5/+Ckip5bXGGODjSR2TqXIKnjqEIBH5TEYIZjItvZJalaxczcq8QiR3XkQYov+KSWePoqed/yYaH7/U6b3o316mIPNGDsyAllLKumiOnpGgXvD3W6Z5zpnZvH29cV45/sCaE0aKGShOMh8CQozY9yIKJLGNkT2CsWAvoHYXWhvn8LS6fZxMtL9w+OSMG5Yf2Smb0dWQRk1i1oU4VhFt5GaO7W8LjgqSpF02vUwN5Qg/aOfISlEi8TekO3l8JIBGjX1PATGBKEsrxAaUxACkxNgz9xK2ip14kM4oBl9GFnbfEBM4mjYvK5JD60i06ACDB81AQOSk1CwDjzHOfOiM2+8hpObFR+QkbZ9F6ZNvg4TxgzGuvRiDB87Ed66Yixft4VXMul4Pyap52iz8YsiQvKzl9UIaxKcJNUPLyEjm5cOjQ7CcUPC8MevGXjvxxIYTEa8+OIUjBsTgx+WVfJKpFaHF2PGJ+DUYjtKqhzYntmCqcfFot/GalRbFXrOCOTurEbCcb1x/gnhmPXaZoyePhgP3D4C9z2zBU12uX3uu9P9SXqPPuk8PHffdfjw9UexJ4faXnPwAVTF0YtOOco6fj7y3k8BbBbGWrQb1uI8NG+cj9aSMj6FVPXbNwi95S4MfWoWvM3NaNm+DpayUoimEHgaKtG0c9chi96x/Q67Fdm5uXB4JF4hu7SoADU1ddiybgPyTpmAtz74CA2k/mdn7EB5ZSUkuxmoa0KjphqlJh2srXUoKSnB+uXzEZyYiGv//QSullwkqT2Y/cHr1C4yV2HbmkrgtbQlbFVqfIp3Bxc4m3rTthcdOkTLkA4eGWlEQ00L1qytQnMzWefNbixdVYHJqToEB2lRb/Fi4c956H3LUNx92ygs/iUbX366EyH/HoUHHxzPVfLmRguaKq2YMiYMC+ZlYcHyUvxZ4cFTdw/H2GHhWLaxlk+ldfVMkWFBXII3NjZ08oyrOPbQvcEnehMs21dgx66VkIkoAqmYzKZs3fILtudthdaohbu+hpOGOYPYwJL9wp2++etD2Hk6vQFl2Wm4654HuVQzUL98Y+YjfIByu92449YbEBcdjtbGejST7cnncTlBmcq8DssE32D20JZf4fW48dkbM/Hrd58iiKR8Y0MdWqwO6Ej97yrRqhb/PxJo9SIqCxpw/8NrSWor0Bs0fFD4+ft0LNUxexsw0ra8zBrc91AtV42Zmu52SXjh+Y2IiTLR+yqoa3DATerCtox6X9QYPXtNQT3ufXA1H160+i78EPT++sAwTBo/HlmbfsHyPzZyzUXFsYtujygTqBPJbrJmmeRt0waoD3nrScVkBNP66lEzsc46nOL2+iTHYWgOLJDE6fXyTsmO9hCZmS7OAlCc1hbkNtdDy64v+KaIfA/EgmB8Bfu4M48YxEij1yioJlOhkq7JzvmrOzpTgZlTW/QXKlD8A47LhXaHFlOdGendpImwTSKbXqOTKissfD8LMGHNanf6wkz5K9L/eIip2HVCSV5cgYzxL997Ec2l2aizuHxmiYpjFt3+7XHbej8VUDiAJBZ85D7Ma7NO2zHyS+jwWSRiG7QHeF1hrzOrzeZkz8mkf3fB9+z7b9tXV2YE73SYKHQKSGHY124WurCj28AGD8ntxJoVv/mufaA2UnHMQP0GVXBo1WCTHgOV1CpU9DCopFahoodBJbUKFT0MKqlVqOhhUEmtQkUPg0pqFSp6GFRSq1DRw6CSWoWKHgaV1CpU9DCopFahoodBJbUKFT0MfyuphY5ruLspe2XbPbvrfv8TZAkerwytTtu+skryeHheFd1/kWqIZWyRvJIvAQRLlfwXPa6Kowt/E6kVnpheExQGjdEA2WWHx2bF4eUJOTTY8k6WyE/Q6rBPzj6IBjNfsuix247IvRj4+m9p7wDFb8lWfv0PqzVZEv/gqAScd+bJWLVkMSoaWnmetCnT/4UAdzWWrtzkS9V0CLCc5r0S++GKK65AkNCKd99/H7WtHmjVNEU9Hn8PqT0SQo4/A6nX38YX/1cvn4Oi776GojcdOFEfIyrjzT4ZUFg+MsW//tr3twRtTG+EDhiIpm1r4LU7+Tm+wgFA/HUPITjcgYzXXyKy+M9hyfVZUgaW1XMfCe67/v73bYPsAUJTNBh7lgZBgSy5n8KXUJZneLD5Z4mvFQfLxssuu29qMMm/TLx9uy8/2vSLrscVJ/fG8gXz+AFMSofF9se9l12H3elXobTeShL7IF8dexeNHlfdejfOG5+KLz7/ijX5QbKlqehJ6H5SyyyNRxgSr/w3XJlLkbvoV3isLTx7J/yZOjmReCUOkauiTKrDHAiNVgPJavGtx/ZLYzEghCSyCK+lxZd4weVGyJgz0e/i07EjbS3PaQ09Y43MEyZY0tfDpjT4FhKzRAReDxQigC4kFJKthWUr8GUqpedkSf7EgGDiJanDNgfdZ3/Ryx4vKEbApIv0KFjlQUmBxLOB2poF/g7sdQNC6UAiv52UEYHlaKBHYYKdHr3TdnaxsNg+uOC8qfjpk+dQ0dgKvdFE45WAlUvm4dJLpuPsqRPw/ve/4WBfHcvgotMHITGuF1Ys+AqzPv4SgcFBXeYnU9Hz0I0VOmSev7rXxXcjZtwJCEnpBbswDsmXRaN4zvuIu/kpCI27UfDtdwg78SIknHQ88j54DZHTb0RE/xQidQhMYQGonPcuypetgBgSg/iLbkHs6LFESiLRnrUope1Jl92B0L6DoQ3SY8Cj78BZtAv5H72NkGmXI+mUM0jVb0HJ12+RMJM4icyDJiDl8lsQEB0BT20hCj99Bc2Vzehz29MwhwZAFx4Lrd6D4k9fRl16JhF7nybzl+txWxWkL3Vj2wYZLCW5LAkwhAITrzJg+Hg6yC1g168ebPjZS2YHcPK1egweQ5qBS8D2RR5sW+KFiwaY/sPHoHeQBlt2ZqJNfxdpsGquK8O2XVmYPHkKvvxpOdx7MxXvB6/XDcntpWfQ8KQHJpNJrbjxD0I3SmqB90JLxhYYo+IRnBiFmtWLYa9rIDkYiKjx09C0PI0kp4LQIScgKCkGTC+NpO2hsRrkf/kJIk+7BglnXoCq1WuRdN0TSJgyHKXffwynVURQQiRkRxPqN65CUL+BsGZsQNWqdZBaayHTfZ1Fe9CYNwS9z5iGClJzWRkfXUx/DLzveaAhHcU//ozkqx9A0vkXw/bVXESccBrE+gyU/jIPCZffjbhTTkf9rrQDNhkbWCbfbMTQi+gIEsVrP3cjcJgWJ52nxerPXDDEa3DyrXrU5cowjtBi0plarPrUDTOp7tNu16OlWMGOLSL6JSfB3lKLmqbm9mSLLL8Y0ygKCspwzrmDERJgQJ29Taff5zmI7LEJvZHSbzjiY4OQs6LusDPHqOgZ6NYUwawLtm79A6ZBU+AiyVPx8zdwttgRNOxk6MwSWnPzSDU3w9w7CbainZA1oTBHh6H0qydQPPdnGAadDE1IC4xJ1GGnTkHJBw+ieNESUl11qCHxKMhuOC0Ckq+8DQ0bl6Fi4XzoSH2GXg9L5jYYU8bCbRkGW10tV78jJp0Dk9GOXW88hebCGgQfdwaCI6Pp+n1JY3ch591nUZVejPBTroRis/msA/iL9u33gkBNtoTSIoVbDa024LgxWlRs82DVl16IMRJSR5uQeryGtAMNSjd5sWq2F4YECf2ONyFlhIBtGwVo9IE04DggEYnbRHFbvjKnhWxps5k0AVIFbPb9RDXThiSSzuddfgOuveR86F21WLcp7bDyu6noOehmm5qMSWMEQvoNgruqkNRWLTRkK+vj+kOwNcJWWgLRSESOjUEzqZq6yGR6QAuaczKhD41BQHIiHHt2QIzsD8Vaicad26ExmPylLAVOrICkwdCbBFhLiiCYzDwJPjNsBbLZg/qPhFxXAndTIw0EBgT0TYW9KA22yjpoyMBlpWu8tbkwhidAtlTCUlYCQ2wSqeahqF5dQJfX8soaXUEgHTxnjRdb15H6Ta0qG3nyVDgaFJ6HXPGytOdk65p9uRXtLb7EgDQOsXTo0BpZCmUJFmsDDIGjabChA1tafdf2OwjDY6Jha2iE3ebskqjMSy5qZMz76kPs+vNPPP7kY5gyaQTSS5b/hd+piqMN3UtqSYImOAaBcbGwbVvNM3eKGrL5EmN59Q6vR0DY6KkIjAlEaUERTL0nwmtpgINUdDE4EWYiXVV+NkQhichMEis4BEqjk8ieCk9jFVz1DhiS+kNU3PA026EzBfhydWsN0BiDEdAnHvaKTaSO67nTiycXpGNEIn7giCmIGJCEgiVvQ58yjVfedLU6YRqYyBP72YsKeAncA4F5vbUkQHVGXw5Flta3pQ4YQlI5NMoDTTIjpYjcUgXuEGDgUAEh4TTG9RERFiEiq1rhxQSysnJoMLoMfeKiUVTVzK/N/O96UyCGDe6LvNwtaHZ6/FlXu3oOAU31tdi+ZStKShsRHR3hT4Os4p+Cbia1F7qIJBjDzKgr3EMSzHd7e3kJ9LHXYMQLn0EM6QW5uRL2yhqyswfAXZkHD+mypsGJpEW7Ya0sh622AtbaazH4qY9JcjXTdi+yXnqISE1kqi8ntT0Yg575GK27ViPvyy8Rf/VDiBzaD+aEZHgjAzDyhVTkvvk0mjatQuJDj+O4t36g50pAw8o5qNm6G/1PuR324t9Jiso0SPSG4mqArab+wAUFBHRK5s8d6/R5x88epD5mwHXvmCAECLAVS9izToK+TEH/J4y48T0TDVYimrM8SNsk0QCjQ1HGFmzJrsT0007CurQ8fknm5U8aNArjhiTj1f88D48k4wBVdTmYY03USvDCieCQEDIH1LnpfxK6t+g8SUypPh9Zz98NR1keqcDs9gqs23/DntfcMEUEwpqXTSRywNXcitoln6BeskLRGIjcmdj97D0kaWvhtbuR8dxdiBx3AkSDCMueP2El0mlIZbXuWoa0J/Jp4AiH1FpHmrcDDavnwrLdDNnpoB6vo04vw0M2sv3PpUh70Y7Qvn3gLMtE49ZN3CYtnfMi5JZqiAEBsKevQcbz2+CxOn2V6fdtQBKYDWRLz/mPE81lLEe4b7uGpHbVbi++e1TGgAki6DWQS8RtaiF1PF3Ct4840H+cAI9FQO5GL5obwWtdOUkzmfvjPDx689lIivsJJbUtYPVGpp5+OmpzN2PDzkw67hDBJ/ScbqcV27fvxN3XXIf3Q+Px7HMvorLJSaaBmqi/p6NbSc3mkWVHM0mmBp4c3xfoQbYlGZVNaxehiR+j8U2/0H5HWa7vRFLRJbK5W3Pq+WemOrvrClG5sG2/hm/n0WOKB3bSAmx8ykfk+6w5OzqVFWJg0Was6FXrtt9h+XM5n8Nm01WCINP5GeA+Z7qPt6kKrY1Kl1U2OdjUuFVBWYbCZ6A6VqxhpzQWy9hQ4FN/mWLiV05QXyijJtdnGnfcrjfosG3Nz3isYg8a7T5nGSs5u/bXb7Hqu1pY3Dhk8Tr23swDP3/2+yjK3IoQvQI7q9ihSux/BP6WZP6MPEqnbSLrzfxzJ1nYgUj8mI6dmUWQdVFGhl9Bo9vnOgeKexZ85G67R4fj27cdBhF4zv0D1Qnouuou396V0GSElDxupKfv7hD7raAgK8NfbeTwJC0zFdwuO9atXE4DmgCD0dBe6eNw0HEMPJTzXDnInHnHa6lO+O5Bj1ylxYuy81pZ/l7ES9p6+FRQl0EYsgSX203jivGoCNIQeHWQzir24cR7738dkchs6ryNGMbK4Gq04t5qJKx8r0fucB5gIvveoBd42VxWDthXnkjh9jyPH2+rFEj/GmlwdZPdL0u+v9kwyMoIMbDAHKOJVUcRYLF6Oj0LKxPU1tweFseqsPdWtYn/L7qV1DqS0B6v9y++i+KL9fbLXYUIGxQejSH9kpGRng6L09tJYjDPcGBoLMYN6I2cPbvQRPb60UDsvwLMBNHqtRg/KhKNVS0oqnbw5gqLDEDf5ABegpeZMJYWN6L7xGDyAD0a3BpkbCrBij8bMG5yIkYkmTBvcSGa7RJv49CoINx+9UD89E06siud0NJgwQrcB5n1/J5eGhDGTO6Ns48Pw6wP0tDoVHwF7+lcp1OGxOLu6a/BQ6Jhghd7cprBrtxDv4JuQbeS2mA0wmuz8UJ2fwVxWNSVLiwBD957B9Yuno0/NmbQfSQMHjQCLzz1b9x6/TWoL2rgUrDNLvW6XdSBR+P55+/FY7dehQ05VXw/I7vMpA/Ay+0erJSuL1ad+6l9ZYC5kSy0LxTxTSkJe/0INNAw6djWBApfj+Lbx8NpWZVPgE/3HcklokyS6oMC8NjD4/HHj9swa24ZF6XhsYE4+8xUiPRZR4QrK2lCozYA0SHAtl0WXHn5QOzJ+xP1DS5MvnE4RgyKQE6VC8nxJiKxFqOGRSIx2gCrS0F1aSNm/1qJe+4Yhd4xBiiSF6JOj6ReJjwXE0yNKfLifS6LHW+9uQ2Z1S7uCLzy2lFIUFpw22Ob+d88AJEaxkvtxyuUqv6Aw0b3qt9d1YE9YpdWEBwejuTBQ3Hy1GloLdmJ4hoHmuur+D5GrpheKYhMHoaqsnwUllZzIsXGJcHorsYLLzyPvBor76TsWFNgCAYOHIRAg4jS4kKUV9Wiq9le1vE0gaHQGnQQzaEwRkfAVpgNZ0MTBFMAzNG9oI+Og2xrgK0oD5JLgiEyFjrSHgTFC4mklT7YCEt+JiS7E2JwFEL6DwEkG6y5e+B1uLo0ypl8c0PeLxSGlR7UHaS0LhtMeUVMIonkVRAZF4TBqUHIL2iiQYxFpPmqhw4aHYyoUAnRgTY46HqpyYEoqLbhvU/SMCglEHV1DjTWG2AOMaJ3Ep2f1YDKVgnWVjtcVie++jId/QdF4d/XD8SSnzIxY3MdTjh7AC6dEoWvvkjD7kIbKpq9fPEb09QZcTUdBjDWriyGICEyHA6bBfVNzThSS3N7OnqETc1tPeqQk6b/C3dcewUiAo04/9Ibcco5l+Pzt55FhtUBbVAcHntqBnQBIfC2VuGB++7GjuxqnHXJtbjsvOnQOBvw4F23oYrIGBTRC4/PeBEThiXBaifiWStw+10P0D7bfiudZLcTkefegr4XXACP1crJ6inegfRn7oVpzNkYcMP1UBxWiDRI2NJ+R/7X36Dfw28jJD6C15hm68h1ISEo/+IZVO4oRf97n0VwbBiferNnrEX2h6/BbXV2WvrJCG2CAScrUTBxRdZHbUboCrEVO0niHWihJdMQbGRiMFuZaRDGAC0G9A2DWSfAZNYh0KhBY7MLUWYNQqKMtC8UNosXerMWU6cn46wxwZj5yjZ4AwNxVmooAoMN0JP0DQ03w6V104DZROq7Cw31dqTtqYPGoMcN5/VFXEoE+g8Ixacf7cBXi8r4yjOjUYu2FaROhwd27DXNvB4n+k08B7Pp+9u64nvc+9gL8AraHmsaHUn0CFIzFZXZcqsX/YjszDy89coMLJr9Dn5a+ifsrY1IGT0ZBrMRs199F0vTy/HZ559h+tQJ2JY9D/PnfEhSqg4vP34ddTINr2kd33cYTpkyFm8/+W/8vG4PUnsnwOb0dLmkmhFDNBhhIGLmv/EgnPpeGP6fpxBx3AjUZ29G7lsF8LS2wDRoEvpfcx3C0naTVDegYt77MI2+FFL+UrgChiN41BTohkQilFTWrLcfhWxIxZAHH0FCQRryf5gHsYPDi1XTNgo0cEnJiKaO7hV8pDaQQbxWKsVOkU0O7i/dmWPK3WrDzOc3oqXBDqNJh7rSZm7rRgQRiWPCcMWZMXjsmc0YMbE/HrwuGa+8tAl1Dt8UvTnDgr69x+CCs1OQ3WzA8cMCsXZnM7eL6xvtGDQqCb0jNMgsduLkk+KRkhCE6CgzaAwhu93Eo4THk309YFgcmoj42zdV4E+yoXUaGV99vh1GOkDu2Mjc2SmqRP4v0SNIzcC+eGsLqYAVlfCQDtlQX4fS0lLo9RoSejo4myuxdvNG5Fa6UVxZC53RzJXU5voalNfU8nMYN5j63VBVioKSGtx4z6MYf9JuLF70E/aQGsw6mELHuT1uIoiuPVGBIGjgqM5Hy57t8ARZ4Gxs5bHlMIag13k3wxAVwhMiMI+zLiCUbFsXXOWFEJIq4KHnlUJ6QRsfQ1IyDoIhGIlX3sdj1Uk3hyY0wm9foj2Li5ae3KJY8ZK4E7pObQDYBCbtxC6lNNvP0htlZDVyScm0Dons7NQRcbhxahQWrKzFgCFxmPHYeJTVuKHQOyZEGlBb5uKDps3iwOdf78HAeDPCE2KQsbMKC5ZVY9L4GPy2OB8NmgAMCyMtIsSAAf3IICftSfQ6MWPGdhRUOZDQOwz33zECwWSCcA+/QfQtc9coKC1p4Z5ync737Bq9EUXbVuC8c7fBY7dCErVqkofDRI8hNYNGo4feaCDbzNcxmKoJxUd4r9PNt+n5ai6fDc5sfG+bUcpUeCIr87w2Vubh33fdihMnTcKkE6fixdfegPv2q7FiSz6S+wzElBPGoqogE1u2p8Ppv77idPgCZ9gct+SlvqpD0qV3IChGj5y3n4E3NAVD737It5+BBbqIviAbhSQoj1EnKcVDW7//mtRWklteD7zWJt7BO6Zl8tBThgkheFYeiTgisMfvqzDSe69UivCqmA+fMr4/2HX2nTZiU1SMTAr3SHtQTrZzBknQ4WNiODl3V9TyAZDNFI4dRyr4iACs2u3gtrlRp+H/shGDJ2fQalCWU4+nZ9SiV0oUXntiOBweL7xE8IYGN0KCdZj3cTaW7SIzh1R/jc73LHyKreND0Xen0ZsQ16sXaVsNaGpthXSI+XAVPvQoUrMvnJNXa8TkSSciv9KJsuJcnmZEy4I2eI8g6aHT+CK5dCYMGzIA/Qf1homIM3DwKDTLefBqgzBycAq2rv8dlaRWTjr+SUQHBcJJqnmfYSfguWefwZ9LP8eOtHTYqaMzldEXjeZ/DkZu+lsTGACppQrOpkZETb4SpohQcCkq+p+Fp09iASV6srstaC7NQfyYkQgIWwhrkwNhQ4+Do2AnWurqfatE/GCS2qE4MFvI4Ta17L8vo0eVYGV+9sOSaXyqmcjj9Mjcvtcwr7TNiaxCCyIDdSQ97Rg7NhaIDoenthWL1tfj9BPjsPP3LFiEcGiC/DMINDIOGRaN4QPDoDTUcyufDZapgyOhp5HA45C46cI0AzZ4sQUyRr14kGAYGoQ9LiRSW3/2/kvYveVX3HTHgzToKoeMplPRw0jNIsns9SX49rsfcOX5p+K5YePx6VszsLOhBUUlJTxwgsmjyrJSVNXWISAiAXfe9x8kRAWjltT1C2+4E+Py0vHjwhW48JrbcMedWh7FtWnZj1i5PRcmgxa2lkYUlRajpLyGSw7WWb0tdXBUlfuc+yRdHdXlfFvV0u8QcvPdGPnKF3C3NKM1N5Ns2no6thSSzQ5vXRUkSytkXR089W6Uf78QhtAn0O+BNyCz7KGeFhR/kMnV0o5dmamhDriwUqjYvwlon/Yg3u+OYNIzOj4YJ4+LJbU7CtdSO8RGm3DbNYOx8Y8CLF1RiEceHINbJ2gw+9PtGDKmF1JIq561uRaxQ82ooYEF3Gst8vM1Ljt+W1VGKoMWp5DtfNf1A7D51wzUtvq83Gyk0THJfhjilr1zaHAQAoxGOK0WnpZKPFDYnopO6HGtpBFlfP/5O1j8w2c81tntcsFDPeSOux+Gh2U7oWNefupB0pC9kGj7ow/cydVniSQKW83EprNcTifSb7keSUkJkF025Obl88R9LDorY+syXHD+Sn6+SyKZaApAw4rv0PIHSUxJC8VajuwX72ET4PTfbqQV74EhPBSO8gIiKYuaklG7cSUnP7JyeXAMhE2oJ6nltdO9Xr0X5uR+pFkocFSWwEvkF/X7R5MxYhu6cIb9N2Dz1uFRQUgM02DthnLkFTTT4NeMgiIrmq0eni/xu0XFuGhSODbvbETKuN5Y/XsxSmtdKF6bjy307OFxoWggrWLR/CxkVjn5TEQwbbvg7N7YTcd8tbDYL5F904rVpNq3OjwHdX6JzGFGBD5u1Ch4rNVYvGA+nC4ZBpOqex8OehypmSecqXkOu923wd95HA5vewCDw+Hwe1YBm62LVMG0o6WpHml11VxSsxjstqksD5GR2d6cVqLPdSPQ317FL7ZZ9hGyrwV/jLurphjuKpkv52L2LFOMmRTmwSn+IBPW4SV/HDrL3mInbYGDzU//hUEXTA0uyKnBU89W8ylBpoIz+5jZ18zGFemdli/MxJolGrhoQCpZkos1dJ6X2c9e36x9U40FL766DVaLxxdNRvvsDVY8++x62ubibe4jNX0nFgdefGUbtbmLL1I5ENiVDTSQbf5jPnLXz8WGTbuhN+r/snboaehxpG7DfhFIQlsaos7RSQey61gCfE0XQR9cwuwjZZRO2wRO2Db/W8cFI+2JkDqkKWrb0/aRL1w5SIc/slC484urxXrNfk4o7gCkH4dL8nnKvb5gFz6Y+ZKb88GgkSS1qO089WSxunlwT6dr0qDR2Nh27MGey3f9HRvXcm2KRfgdzrSWr+CBsDd9chdFEQ4NhTQsL7xs7b9e32UfONrRI0nN0wez3tphtRXP1cu8N12osgwsxNS3aut/bxI2bSX53elsbfT/ksy/O8Dbx+PyrcdgIa0HWSwicM3H/4e4/6QSXyWr7TgIKTzDjVbU7FdIQaEG0iikMUHP470PBbaI5XCbUJJkRMUlIkivoKS8ig+05sBQpEYE098V/Ks/HFozx2FcYgqGDOyDkvwMFJXV/qXa0l+BHkdqZtOJhgBoQkIgNdTyOGqZRt2godMQO3Ekyr77EE6rsz01ka9IgIDI6VcjKNCD4vlzO32JPH77MEZ5RuiIviz/twHBgQJ2LPRgzxaJJ0s46HkHmKY51HLG/xnMhjcGI+bMGxA1+ji4S9NQPG823FbXQTvvgdqh43bfZxG66Dgo9lZeBaVNQrJB09x/HBJPPw3l8z6CraqufQA9WCmkw2l/fu2wJMx4+Q3krfwGr33+E8/+EhCeiOdfn4nZbz6FRWt27bfybV+wdQCpIybh1ednIhAWvPv688gvrjrmMsf0KFIzgnpbLQg99Vz0v/wCpD92E9z1dk7g4DEnIuK4FBR9aScp5eHSgq/rpi9SkrQwxyRCK5f42Mm8xzQQcOlNkkxmc8hsTfaBVDGPTwk44XojeoUoyFjvhbVZ5pfiSQUNvuARZopreNJ+5nn25TXj6r+CdvKzBIUsIIRtZ+tA2PHCAfpUV5H0B+3+9E7e1hbEnnEr+l5xCepWLYaVzQo4nJDdbn/UGpHI5eTBMwJPpez2XZQluFDI1tb5FpnwIghssQZrH9KCRK0eXqcdmohkDHr8bdT9+DLKV6yGGBjEZxzYQh5tUASMMVE0YLnal3IqHickv7de5KYHC7phnn+3L8mFoOVTduJBtAmXx4tpp5+N4cnB+GD1BnoWlt1GQWVxDnIrrbiS3nXFhl3wHKJ9vB4JA4eMQkKogjtvuQvbs6v+pyWvfzd6DqlJAgkh0YiZch6iJp6NgKgYxJ3yL9grS1G3dSsCYhMgW+2IOftaUhdl1K9eAkdNPcxDJiI0NQVSVQbK0zb5MqDQtcTASIQefxKCk5MgWRvRuHklrGVl+y2uYMSN7C8iZaQGKYNFVG52o7EKcNiA6AEioqKA/O0yZJOAQRNF1OXIEIMFRMeR7RciICaO9m+SUbRH5j3OECZg8BQtInsJaCpVkLOBLZLYZ04LPkKzEBd5n60aOrCrlBACEU8XnYLYacchetp0KNZaWIvz0Jy5C/qoFASnJKNxxwZeACB88lQ4i9LhcusQMWgwBH0Az+RqzdyChm1beVZFbUQvRE04BSYiqau6EPWb1sLYewpCB41GSEISPCMmgnbSNdeTBBQQN/V87kgr/+lL2OssfKBljrnAoZMRedxYIrcFjZt+p0GmDPreQxGc2AtiUCTMUWFo3rkGzXsyOptTHb53jT4Ip508DYW7NiKjpNaf7kmB5LZg+e9/4IV7r8DglDhsz6/lTsADgSkMWhpd3TQ4Nbe08LY9Si2og6LHkJrZ0FpzEMJGjkfEyMFwN5cjoP9x0BhFNGVmwdQrFobYAIQ12hAy+kSExIZi9+uvwhiXjKiTLkF4vwSkPX4VHJWVUAzBSL19BiIHxKFp106EDD4Ogq0OlqKi/aQ102ZNUQKSh7GACgERyVoM1iqw18oIH6fDpAkCireTJCQin36XAWvfckLTT4MLbjageAuJ5WARo6YBs++1o546/yXPGxEdChSkyUg5R4TUomDraolnKW0DI3OEEoIHMADhrCiQX2ST7oEtQjm+EEjj2CeijFUkEUOjEDruZCJwPNwlexBG2ouLBj390HOQNHUwmrevooFxKAbe8yzyXroBuohxGProE2jZ8jskYxSSTj8Lux64AnZ3KIY+9SYMOiea8gupzcfyPO7ahEGInHACBMkKMSwRocND0JKxGZKgQ8iwSeg15VTUr3ifiL4NbJQKP/V6DL7lZjrmTxiThiFu4iRsf/h2xJx+Nfpfch7q1y2DNnEoYidPws4Hb4LLsr+JIJMtHRwZiYF9ovH7nF1wtydlJF1MKyCbBgOHYsbIASnYmlNBmoDhQD2Ia2MsUSO7Ayt4eKxGr/UYUguk/nmq8pH78VsIGDAC1tXfIWf2d3wRgz5hFBEvHJVzX0beN/MxYMZsBIVHQqvX8DlmVgcnIO5iOGrr+eCgCwymgWEUbDvnoeirj+F1uEkakPwzGNrDS9syqzC1uXyzhCqStNe/LyLzNzdWz/NydXvCRFJVpb2dkPnqJL/DxlYl4adnnECiiFteMiA8QUBgnBbJiRp896ANOXsUekZfMgHdPnY5zywieJEvWxAGX/09BuZWqobzAO1jgCNnCwo+b6VBajjZte+jYs1GKKIRA/51P9zl+XBb7AgcPgCiZCMNpw5hxw/lK84yX7wXQtxEjJr5NLVBABL+9W+YgzzY+dAtsFc3QBcWyePU3Zu3UVPGIW6QCdkvP0zavsBDYNmUX8HnbyJ02CjSDopJdfdCE90fKZdfRwPGAux+6TmETr4WIx66E8aE3qQV9EXL9t+Q9uy/ifh3YfDVZ1M7s1pr+78bG88M+kCYiMAtLQ0+lb2tnYiklsZGWF1e0oyi9stTt/d78SKhzzDcc/9dmDR2FNbN+wyVtdZDJ3g8StFjSM1tQUmCMToehiAjasrL2qeujDHx0CgW1G1aB8EcTCpdBKzpa3x2raiHOak/PE2V8FpILSQGea2tqP59BRJOOx/HvT6FPn+P8gVz/U4boK1wQNsii44zWoJvRqtdLWYqZvsTdsjVZalVYCEVXWMhglt9U2ARvUS0VntRlq9wO9xp9Z+w7+wcm0qinzShDszybVtVzWRznWhnidW6XtBBhxmikqCRLLBV1/qe2xwDc3QUbFt+I3VVRmBKH2qHWrjsXiJXElrS1hFxa0kC94Via4DHZUbYkEGoXzUH9qoaCMYAX2FBdn0ifFBKKhwVf9K1FH9BQYEPlMaIeOgNIpwVRXwajRVWMAQCpSsW83Xc7DjJ7SSNhL6f6GA0LFtFdrgb5tTepHXV8NVlB7KIJdkN5iUxGAI6EZfdVx8QAD0NLPZWO/dhdAXmv3DYWpG+axdSknsjjCS/3qCF23vAWx7V6EGk9n2JhuQhEL12WLJz/KVvtTAmD4JEpHXW1pEdOxCm8CA05mfwziSQFAzqlwpX8RY4WyzQmoLoi/Si9NOnULkgBrFnX4++V96Fxg2r0FhYjuGTTseD99yAPWsW472vfuRRZQdbPaQPFLnji/oWTAE+YrOwSsXj9z91GBCspGoHhpJNS3Z1aYXCK3ywKVev1PmaXiJxpBCIe+XhiKWv0OtP1q+nQewPuRAvC3ncuu7qqUx9hsNTXwZnTS1XXc29EmEKC0R1ThbdLBRhw0fDVZEJRReFILKXa9dQO9HQEZw6EHJDKTxukUwaE9w1Fb5iDDq29JTVGHdADIlCQK9eqNuYTgR1QKMJ5PYJc7aZeiXx/OktRaVguoU2OAAikdHV1ACZBtbIk06Cp7oAHk0EDEYBtvxc+m6CEZyUCmflTnidTija/Usds2CZVrY6r96GgSl9afzb21heGrWTUnojmEyXrILSvSlb9wGLxW+sLcGsV15ECw1aj95wMqLDTWiuslP7H1ueb4YeRWoGrdEIXXAk4i++DYG56ahZvYqkwkC46kvgsroQNCSVyCLCWtWEqNMuQ0hKCiKI1A5tI5IuvQ51q1Yg7JQrENYrGM1ZOQhIHQB7cSZfE83mWSOik3HCuBNgbi3ER3MAl3fv3BMrYdvmy2HxzQ2lCkyxAs64XQ9DkhaRUQKXFiLZ3BrT3gAUlkhVr1eQu1aC9UIdznvcgO2rJCQMFVG40oud64gEHWxqltmkSWnB/ZpN0O4jfJwCU/27du8oghYhgwZRWxTCwyLumEbBguB0JkRNuwgB469G3LjRKP/sR1KDU4nsJtjKSyGSdhPYvz+cVavgqSuCncyU2H/dBo82BqbUEWSfb0bJvLnQsrhuInjkCeexot2oX/0rhMi+CB8+DCEjJkNvDkCvf11LtvsGOEpLoehD0fvimxBuNyN+3HAUvPkADL2GQyu6SDuohDY8DkG9E9C45Cc+AIldaMOsqonT2ogNm7fjiskTER30MRqcMp8xkKgdxpOdbq8rQHpuEXQHm48nwpvNRl4xlA0GLGrQQ6OpSuq/GaxQnmXrcpTEh3GJYW6u5lMutrxdcDT5KoIo9mZU/fIt7M0WRI/th4D4KNRv+I2P4sG9+6Je+zvcjTUwTpiIuL7D4a0pQs67n/EUPYJej4rSbPy0cB5ytm2Gl821tIkOkrwZy72oKpR9ebypL5Ru9GJjPw0GjtKiKlfG+u9kNNSSRM6Wsdvu83bLNgW7lktorCeJUyJh7ktOnEDEHnOWBq2VChpZOZ4uOMpU7sYubEw2SnStNzBHkA727O2w1e7kDj6RVAFXaSbK53+L6InHQ1eci4oFX6B26w66TCxqfvsRtopKvgTSsnMlXPnrSLtpRuknryLh0qsRc9oFvCJK44osn0+jqQpFX7+P2OOPQxCpsY30fejDYhHSZwDkpjLUbCkhzaAP7CV5aPrjDxTM/hSxJ01FmLsFhR/PRPnajQifEIMKIrGzqRWiKQQNaxaicdd2fv0u34r5NUQZy5csxoVnvowzp43H5wvX8OSGEfF9ccaJY/HH3FmobnUfcp6ahS7U1JRDE9wLN996B779YQGyC0t9q+qOIfQoUjM2eZqKUUwdxFdTzhctVb3wA3BL1GiGPW8LcrM28eog5V+/iFK586SQoDfCuWoumtYt5Pa17LD5CtTRdXT05ebv2YQH7l1Lt9Lwkd9vXsNLNuSqD11cUotaH60ku4KV7zmxntRot93nKefz0YVeFLZ9blaw/D3feWyauGIrEXunBHoMkAbrS456gL743yUNELhZUTH/Pd+ZfieQ6LWi/Ie3ULnQyNeEy/5EgYJQjNyctdQGRhbcjtKvXuPrxUWyoa15m5D1wlb6zM7xVwNl58CN+mVfoY5+uetBZ4CtagEa1/3YaU6dDS5s+WvNwo/o2Dl8Ml9yufgg07R5ARo2yNDQuYq1ArkfPM/nwIWDOK201FilmX/ipZdeQbDky1bKHBEmswEL57yHZb8s8y29PQR09AWkb/wdL74agBNJc0iIDUVmfjGRXSX13wu2ltlg9Ke79Uc68cglf+Q165h63zpANvrv+3Xxc9jxLOMndfJ9M3qyWGDRKHYZ7sW81J1CI/2HeZw8hoLbx+3ZS8S9wSNt5/F5UUZ02U/orm/z/8Letmh7X3ofjcLDRvkacK0/uIQdpTPubUP2kG0PQ4OZyCLxnPa9a8Pb4uoNJr4QxHdtH7nEfUjRdn3WICzHW9t5fBu1N8vK4ruC6E8QcahGEKCnd1i3fDG/l+gfABoq8vHlN9lEcu1hZSPlhRRcViz8cTYWzRP4tY5FD3jPIzWHsE/c8X4Ry/z/B+4sAtp03i6jtvY5T+g0VbLPPvanv093rkrS9WcO8QBOV5mlUvIeuChB2/X8z9P1McJ++30LUjT7vWvH9tm3rXwVU7pun/2PPXQ7d9rWVnyBDSSHWVWEq+H7EVA4qB3dJYj8umMsLHRf9ChSsxhdSe4qke9fCy7xzWb4QiwdpIp7DnnOAa/FvMUs17VG14nsbC41OCoBZ506CSt/W4raZpsvlJSFfrKVTB06r4np8YIMp9O9//XZmhbaryNJa3Pvv//vBpvBCAyPxfknT8bmNctQUdeqZjv5L9FjSM0S7hvJxrN2tT76CMKXoF/yBWSzEd3tgnHQZPS/9XaYYiLITnwPhXN/IMFn2ktKyT/h2SEaba909yf8Z2ojEU0bk4Kg5ES07NpEqqCXe294CmQaq8685AZcPrEXli9a6LssXTcmeSCGpkRh04ZNsNNBbFC7/ZHHkSCV4tHnZkEhfZ7Z/9zGpes7PCLueeYl9JMLcN8zb8DlrzvGpDdb/MIWQvgqnBy8DfiTt9W9bpe2Co0lCt/eXuiQbVN8ZGUqcFthg7bIMF/xAtn3nqxNWVkgl4RJ0y/BsDg9nnnrS9q3Nwrs4FqICoYeQ+oDRQsdSbD4abaiS2MKJMnpIqns5va3q3I38j56CclX3QdjRDg/lnVd0V9tQzAG8flT2WGHovU711jnps6skJRn03ASSXjZ5YS5/0T0v/ZC7HiAlc+1EV9MvEpFWGwqzpo+BUvnvILaFjt0BgM8NheGjz8F/7nmRFy8dTNabB4eUx0eFYVwZxN3HJrMRjjsDm4ry/Atf8xK344msRayfyklGxwUesLAwCA+38wSBWoOsgSVD2osoYLRzDUC2eXyVR0lbYI5x7R6Hc/i4lsX7ctLxhyQClukwaJqFC8PyuHtKWihDQzmDkmmjTC73tJQicW/LsVTN52DpG/no6zJ2Z4CiQUYcSeoRnvMhnH+1egxpP7LQTaeYeBE9LnsWpgiw0n4utC0YRHKFi2AZGtAa3o1nDUNMKJtGSJ1Pn0gep1/LWJPPAkawYu61dRBf57Hq2DEnnc7wlNiIQRFI6BXNFq2r4JHDEL4cZOgD4vA4EdmwdtcjZI5b6KxsAJDj5uIvmFavLRlFydhQEA0Hn7qOYwfOxphkUF4692P0VhVjLfefA0WmwNJg4/DOx99jt6xIfhhzqeYM28xAsJ6Y8ZjDyEq2IAdq37lXmuJiBWT2B933nUXhqX2guRx4df5c/DZD0ug1XWuHsqXqYp6JF3/AF0rAPpefUn58KDsm1mo2bINcRffhdgTJvKaaa66Enr2dyAHpCL50suhDwyk9qmCIToB3upMZL/zAjRRo5B89c0ISoyHt6YQJd98gKbcPGhFGbt3boISeCMmjBiKouWboGerw3Rm3P7AwxjdOwSvvjgTWWWNvmJ9KjpBJfVhg1Rj6piOihzUrcqAse/xSLr0HthLs1C7ZTdP6K8w9drrO1Z2exF7/g00CFyI8rkfwS1HoTd1eqmpCsVLV8HUbzTip49H+cKvULl7M3RmLWzFe0j6hcMUNBwNfxLJGxvgsrFkBhr0S02Fraka1U0tPPuoTGr/5vVroDOFIGJMKtas/AP19TVotrl5lFVcfG8sW/oxWgdPws233oLVq9eivLUV69Ztwo0334mpE6swZ+7PsHo1OP+q2zB1dApefOkN0jQSYCbpqdnr0O4MEo8hoyYjNFKLgjmfIfL0q5B82XVo2L2bWxfN63+Bpb4FCRfcij5X34TybaUI6ZOKus2bEXfy6ahZswShI09A6PBxiL34ARjFOpR8+xEiT7sW/e94CLsevwtKqwdNdQ2oanFicP8kCMvW+yLkSDqPGTcZU4ZF4vP3XvWF4B5bs03dApXUhwk2T2rL3ooGUi1D+wwg8jF1luz42ERSsXd2TlvEVEtjICKOn0gS3g7BHAa9oicpZ0LYceNQ8ttKbme2ZmxE3gcvE3HdpIKbIDktcCrRiBqWjOrl38NRbyOym/lgYTCQGu6ycynNVoqxOOklC+ZBCUrCxAGh+P6Hr1Hf7ORquVGvR07aBrzxxpsYeEolJr1IkjUkCK6qcsz74TuMPvFsDNcztso896jAK5wYEWQ2Ie3PdcgrLfWtHxd8trDMEk+IPruc+wm8RLpNy4iM78Gtj0Hfsybzufm6dUsRNW4Kgnv3gexxwhgeT89TC1d5HuqWL+LRbNVLFkMfPxRBI09GaHI8Wnbnw5SQxNeqmocNgSkuBs5WK2SnC076DQgJ8Q0sPP+zGwu+/xIZq0woZwsuVCndJVRSHwaY2il5JCRefid6n3MaalcuhL25mWfj1GhNvjlx+J03bH7bS79GgaSoEe7aKriok4o6F0q+fwf24nTfXDH1R1djHZfoGhYYDpYQQc9rT/H0hGR7iloPnzpiSzZabE0wBg7k+ckVsrXZ6ifmGDQamBNJ4EQ26OV2ydrcWE/qqo6nAfZIvlVjDIz0OlZAgL0T2fQ6jYLvPn4NovM6XHz1LbivVyyWL/oSz73yPjyyDuGR0QgOMKCxrg4Wu29Omdnl7sZa0k7MNNB4+QCjCe2NQQ+9Bp1ci8r1q+G2WmGK0HMnGp+X5jNVHr6AhocCBAdQOznhrKzibdCatxHNOxfD0ehbHKIPDEAo/eZV1vJ0wbw6iuzGrz99jSV+Y1pzmNNd/zSopD5caPQIGjQcrrwNyJ71HEImXIyUS437rKASuM2oCw7hRdRZBzWHuVG/9Gs4bWSTR8dDkByAPzkhS8wHv8d3b11bulVACPRBIXC3+MJAmUDKyMyG7rrzkBgdgfIGa/sdmRQNCQlFOEniZodEQtTLSST648061qJigTNs7pep5yzaTk/SX1K0MJKS8fUHb+DDdzV46Pm3cPbJUzHrnY9R2Sri1vueweVnjMVzj9yBr3/ZxFO8dZx35oElbC17XCqMMaEoeO0RVG3YjQFPT6EBz+ALZGufDxd9K8qYzV1dw80Kd2UGShYsIpKHQxceCclq5/nZE+LjERmiQVpegS+kjs0QkE39wOMzceKweMx8+hFsTiviecRVdEaPIvVf5wFnYsaDlqydiDhnOoY9/Q6MiUNJErP6y75pHVaWtiltI+JuuQVDZySjfv3PqP75K4Te/Sj9/T6sNU0ISu2Lyrlvo+y3P/g191MeSeV1lWTyaLIB970Ia0kOyn6gcyvcKNyzFXtKW3DSCeOwOavId09ie2HObjR7L8KLL7+B3Ow9+OD9d+GWOmdKYSR2kjQcc+J5uObC0zCE1PsQJRyvvPY6Fs/9AfHHn4mpIxJQUF6H0SP6YPumX9Bq9/IsIGZzMIwB4dDrmQbRFufVYWkZfKaJVFcEW1U9Uq75D9nHLQg//nh4SncB/sygbemR+WvSwOLK34byNVFIvPJBmAafCF1kAqkuDch++VFu1oweO5mkeB527Mn3OclYyiRqnwEDBmPQ0ATSWHQ80ykvB/RXfOXHMNpJLQj7RxodSfzV12f4q0jti1YSUTVvFuwF6QhOjUf17wt48gR3fSVPnsB6buPaH7CrMhOmqEh4akthyclE2pOliBgzCTpWInYjkSVjF7Q0GFT98CrqRQ8LXN7bHhodnCU7kf7UrQhK7E3qqQNekvBsntlSX46vv/kRD197Dr79eRkqGn2L+AvT1uKWm29G/5Qkeh4rrC4ZP370JgIFF6nyZlTlbseD9z+CapLuLl0ufv3Vgfk/fc/pYKLnKC4rRVrZHNSVjEGv6FAe8LF+wyZ4iFhajRefv/cCfpsbjILcTE5skQa34g+fIYlaB9EUCMufi5BTuBaushxkv3I/IsefDFFqQeWCT0F6OZwtNtjSA+CoqkL+O8/BUVGG/Hcfh6uyAK4//0TL9skIHTgAltx0WLN3wEUqflTSAJx12mT88PVb3FnGFmKwVMFhodFIio9DzpaVSM8q5HW7VELvjx4lqf9KcNvW40TLxl/RsgF7vcIdEu6zmGdrzg7YsuHbxiRSRR6qyvgGfo6i9cUhO4sz4VCwX0pihfa5KvKJJPk+6cYyD9I2PUtuv+JHPFK0DS1Ob7ukZNKvrDAHJfk5/G82DdWSl8VT8LK5ZoelAVu31fK54+qSXJQXZne6HzcBiBplhbnt29jiB1+stEJk3oO8bIVXA+URbPSOrTlpPrWetnkby9FcV8Y/e6qLUPVTPtoyJSr+7DDOGoXfpzkrnf/bmrXDF+NN12/Z+jta/vy9/d2ZOu9xNOHtFx5DcX4uz9nNQa8bGGhGQcZm/DrnEzRY3f99COg/BD2M1Ep7xNJfoQ0cKtE+78T7xB/7SLu3mdufStNVesC2fTo+VdM2q8TPow7Pisbt2bPHnyR/b9w2k9gdLcuOAwUjX3uVS2ZTd5kRVdw3n+LeR2GLPPbZ1vEd2YKQ9hJXbKmZZv93bZ8dY4tFOpzPc393aM+2453WFnrPxk7vyd6xsnA37rz1Zn5PldAHRo8hNQuPZKliw0JD4bbbYXW4uNrak8Bzov0/ig0cKzjYe/qm2lSv98HQY3oIW0QRHNcHTz/zFHqZPPjyw/exaM0WdUTvURDU0NDDQI8hNbMD7fVlePPVl/HojFdwzZUXYxmRWvIvJFCh4p+CHkNq5kzyuJ3Ys3MrdueVYnKsLwGCdCymg1Sh4v+BnkNq+JxCJoORr6vWaUQ4ieQu0QCzSS2DquKfgx5Fag5BxtZVa3D2g9fhmaefxKpVK7F2yw6I/wAHkwoVDD2upzPruam+CqI5BGOOH4P8rHS+9leFin8KehypZUXA5OnnwFOdhRtvuAnVFjcPvFCh4p+CHkdqryzBHGRGS3M9mpud0PSwuWoVKg6FHkNqFr6o0xuQktQX/VPjITdn8LrGB8jLqUJFj0UnUh/LkTqSx42whH54euYLSDDZ8eXni+BW1DW3Kv556DGSmi3na60uxhP33Q6304bmFqtqS6v4R6JbSS2xwmMuN2RF9i1COILpaJiWIXk9qK6u5iuYdLoeM16pUPFfodt6PktQ71IEjDthCkS3FRlZWbA53Ec0hJMR+1BF0FSo6OnoVlLr9WacOP08nDN1Arat+AmPzHyDV44UVLtXhYojhm4jNcuP5bE14fWZj6PF9SIunTgBQXoDGpzuY66qoAoVRzO63fB02iyob2qGxxML2ZckW4UKFUcQ3U5qNsVkszhgNgUjxByAWltze60nFSpU/P/R7aRmua7S1q5A3aVn4d1PP8Nvv8zHx59/D69KbBUqjgi6ndQs4WdQWDgCjRpkpGcgt7AYsiCohFah4gih20ntlbwYOu4E6Fy1eG7GDFS0uhBoNnX3Y6hQ0WPRraTmdZbdbp4918OSs9PtTXp1WaQKFUcS3UZqlrpXawzE2Wf8C+efegIcTXlwsWLsav4wFSqOKLpPUpOUFjR6DB48GIU7VmLxgvmweWVeSkWFChVHDt3GKEHUwGtrxnuvPwdFksDKPanpe1WoOPLoVjGp+Ascs4TsumN4macKFUczul33PZbXbKtQcSxANWhVqOhhUEmtQkUPg0pqFSp6GFRSq1DRw6CSWoWKHgaV1CpU9DCopFahoodBJbUKFT0MKqlVqOhhUEmtQkUPg0pqFSp6GP4RpGZrub1eGVqdtsu0Sb79Eu3XHVNplVhRQJ4fqiNYaqj/Mb6erZ4T+FLYvddkiS1YRRVBTeN8zKDHk1qRZQSGhqNPYhwK8vJgc3dOS8yIERAchQGpCSjIyUSL3XVEq4b8VeBVPrU66PU6iP7nZVR2eVxwuT34b7O+uZxuTD3/Spw+Kh6vvTYLLW4a5AxBuP3u+5C/cTEWr97Cq4qqOPrRzaRWWKkOkiQilDZpIkv0WQTrlgp9JrHA9wla36MxScE6MF+2ySQJE06070DSiB0rebxc1rDMpR63C0lDRuGNJ+7Erddfi4wSKwwGfTtxvW4nYvoej9dfuhf/ufUKbMytps57ZEit+CUe+z+9JTW22E41ts/r36+F2L51XzLK/m37vq2X3nH0yZfgvpsuglZkA5UAAwnThT/NxqdzfibCa+GVZCK8AFG7V0Nh0rhtu8bfxorkhSk0CjfddAMq1/+AVhrYQFqLy2ZBi1OPm268Flt2pKPR7t074NH3KFFbiyTB1YV3Rxe6L0kC6wCk2mmCgyDbWiGRussfIDQS8DjhdXlgiEmEITIW3sYKOKoqwGUPdSJ9QDBkjxv62GTqiDIcZUWQXO69A0MbaFAQtAYMHjwMQToBubmZqLb77kNjBaLiemNcbD+UF+WiurGVpJweUdFxQGsxXnjhBRTU2mggOLCa6eUU2+e90JGUe8FIa4IOBnpGg6JDkqJHvmhBo+Lle7W0b4gSQv+XkCm00DYRAYIGrYqH7uIDS5ocJuhhp3OctLXj28qyF+HRSRjQJx7vvTYDe0qaYNJrUVlewvcHRUSjX+/esDVX84ytiqCj5vEgLDoe/VOS0VhXgYKiUroJDXxkmowYdSL6hHrw9s9LwOQ8S1+hyE4s/WUurr1oFqYcPxzzft/KBzym8ZsCgxBoNsLa2gKHy6sS+yhC99XSImmgi03F0MeeQ9mnM1C9eTuCRp2GIfc9jNLPZgLJk5B0+ilQiKy6ABMq5r2LkvnzoE8cikGPvEKSR4JoCOD7Sr94HiVLlkA07s1CyqSNaAzCfY/NxHknjYbbI6G2aBceevhRuElaG8MSMOOFl6FoDLDWF+ORhx/CnkoHHnjgSUw9bii8tmo8en8aalos0O2jfjMia+hnrBCFEEXj0xoArjVYiW5paIYbncvbu4mE5yp9cYecCDsNB+GKGcVKNe7VbIdXDsLjygiMVkyQSEvZo1RgM13jAsThHnErKvngoWCk0hsvyX3xsLgJGXAQ0To/FyO2y2FBaXER8vLroafxqK62Fv1Hn4jnnnkCsUFa6GmQWvjth3jl/dkYPPFsPPf0wwglxhqJnN99Ngvvz/6Za0qjJ05AVV4OCspqoPVXI9US4esri1Bc68CE40bhpxWbaKuOnl/GOdfeh4evOxMzH7oN81Zsh96gZrE5WtCt6rfH5oJojoY5hqQjqW29zrsagqMKDWk7ESAFoOijbbA3NCHp2kcQN+U0lC34HrqY/ghO7QNb2m/ImfM5tCHxkJrLSCJ37kSMxGOmTMXFZ0zCO889jG2lDrz51ju4/qJz8P3mEujMZvz62Vf4dk023pj1Pm6/9mLcM+NdfPHOq9h1/Dl4+oHLEGDUYj9RzMGkpBEXSf0wnMgpCT5ZqlFEFAo12CM28dM6KsnsbzM1bwyd97ywGQ0Ion8HYjQROhH9cRLtnSluRysC8RQG014TIuVg9EIA/21FCwYiBCbBizq4urSRFZKwQWFxeHTG63B6BThaKjBjxgs49/qbESZV4Z47nsGoM6/FnVffjKV/bMcVN9wIfXMebn3sBZx2xV24+vo7sGLFaqSVtKJ3fAwqatNg5z4Hv+lDg5vDZkdFZQP69o6HUUdS3beH29cGvdk/AKhi+mhCt5GaOXNkawOcRFpjrziYh0xBzMj+yH/t3/AqBoQMHovwYUNJoksITOwNR2Y+vNRRA1MHQLFUIPe9F9BSUkNjwW4itL7d5mZgqj1T01MGDkFraRYW//o7SlpFbNiRjUFDiTDplXA0lWPRsmVI212NbTt3Y/yAgQg0iqSKFyAgrhyefb3IHUBWKSnJLrwubIeR9My2I5nK6RYkkspClwo48xTUoAmLhUr6FI4aORWhghmjlGCyg7W4RBlI2zVgWZLZdZgSPkmJxBRlOIqFPDhJPS8gCd5A+5imsB+IUPbWOnzx/mvIKG0l+8CGilYFw/smYfWC97Fpy06UOqNww/nTMGzsOKTGRWDZ7C+wKy0dLYYluOqsyUhJjMbOomafd5vMF9k3OnVqW6ZlaViJYP92LdnjS795Fzt/m4Oq8lIiuOoZP5rQfZKaOb88DjjqaxGYPByJMVNg2bkMNX/uQszlT6HX5FEo+vQN2KwaDH7kZTir80g+6hCQ3A+Okiw4qhtIygd0PSXl3yhytvn+EPyyU/E72hjtWCUQ8L8Fv0QW+DTXoQrUM2WY5BLulUdhuGCCS/FJai2prflKDZ4WM0jFRgc32F54yB72Ocj2Oge19G+2UoWXhXxOVpfgQSPd5VGMxalyCswknQ1yFEnvACwSi2k4YfZ5V00qkGnhREb6LqzPrAKNUTBGJRPXfUNM2zjFnlbwP7PSvkPkTaVw36UblbX1mBQXDzPZ5VbP3rbTU5vHxkWhYudGuheZOKRmK2R3SIz9dH+Nxq/dqML6qEH35f2mDiB73XCVlaPXJRci0N6AjBkvQ/JqEDJoFNxlGWjKyUTYCVfBFBWI8pxcaMiGDk6Oh6twOUlt6jcHEwhk55Xk5yIs8XycetIE/FnuwfEj+2HXgqWkUkoICI/H6VNORJOShZHDB6Fk21w4nBL3xB8K3PFOP+vFShTSQOPxy2oNvVMdLJCALtVjtk3TwYPEbGIXETZdseBSUq2NRLcS0Yv+cghZ3S1IFyw4G30wH1mktseS+q3FbvicaF2BaT8ajY7sWT0MBgMNTkRyWyuKy+twwtSpGLVsDUZOn4YgnYystDSMntaCqWeejoXrtuPUs0+G1mtHeXUj+3awbes2XH7fRUiODcfuknqmBEAirSk6Oh6psUH4ak86mR0+l6BXUnDapbfi6Vsvwssz7sFn3y6DwahOdx0t6EabmgVFyLCU7IHXeiqa1y9Ac1Yec76iYeU8RN56J0a9dhxkBxE/Pw2W0hJoAiJI9XOgafeuQ8wdC9CTtN216Td8u3gC7nnyNbjJ3qzM34wPv54PY+JwFBUU4fRLbsI515nRUJGNdz77jsipgSJ7aDyQfKQ8gAbO9rGyu4uFIp//uwN/mQw2YP/ifuwcCynm1UxD4H/LpIo7aIsHX4h7kCAdh7dwAmxEHC1JxJfFbdiCWmQjAkuEcqQKOgTKRmQKNrr+/u8u0AjnsLWgqqoCdpeHS222TfDY8OG7r+Pppx7HJ199R+aKiK+//BA79uyE6+N38eyTj2LON99DqxXw+SezkFVej0CTAbs3r0S190acffrJSP/wBzDXoEK/k087B1JtDlbRQMBmBrjWQ/eKjginwcQAW6tNTSZ5lKF7y+4YjbBs/Q3bdq+B4rTx6CWmCTesm4cdxWnQB+rgLC8mIpN653KAUSbr2VvoWAefNz3otTUayC4b3n7pcSxdQPayQUROVhaarA4YbWm44apLERAcjoRe0SgpyEF1QysCzGaueg8Y1A96UUaLzXNQNdLQlV17AOjp2GVCLlYRH90KnSdYcZ9IKqzCrHMJz2g2o7/CFGwB5aKdO8NAw8A1Yi2fwvoTezBfw7zrXctpnV6Prcu/xg1rvofTbqf38D2bhtopL20j/n3LjejXNwWWhhrkFRaTTWxG5tbVuPXGXAzom4y6mgoUsiktsu2p6dBaV4Y5X8/FqccNRZh5AVo9EkxB4RjWPx5ff/UVyhqspDkZIJBGZAyMwnEjhiNv6zKs27jjkOaLiu5FN38bAne6KNZWn33ZNsJTr3WWkt3sn8tm8NmfMiSbdf/56ANdnTl7JA8y03dy6ciCT1iHk0h3t3o8aLVaUUGDBpuqYZFm/YdNwH8euAPx8XH4c/0SFNc3074j4/RhT+xm7rV2wa7AQmQV+Osy6c3mp5v4c2ralXcFrf5jmLq/7zRZp+szJ53HCZfbZ1t3PE6j1aG1qRZbNlW3B5kIfLsWzQ1V2ECE5qp7B2cjm5JaOu8TrPstAGxqnwcIkdSf9eKTsFlaaVAwwJ+2HVpRwprffkTxzjWobXX5Q0tVHC34W76NrkiqiFreUffVgNuObVP7DufaTFpp/Oe0+XAE7tTR8F8GRvbSwj2Y9ear8DhsyM/PJ9ubFE7N4USTKTx4RtRo2p+JRWpxgu4zKAgH+MwgduE1P9jx+0M4YNAHG+C68kofcDtdyEvv0NjU3P4OEpklTc3NfABouw8ju8PSiE/efYOO09O11Pnpow1HxRDLF1SQusdstq5sZ+a5dbs9REQW3nnori6RNuD1eHgH5ETW7v+a7D4tjbXYuLESXHZywh8eoRVZQGJyMuzNjaTe2/nW8Kg4UrmdqKxr2o/YxwraBr6O6OpdWLsaTQHd9Vgq/kv87aRmHtaQyBicO30qNq5cjqKqxk7EFsgGNYT0wpXnnYE//1iMrNKaLknaDlKrg8OjMf30M5EcH4uMrWuwbNUmCCRRlH3mog8ktQ4Gj8eL1CET8OKTd+Kd55/Bxj0FdEsFo6aci6tPHYj7H/gP6q1uesZjk9gqjn10O6lZOCdT8ziY3cZIGBmH2267BVUZW5BRUMGnaLT+RRusnrVBE4Kpp5yKyrQ12F1YfkBSM4lvtztw+V134Y4Lx+Pnn5fw6Rfm3ZZItW5bWukhKc5USmZvMg2hHcxeJHuUmwH0XPw5/eOASCRl878shvpfV10HR1U+9uQU8gUNoiBh28bVuOf2q3D6iWPx1cLV/HjVJ6zi70C3klr2ehEWk4BTpp2C+Khg7NyyCqvWb+PksdkcGHr8ieg34UyUZGzHivWbuNd45IST0DcxDgu/n43ssjoipr7LazObNjgyGqdMH4czpo1DfXUZdmdmoLKmFsFRsRgxpB/SdmxHq0vBmPGTYK0tQbXFixGD+kJnCsOwganYs30jVm/awSW6aAjCKZOnYvjgVDRUl2DNmjUorapDeOxAnDphKGa/PBv1NhdMZjNvxvqKPPyxaTdOO/VULFy+AQ5W1vMwTAUVKo40ui/4hIUamkPx8DMv48QhvVBUXodLLzofrz71ENYWtgLmKFx55VXILq7GtVdfjuiXH8dHc1dhyNiJuODkkzGoTwweveNqFFbWQWPaP75KklgcdDTOPe8CpMaEQXFpcMWVV2PFvNmQKzx47tmHcctVl6GhVsYdDzyBPcs/wZK0Rsx6/wPUF+eiwSngcnqee++4DusyqnD3vY/h2vOmIDczCyHTTkWoTsarH8zBiH79EUKf8wpKefx6O2QP9tCx5145CdGhgSiqt3Uxe61CxV+PbiM1k8ZDRk7CtNEpmHn/TZi7LgdvfvoDrrnqKqS98D7ZtgK+fvt1vPTFL3jundm4+uqr8PPyNfj2vVexbNEafPfVG9g3+QZTkdsyfWjJZq4szMK/b70RL388BxG2HNx87zM8YcBx087ijjMfBOKfl1RyX9ik123Fi088iPUlFsydOw/HDR+IAkckrr7odHw84358Mv93hJPNH2AQeT3t8JAowGVBs7WVq94dngZ1pZUwB4YhPCIQBbWWw3S8qVBxZNF96jdpoxExMbDWVyEzuxROmw1ZWQUYOzkWQcEmeGxNyCgsgNthR0lBIfTDhsNsMqChtRVS+wrjjpfzG7uKP6mCfyubhlHY8bTd63Xz4vZt95f958ltApRIaWuoQgGLyrKRCt1C96JrxcRGQXDWYeXm7dyZ1tpUj2Z2DyIpuyabytFqdL5F2u0QYAw081BYj9Orat4q/jZ0q03tIrvZYA5EYKCBr8kNDg2C5HbB7XJD1JsQbAqAh0Uy0TFsQb/kln0RT/tMc0leD6J79cO1110BuaUCX87+Gg1WD5eMvjlVoX2xgYaFgEqAgQYIWSHCKyKCA0z+eW9m50t8IYiWZfDwc9TOMn9oA5EQEYaM4lqYDAbuvJNkL8qrS+HVByAuKhK7C6sBtM3TCkhOTUZzXTVqG1pxwAlkFSr+YnQbqRnhCjK2o8l7Nx586CH035iDC08fj7XfvYFGuwS9MQw33nwndFFDcMGZJ2Hbqjmoa3FCt48Gy4lI9nlwZBJuuP5GuOqyMf+nH+lYV7u6q9WSJNX7Xo15uBvqG+HUReP22+5EicWAkf1SsYEGFZEIzhZCtK2uYvPgRqMB+Zl/IqfUiidnzET8dwsQ338oGrK34csfF6EsZzd2lzRh0vHHYdXWdJ9TjaS/PiAUUyaNx9aN36Om1UpjUVfrqlSo+OvRfeuptaTeludgxgvP4cZrrsRVFw/A6vlf4J3P58JjisQv879DVGgYLr30X9i9/ie89eFsviDfTWq60cNUXsGvPws8UMTWVIW5P82D3FwGq8PLVWMGtipq+4a1CHRVcqnN1i1XFezBp5/NxmXnngxzST7Zzt8gp6AcLQ1eLF3xO6wulvvMg/WrV6CsqApeSw2efPI/uP3Wm3DJFVfB1lKPr1Yt4ql/3NYG/LxwCR686jzM/XU5cssbeQaSUZOnYWRSAO59dhU8Eg0WaqCVir8J7aTuGJhxuCGZ/x0E7mja9Psv2LVpNQJNejQ2NvmSDtqq8cKzT0GjMyA8NASW1ma4vQpCQiPRf8wYDBh3KgK1CiobrD61mq5TU5mDxx+8lweqsPnnthQ8LOLs649n8c+69nBRL777fBZ+m/8VHLZWWGxOviCCDQAzXtjNz2dzzR+88TIfCNg0VVn2Drr+PQgLCYHd2gqn28OdccyLv275AgxOMiMgMIRuSKQWtAg06/DdFx8inQYLlvtMhYq/C90efMJihT0uBxocdr54o82hZDCaeJaNpuYmv1fZi4iYZNx9/8OIDNTj28/e8xHG4CMMC1XUH2ANr26fFV2+8Ef44ph5iONe1bhj5tCOccxsUQQb3BobG/jztAW8sMULzpYqvPbKKzxQxRdPDmz8bS7WsGWULHhFdXqr+BvRTmpfFg33XySlO4NJ165me5S2TBrwEbO8aDfuuOUGnkze5XDylEX/+7PtH9d8yDMEoevoNSI5y3rS8VHYs/ui4P7Hx1Oh4gihU491ezxH1YJ3NsA4XS7+WTjKFkns205HU7up+GejE6nVjqlCxbGPv32VlgoVKo4sVFKrUNHDoJJahYoeBpXUKlT0MKikVqGih0EltQoVPQwqqVWo6GFQSa1CRQ+DSmoVKnoYVFKrUNHD8D+T+q9a+OGFDE2XRWFVqFBxOPivSd227tqg1/NkfvtnD/vfoaPHGYRAVAtWNCqeLsvDdngSXoFS8P+oUKHCh0OSmuXqZsn3WPIBtt6Z5b6/8Ko7MaW/CU8+9xrsssATA7J0f0y+ajtIWZbkz+0v5Kr3k0/x/7DPbF/bOQpY9pEgPC+PwxxhC74X63nlSMV/JVYTWsdLywmczoJiwPXojXRUYL1ggZldwyvx1VzqwhQV/2R0SWomjRmZWXWLqJgYyG4HLHYHzw0WlTwE1113OX7/YiZaXW5odHokEhnjiXINRNNywQEmv5kUNRItR9I+uhKKBRustFVPtwxktZXpHkOVADrDjULBTmcbECYo+FDcg2z+t8hJzY4VZQ2SiLaVRN5yuEiWaxGDEFyCfrTfiXzBV4JWGx0MW0sDLDYHtDqDmqJXxT8SnUjNqlx4vG7oDIHoN2QoTpl+Fs6eNgFvP/s4ftuSzutGn3r2RQhX6rFw2Roir4hTlVQ8KPcDK77KLvamuBMLhVokIhwz5VFEO1LT6bh0oQwPIQ0pSi/MlAbCI8iIEliGTw+exAYEoBfuVfpCS3+/LrYiiwaBeCUMr8qj6UokzRUt7LTtMXE7opRYfs8YQYt/KQNwClLxg6YQgbfeg1MHBOKnnxZizYaNqKiu4/oDL7ejCm8V/xB0ylFmDgrHmOOPxxlnnImRI4bC2lCFZQt+QFpuMVeEA2NSccm5p2Ldb1+gsKoRAcYwnK30QaVYhceRjViSoTbRAZ2ix7XKYPQlyXy/uAlexYj+soGXoWGSOlkIRbZSjHuEXCJmMFrp/llCOWYIbrwuj0QEHdNWtzkZwfhTyMZbQhWeUyZw4j8gZuJh2PGiMhKrhDzMRx0sNBhFLP4ByUGX4+pb78UV11yD1b8vx8qVq5GVVwy3ombtVfHPQDupPW4Pxp57OT5+5SE0FKfhldeexiKSxs1WBwKDAuD1yrjg/MsRLTTjmR8WQdDqIQle5KEJ15BcfpLU5+2owbdKEynGZoxWQvGtuAub0AyDIGJne315gejoxKfabGxVWonkLfClB5SQQX/bOrneRNIG7FgglmIHHbdWrsUVSghtd9EQYiHFXUE1nbFbbEEISe26batx14Y/EN97AK668Rbcf++T+Nc503HlZdejqMUGnaqOq/gHoJ3UrPRq1tbf8eY7gThl6kTccMe9OH78CViybAW2btsGb1gckfo0bPrjO6QXVcFgMnP32BdCGopIpT6RVOKbMRKhRLRPhPr2ihm+//ucaG10ZY4uF+0y0ladv+y6Z2/NDZLsMtyilxfAYAn22XbZfzX2t1YRaAjR8DMV/y8rJxud0BcnnXQKTj55ClITY7Fu5S9YsngR6h1OaLuoe61CRU/EXlJrNKityMY7b76Ab7/rhclTpuGM06fjlVdPxcO33gxb7Bj0DVfw2vxFkHV67q82ECWHkt2bi1r8qWlAkBSMwaSCW1GBPYoVF5Gtu56Ua7diQIqgwypUca+3hiS3ttM0lIBEJZDU7kDuxY4TyKaXg2Hm+0w4Re6FDOLkOCUClWSvW/00FxUNjqOzhkkWNItaXHnrf3D+CQOxef0KPPfZLGzdkQaHy8vTAauqt4p/CjrnKNNowWqwt9ZXY/73X+KXhT+ib9++sNtl/OfRK7Bh2Xyk51ZApzNwuSoRGU8jm/o0BMEpkQKtePCiWEFqsQefanYjgezjD3ACbRewh7avEirBfOMVig12USGp65vi0ig63KwMJ4IG8nNPk/vjeCEeC4RSWMnOnqL0xgQpFU7BgWfEPDgUVhPahu/FYlwjJ2IW4vAjsvDTd+9h/sd1KC6rYi/DydyWUliFin8KupzSYuQ2mrRQZC9279qBESefhT6RWsx88Re4ZebsApe4ElHwXWEHfiUyBpGELRUtKCV72UCXrSJb+z5xE0nyYCikSucLFtKTtSgSqvBvsQ5WGgA0/rARmWzz94V0UscFspZ9EWUS/YTRuUa6x9tiGipJOFcJrShRnP55bQU/CFlYoS2CSRFhEZxozC4Fs8N1LId4tzajChVHDw4afMKCTsyBgajO2oHbbr4ZVdU1nRLeM0paBBfSiMgkqDlJ20JP2CcHUXQzqcs857aC9oCTRsXlP7sNCurp6I41JD10RSMNFl7aWgUb1glWsKpXWr8N7gtkARoUh+9vkvo6fdfJ/VWo+CfhkBFlLDrLYmlFS0szr6ixX75r/09XbiiBR4vte/ze/+9/nb1ggSd1JJkfwHaU0cBhVPYv4S4AUENEVajojMOK/fZV1Ohe7zEjq5Pk9U6hEfouCK1ChYqucVQvvWTENuDoqsyhQsXRjqOa1CpUqPjvoZJahYoeBpXUKlT0MKikVqGih0GrEZRX/+6HUKFCxZGBJCHv/wAqhMEjGS7HIgAAAABJRU5ErkJggg==) 

45. 

46.  	看图写结果：
     ![img](data:image/png;base64,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) 

47. 

48.  	django、flask、tornado框架的比较？

49. 

50.  	什么是wsgi？

51. 

52.  	django请求的生命周期？

53. 

54.  	列举django的内置组件？

55. 

56.  	列举django中间件的5个方法？以及django中间件的应用场景？

57. 

58.  	简述什么是FBV和CBV？

59. 

60.  	django的request对象是在什么时候创建的？

61. 

62.  	如何给CBV的程序添加装饰器？

63. 

64.  	列举django 	orm 中所有的方法（QuerySet对象的所有方法）

65. 

66.  	only和defer的区别？

67. 

68.  	select_related和prefetch_related的区别？

69. 

70.  	filter和exclude的区别？

71. 

72.  	列举django 	orm中三种能写sql语句的方法。

73. 

74.  	django 	orm 中如何设置读写分离？

75. 

76.  	F和Q的作用?

77. 

78.  	values和values_list的区别？

79. 

80.  	如何使用django 	orm批量创建数据？

81. 

82.  	django的Form和ModeForm的作用？

83. 

84.  	django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。

85. 

86.  	django的Model中的ForeignKey字段中的on_delete参数有什么作用？

87. 

88.  	django中csrf的实现机制？

89. 

90.  	django如何实现websocket？

91. 

92.  	基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf 	token？

93. 

94.  	django中如何实现orm表中添加数据时创建一条日志记录。

95. 

96.  	django缓存如何设置？

97. 

98.  	django的缓存能使用redis吗？如果可以的话，如何配置？

99. 

100.  	django路由系统中name的作用？

101. 

102.  	django的模板中filter和simple_tag的区别？

103. 

104.  	django-debug-toolbar的作用？

105. 

106.  	django中如何实现单元测试？

107. 

108.  	解释orm中 	db 	first 和 code 	first的含义？

109. 

110.  	django中如何根据数据库表生成model中的类？

111. 

112.  	使用orm和原生sql的优缺点？

113. 

114.  	简述MVC和MTV

115. 

116.  	django的contenttype组件的作用？

117. 

118.  	谈谈你对restfull 	规范的认识？

119. 

120.  	接口的幂等性是什么意思？

121. 

122.  	什么是RPC？

123. 

124.  	Http和Https的区别？

125. 

126.  	为什么要使用django 	rest framework框架？

127. 

128.  	django 	rest framework框架中都有那些组件？

129. 

130.  	django 	rest framework框架中的视图都可以继承哪些类？

131. 

132.  	简述 django 	rest framework框架的认证流程。

133. 

134.  	django 	rest framework如何实现的用户访问频率控制？

135. 

136.  	Flask框架的优势？

137. 

138.  	Flask框架依赖组件？

139. 

140.  	Flask蓝图的作用？

141. 

142.  	列举使用过的Flask第三方组件？

143. 

144.  	简述Flask上下文管理流程?

145. 

146.  	Flask中的g的作用？

147. 

148.  	Flask中上下文管理主要涉及到了那些相关的类？并描述类主要作用？

149. 

150.  	为什么要Flask把Local对象中的的值stack 	维护成一个列表？

151. 

152.  	Flask中多app应用是怎么完成？

153. 

154.  	在Flask中实现WebSocket需要什么组件？

155. 

156.  	wtforms组件的作用？

157. 

158.  	Flask框架默认session处理机制？

159. 

160.  	解释Flask框架中的Local对象和threading.local对象的区别？

161. 

162.  	Flask中 	blinker 	是什么？

163. 

164.  	SQLAlchemy中的 	session和scoped_session 	的区别？

165. 

166.  	SQLAlchemy如何执行原生SQL？

167. 

168.  	ORM的实现原理？

169. 

170.  	DBUtils模块的作用？

171. 

172.  	以下SQLAlchemy的字段是否正确？如果不正确请更正：

173. | 1 				 				2 				 				3 				 				4 				 				5 				 				6 				 				7 				 				8 				 				9 				 				10 				11 | from datetime import datetime 				 				 from sqlalchemy.ext.declarative 				 				import declarative_base 				 				 from sqlalchemy import Column, 				Integer, String, DateTime 				 				   				 				Base = declarative_base()   				 				class UserInfo(Base):     				 				    __tablename__ = 'userinfo'     				 				    id = Column(Integer, 				primary_key=True, autoincrement=True)  				 				    name = Column(String(64), 				unique=True)  				    ctime = Column(DateTime, 				default=datetime.now()) |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     |                                                              |                                                              |

174. 

175.  	SQLAchemy中如何为表设置引擎和字符编码？

176. 

177.  	SQLAchemy中如何设置联合唯一索引？

178. 

179.  	简述Tornado框架的特点。

180. 

181.  	简述Tornado框架中Future对象的作用？

182. 

183.  	Tornado框架中如何编写WebSocket程序？

184. 

185.  	Tornado中静态文件是如何处理的？ 如： 	<link 	href="{{static_url("commons.css")}}" 	rel="stylesheet" />

186. 

187.  	Tornado操作MySQL使用的模块？

188. 

189.  	Tornado操作redis使用的模块？

190. 

191.  	简述Tornado框架的适用场景？

192. 

193.  	git常见命令作用：

194. 

195.  	简述以下git中stash命令作用以及相关其他命令。

196. 

197.  	git 	中 merge 	和 rebase命令 	的区别。

198. 

199.  	公司如何基于git做的协同开发？

200. 

201.  	如何基于git实现代码review？

202. 

203.  	git如何实现v1.0 	、v2.0 	等版本的管理？

204. 

205.  	什么是gitlab？

206. 

207.  	github和gitlab的区别？

208. 

209.  	如何为github上牛逼的开源项目贡献代码？

210. 

211.  	git中 	.gitignore文件的作用?

212. 

213.  	什么是敏捷开发？

214. 

215.  	简述 jenkins 	工具的作用?

216. 

217.  	公司如何实现代码发布？

218. 

219.  	简述 	RabbitMQ、Kafka、ZeroMQ的区别？

220. 

221.  	RabbitMQ如何在消费者获取任务后未处理完前就挂掉时，保证数据不丢失？

222. 

223.  	RabbitMQ如何对消息做持久化？

224. 

225.  	RabbitMQ如何控制消息被消费的顺序？

226. 

227.  	以下RabbitMQ的exchange 	type分别代表什么意思？如：fanout、direct、topic。

228. 

229.  	简述 celery 	是什么以及应用场景？

230. 

231.  	简述celery运行机制。

232. 

233.  	celery如何实现定时任务？

234. 

235.  	简述 celery多任务结构目录？

236. 

237.  	celery中装饰器 	@app.task 	和 @shared_task的区别？

238. 

239.  	简述 requests模块的作用及基本使用？

240. 

241.  	简述 	beautifulsoup模块的作用及基本使用？

242. 

243.  	简述 seleninu模块的作用及基本使用?

244. 

245.  	scrapy框架中各组件的工作流程？

246. 

247.  	在scrapy框架中如何设置代理（两种方法）？

248. 

249.  	scrapy框架中如何实现大文件的下载？

250. 

251.  	scrapy中如何实现限速？

252. 

253.  	scrapy中如何实现暂定爬虫？

254. 

255.  	scrapy中如何进行自定制命令？

256. 

257.  	scrapy中如何实现的记录爬虫的深度？

258. 

259.  	scrapy中的pipelines工作原理？

260. 

261.  	scrapy的pipelines如何丢弃一个item对象？

262. 

263.  	简述scrapy中爬虫中间件和下载中间件的作用？

264. 

265.  	scrapy-redis组件的作用？

266. 

267.  	scrapy-redis组件中如何实现的任务的去重？

268. 

269.  	scrapy-redis的调度器如何实现任务的深度优先和广度优先？

270. 

271.  	简述 vitualenv 	及应用场景?

272. 

273.  	简述 pipreqs 	及应用场景？

274. 

275.  	在Python中使用过什么代码检查工具？

276. 

277.  	简述 	saltstack、ansible、fabric、puppet工具的作用？

278. 

279.  	B 	Tree和B+ 	Tree的区别？

280. 

281.  	请列举常见排序并通过代码实现任意三种。

282. 

283.  	请列举常见查找并通过代码实现任意三种。

284. 

285.  	请列举你熟悉的设计模式？

286. 

287.  	有没有刷过leetcode？

288. 

289.  	列举熟悉的的Linux命令。

290. 

291.  	公司线上服务器是什么系统？

292. 

293.  	解释 PV、UV 	的含义？

294. 

295.  	解释 QPS的含义？

296. 

297.  	uwsgi和wsgi的区别？

298. 

299.  	supervisor的作用？

300. 

301.  	什么是反向代理？

302. 

303.  	简述SSH的整个过程。

304. 

305.  	有问题都去那些找解决方案？

306. 

307.  	是否有关注什么技术类的公众号？

308. 

309.  	最近在研究什么新技术？

310. 

311.  	是否了解过领域驱动模型？

https://www.cnblogs.com/wupeiqi/articles/5729934.html