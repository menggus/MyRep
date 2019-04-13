### Selenium  &  PhantomJS 使用

```python
from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.PhantomJS()
# 自定义窗口的大小
driver.ser_window_size(1920, 1080)
# 设置窗口最大化
driver.maximize_window()
# 发送请求
driver.get("http://www.baidu.com")
# 进行网页截屏
driver.save_screenshot("./baidu.png")
# 元素定位,百度搜索输入框，并输入 “python”
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()  # 点击按钮搜索
# 退出浏览器
driver.quit()
# 定位页面的元素方法
find_element_by_id (返回一个)
find_elements_by_xpath （返回一个列表）
find_elements_by_link_text 
find_elements_by_partial_link_text 
find_elements_by_tag_name 
find_elements_by_class_name 
find_elements_by_css_selector
# 注意点:
find_element 和find_elements的区别：返回一个和返回一个列表
by_link_text和by_partial_link_text的区别：全部文本和包含某个文本
by_css_selector的用法： # food span.dairy.aged
by_xpath中获取属性和文本需要使用get_attribute() 和.text

```

#####  selenium使用注意点

​	1.获取文本和获取属性：先定位到元素，然后文本使用.text获取；属性使用get_attribute方法来获取

​	2.selenium获取的页面数据时浏览器中的element的内容

​	3.find_element和find_elements的区别：

​		find_element返回的是一个element元素，如果没有会报错

​		find_elements返回的是一个保存elemen的列表，没有则为空列表

​		在判断是否有下一页的时候，通常使用find_elements来根据结果的列表长度来判断

​	4.如果页面中含有iframe、frame时，需要先调用driver.switch_to.frame()方法切换到frame中	才能定位元素

​	5.selenium请求第一页的时候等待页面加载完成之后才会获取数据，但是在点击翻页后，会直接获取数据，此时可能获取不到页面还没加载之后的数据，而报错。所以通常情况下，会让获取数据之前等待一个时常，如time.sleep(3)，等待3秒。



### 登录验证码的识别

##### 请求url不变，验证码不变

​	请求的验证码的地址，获得响应，对验证码进行识别。

##### 请求url不变，验证码会变

​	思路：对方服务器返回验证码的时候，会和每个用户的信息和验证码进行对应；之后，在 	用户发送post请求的时候，会对比post请求中所带的验证码数据和当前用户真正存储在服务	器端的验证码是否相同。

​	1.实例化session

​	2.使用session请求登录页面，获取验证码的地址

​	3.使用session请求验证码，然后进行识别

​	4.使用sess发送post请求

##### 使用selenium登录，遇到验证码

​	url不变，验证码不变，同上

​	url不变，验证码改变

​		1.selenium请求登录页面，同时拿到验证码的地址

​		2.获取登录页面中的driver中的cookie，交给requests模块发送验证码的请求，然后获取		到验证进行识别

​		3.输入验证码，点击登录