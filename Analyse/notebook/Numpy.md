## Numpy

### 概述

-   一个在Python中做科学计算的基础库，重在数值计算，也是大部分PYTHON科学计算库的基础库，多用于在大型、多维数组上执行数值运算

### 基本使用

-   创建数组

    ```python
    import numpy as np
    # 创建数组（矩阵）,以下三种方式均创建同样的数组
    # 方式一
    np.array([1,2,3,4,5])
    # 方式二
    np.array(range(1,6))
    # 方式三
    np.arange(1,6)
    
    # 数组的所属类
    type(a)
    # 数据类型
    a.dtype
    ```

-   Numpy中数据类型种类

    ![1556772293005](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1556772293005.png)

    ```python
    # 创建指定数据类型的数组， 参数dtype
    # 创建参数为bool数据类型的数组
    boolarray = np.array([1,0,1,1,0], dtype=np.bool)  # 或者dtype=“bool”
    
    # 数组.astype("数据类型")		修改数据类型		
    updatearray = boolarray.astype(i1)
    updatearray = boolarray.astype(np.int8)
    
    # np.round(数组，保留位数)			浮点型小数位  
    np.round(a, 2)  # 保留2位小数位，保留方式四舍五入
    
    # 拓展，python中保留小数位
    "%.2f" % 0.312312312   # 保留2位
    [out]:  0.31
    ```

-   数组的维度

    ```python
    # 创建2行6列的数组
    a = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
    
    # 查看数组的维度
    a.shape
    [out]: (2,6)  # 2行6列数组
    
    # 修改数组维度 3行4列  ，会重新创建新的数组进行返回，原数组不会改变
    a.reshape(3,4)
    
    # 把数组转化为1维数组  已知数组 b:（3,4）
    b.reshape(12,)
    
    # b.flatten()  转化为一维数组
    b.flatten()
    ```

-   数组的计算

    ```python
    # 与数值进行计算，如
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    a+1
    a-1
    a*1
    a/1
    # 数组与数值进行加减乘除，数组的每一个值与该数值进行运算
    
    # 与数组进行计算
    #####  Numpy中的   数组a*数组b为  元素乘法，并不是矩阵乘法
    #  *  元素乘法
    import numpy as np
    
    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)
    
    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print(x + y)
    print(np.add(x, y))
    
    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print(x - y)
    print(np.subtract(x, y))
    
    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print(x * y)
    print(np.multiply(x, y))
    
    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print(x / y)
    print(np.divide(x, y))
    
    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print(np.sqrt(x))
    
    
    # 矩阵的乘法 a.dot(b)
    import numpy as np
    
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])
    
    v = np.array([9,10])
    w = np.array([11, 12])
    
    # Inner product of vectors; both produce 219
    print(v.dot(w))
    print(np.dot(v, w))
    
    # Matrix / vector product; both produce the rank 1 array [29 67]
    print(x.dot(v))
    print(np.dot(x, v))
    
    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print(x.dot(y))
    print(np.dot(x, y))
    ```



### Numpy文件的读入

-   读取本地文件

    -   CSV文件：Comma-Separated Value逗号分隔值文件
    -   显示：表格状态

    -   源文件：换行和逗号分隔行列的格式化文本,每一行的数据表示一条记录

    -   由于csv便于展示,读取和写入,所以很多地方也是用csv的格式存储和传输中小型的数据,为了方便教学,我们会经常操作csv格式的文件,但是操作数据库中的数据也是很容易的实现的
    -   ![1556782955176](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1556782955176.png)

    ```python
    # 本地文件地址firl_path   如 CSV文件：逗号分隔值文件
    # 格式：
    # param： file_path: 文件路径			
    # skiprows：跳过前多少行	usecols: 读取指定列，索引 元组类型		
    # dtype：读入后的数组值类型，默认情况下会将较大数据变更科学计数法
    # delimiter：数据分隔符号，不指定会导致每一行数据变为一个整体字符串而报错
    # unpack：行列转置
    np.loadtxt(file_path,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False）
    
    ```

    ```python
    # Numpy中矩阵的转置
    # 对于数组来说，即是行和列的变化，交换位置，1行变成1列，1列变为一行
    t = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    # 对数组t进行转置
    # 方式一：
    t.transpose()
    # 方式二：轴交换 0轴和1轴进行交换
    t.swapaxes(1,0)
    # 方式三：
    t.T
    ```

### Numpy中数组的索引和切片

-   索引切片

    ```python
    a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    # 通用格式：
    # a(:,:)   第一个：可以对行进行切片，第二个：对列进行切片，（省略：= ：）
    a[0]  # 取第一行， 同a[0,:]
    a[0:3] # 取第一行到第三行，同a[0:3,:]
    a[[0,2]] # 取第一行和第3行
    a[:,0]  # 取第一列
    a[:,0:3]  # 取第一列到第三列
    a[:,[0,2]]  # 取第一列和第三列
    ```

-   数组数值的修改

    ```python
    # 修改数值
    # 先使用索引查找位置，然后进行赋值
    # 更改a的第三行第三列值为99
    a[2,2] = 99
    # a的第四行数第2列以后数值更改为0
    a[3,1:] = 0
    ```

-   bool索引

    ```python
    a = np.arange(24).reshape(4,6)
    # 输出与a同样的维度数组，满足条件为True，不满足为False
    a < 10
    # 查找a中数值小于10的值
    a[a<10] 
    # 对查找到的数据进行赋值
    a[a<10] = 0
    #
    # 三元运算， 即对于满足的   和   不满足都可通过一个表达式进行赋值
    # np.where(条件，满足时，不满足时)
    np.where(a<10,0,10)
    ```

-   裁剪clip

    ```python
    # 对于数组中值小于a的替换为a，值大于b替换为b，但是nan并不会被替换
    # 使用bool索引运算需要2步，分别进行
    a.clip(a, b)
    ```

-   NAN

    nan(NAN, Nan):	not a number不是一个数字

    nan出现的情况：

    -   当读取本地文件时，如果有缺失，这个缺失部位会补nan
    -   当进行了一个不合适的计算时，例如：无穷大-无穷大

    inf(-inf, inf): 表示无穷，负无穷与正无穷

    inf出现情况：

    -   当计算分母为0时，python会报错，但是numpy中会以inf或者-inf表示无穷

    ```python
    # 如何指定nan  和  inf
    # nan,  
    np.nan  # 类型为float
    # inf
    np.inf  # 类型也为float
    ```

    ##### 注意事项：

    -   两个nan是不相等的：np.nan != np.nan

    -   利用上述特性，两个nan不相等，可以统计数组a中的nan的个数

        ```python
        # 在设置数组中的值为nan时，数组的类型必须为nan的类型，即float类型
        a = np.arange(24).reshape((4, 6))  
        a = a.astype("float")  # 转换a的数值类型为float类型
        np.count_nonzero(a!=a)
        a[[2,3],[3,2]] = np.nan  # 设置2个值为nan
        
        # 判断数值是否为nan
        np.isnan(a)
        # 给nan类型值重新赋值,如赋值为0
        a[np.isnan(a)] = 0
        
        # nan和任何值计算均为nan
        ```

### Numpy中的常用统计函数

-   函数：

    ```python
    # 求和	参数axis 为轴的值一般为0 1 2等
    t.sum(axis=None)
    # 均值
    t.mean(axis=None)
    # 中位数
    np.median(t, axis=None)
    # 最大值
    t.max(axis=None)
    # 最小值
    t.min(axis=None)
    # 极值，最大值与最小值之差
    np.ptp(t, axis=None)
    # 标准差: 反应了数据的稳定性，越小越稳定；越大，说明波动越大。
    a.std(axis=None)
    ```

-   对于缺失值的填充

-   数组的拼接

    ```python
    # 横向拼接
    # 如：有数组t1，t2；对两个数组进行拼接
    np.hstack((t1, t2))  
    
    # 特别注意：传入参数是以元组形式（t1，t2）
    
    # 纵向拼接
    np.vstack((t1, t2))
    ```

-   数组的行列交换

    ```python
    # 行列交换，两个数组的每一列代表字段不一样，需要对其中一个数组进行列的交换，与另一数组的列一样
    
    # 数组t的第2列和第3列进行交换
    t[:,[1,2] = t[:,[2,1]]
      
    # 数组t的第2行与第3行进行交换
    t[[1,2]] = t[[2,1]]
    
    ```

-   快捷创建简单数组

    ```python
    # 创建值全部为0 的数组
    np.zeros((1,2))  # 创建1行2列的值全为0的数组
    # 创建值全部为1 的数组
    np.ones((1,2))  # 创建1行2列的值全为1的数组
    # 创建对角数组
    np.eye(3)  # 创建3行3列的值全为1数组
    
    # 以一个a数组为模板创建同样形状的空数组
    np.empty_like(a)
    
    # 求数组a最大值，最小值
    np.argmax(a, axis=0)  # axis为轴
    np.argmix(a, axis=1)  # axis为轴
    ```

-   Numpy随机数组的生成

    ![1556889824546](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1556889824546.png)

### Numpy中关于赋值，视图操作注意点

-   a = b  完全不复制，a和b相互影响，改变a，b跟着变，改变b，a跟着变
-   a = b[:]  视图操作，会创建新的对象a，但是a的数据完全由b保管，数据变化是一致的，也相互影响
-   a = b.copy() 复制，a与b不相互影响，类似于深拷贝



