### Python 中 is   and   ==

###  对象比较 is 和 "=="

```python
# is and "==" 的比较
In [2]: a = [1, 2, 3]                                                           

In [3]: b = [1, 2, 3]                                                           

In [4]: a is b                                                                  
Out[4]: False

In [5]: a == b                                                                  
Out[5]: True

# 
In [21]: c = [1, 2, 3]                                                          

In [22]: d = c                                                                  

In [23]: c is d                                                                 
Out[23]: True

In [24]: c == d                                                                 
Out[24]: True


# 当两个变量指向同一个对象时, is比较返回为  True
# 当两个变量指向的对象含有相同的内容时, == 比较返回为  True
```



