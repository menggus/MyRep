## Mongodb  与 python的交互

-   pymongo

```python
from pymongo import MongoClient

# 实例化MongoClient客户端
client = MongoClient()   # 本地可以不写host= ip地址		port= 端口号
collection = client['数据库名']['集合名']
```

