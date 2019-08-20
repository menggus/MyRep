## Using the stark component 

#### 1.导入组件stark

#### 2.settings.py 注册stark apps
```python
INSTALLED_APPS = [
     ...,
    'crm.apps.CrmConfig',
    'stark.apps.StarkConfig',
]
```
#### 3.使用stark组件,首先配置urls.py
```python
from stark.service.stark import site

urlpatterns = [
    ...
    path('stark/', site.urls),
]
```
#### 4.在需要使用stark组件的app内, 新建stark.py文件, 并进行相应配置
```python

```