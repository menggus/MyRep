## ihome 项目知识点

### 项目的入口
- manage.py 项目管理文件
- 创建flask - app, 跟进不同的配置文件
```python
# coding:utf-8

from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建flask的应用对象,
# 这里调用了创建app的工厂函数, 根据传入的字符串来创建"开发环境" 或 "生产环境" 下的app
app = create_app("develop")

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()


```