Python 中 logging	模块

日志文件模块：用于日志的输出与持久化

使用

```python
import logging

# 设置日志的输出样式，可网络查看别人的设置
# level 日志输出等级
# format  日志输出显示格式
# datefmt  时间的输出格式，默认格式是 “2003-07-08 16:49:45,896”

# 配置输出样式
logging.basicConfig(level="logging.INFO", 
                    format="%(levelname)s [%(filename)s:%(lineno)d]: %(message)s]  %(asctime)s", datefmt="[%Y-%m-%d %H:%M:%S]")

# 实例化一个logger(复用)，通过导入logger可以在其他py文件使用
logger = logging.getLogger(__name__)

# 使用
logger.info("输出日志信息")
```

### format配置

| %(name)s            | Logger的名字                                                 |
| ------------------- | ------------------------------------------------------------ |
| %(levelno)s         | 数字形式的日志级别                                           |
| %(levelname)s       | 文本形式的日志级别                                           |
| %(pathname)s        | 调用日志输出函数的模块的完整路径名，可能没有                 |
| %(filename)s        | 调用日志输出函数的模块的文件名                               |
| %(module)s          | 调用日志输出函数的模块名                                     |
| %(funcName)s        | 调用日志输出函数的函数名                                     |
| %(lineno)d          | 调用日志输出函数的语句所在的代码行                           |
| %(created)f         | 当前时间，用UNIX标准的表示时间的浮 点数表示                  |
| %(relativeCreated)d | 输出日志信息时的，自Logger创建以 来的毫秒数                  |
| %(asctime)s         | 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 |
| %(thread)d          | 线程ID。可能没有                                             |
| %(threadName)s      | 线程名。可能没有                                             |
| %(process)d         | 进程ID。可能没有                                             |
| %(message)s         | 用户输出的消息                                               |