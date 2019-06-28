### 添加断言 assert  (调试辅助功能)

### assert

- 断言是用于程序bug的测试

- 通过对某一变量或输出进行正确的指定, 如果不满足指定条件,则程序终止,断言错误

  ```python
  # 例: 商品打折函数
  # price:商品原价  dicount: 折扣
  def discount_price(price, discount):
      discount = price*discount/10
      assert discount>0 and discount<price, "error discount"
      return discount
  # 打9折,价格变为90
  In [15]: discount_price(100, 9)                                                       Out[15]: 90.0
  # 折扣大于10时,由于断言存在,会触发AssertionError
  In [16]: discount_price(100, 19)                                                                            
  ---------------------------------------------------------------------------
  AssertionError                            Traceback (most recent call last)
  <ipython-input-16-56248123c4fe> in <module>
  ----> 1 discount_price(100, 19)
  
  <ipython-input-14-733e581b1c1b> in discount_price(price, discount)
        1 def discount_price(price, discount):
        2     discount = price*discount/10
  ----> 3     assert discount>0 and discount<price, "error discount"
        4     return discount
        5 
  
  AssertionError: error discount
  
  # 从上可知,通过断言可对程序进行测试, 程序的运行结果是否符合我们的预期
  
  ```

### 断言语法

```python
assert 条件表达式, "断言错误提示信息"
```



### 普通的异常处理与断言的区别

- 断言是为了告诉开发人员,程序中发生了 **不可恢复** 的错误
- 普通的异常处理,是用来处理  **可预料**  的错误情况, 针对该错误可进行相关处理



### 注意事项

##### 不适用程序功能逻辑

- 不要使用断言来进行程序中的数据验证, 应该交给if语句来进行处理

  断言语句可以通过一些方法进行禁用, 所以不要断言不可用于程序主体逻辑中的验证, 一旦被禁用,用于程序功能逻辑的效果将消失,这样是非常可怕的,例如:管理员权限的验证, 跳过验证, 非管理员用户也能进行管理员权限的操作

##### 永不失败的断言

- 当断言语句后使用的为元组形式

  ```python
  assert (条件, "断言错误")
  # 由于是元组, assert会误认为元组为条件表达式, 但是元组会被永远认为为True
  # 所以该断言,永远都是真, 不会出现断言失败
  ```


### 关键要点

- Python的断言语句是一种测试某个条件的调试辅助功能, 可作为程序的内部自检
- 断言应该只用于帮助开发人员识别bug,它不是用于处理运行时错误的机制
- 设置解释器可禁用断言