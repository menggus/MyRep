## dailyfresh

### itsdangerous
- 一种加密工具, 为传输到页面的数据进行加密操作;
```python
# 加密过程
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired

# 加密用户的身份信息，生成激活token
serializer = Serializer(settings.SECRET_KEY, 3600)
info = {'confirm':user.id}
token = serializer.dumps(info) # bytes
token = token.decode()

# 解密过程
serializer = Serializer(settings.SECRET_KEY, 3600)
# 需要解密的token
info = serializer.loads(token)
# 获取待激活用户的id
user_id = info['confirm']

# 注意: 加密&解密的操作方式一样.
```

### "记住用户名"功能
- 通过记住用户名, 下一次登录时, 就不用输入; 
```python
# 页面需要设置该select标签, 后台访问时, 获取标签信息

# post 登录时
# 判断是否需要记住用户名
response = redirect(reverse('goods:index'))  # 跳转的响应对象
remember = request.POST.get('remember')

if remember == 'on':
    # 记住用户名
    response.set_cookie('username', username, max_age=7*24*3600)
else:
    response.delete_cookie('username')

# get登录页面
# 判断是否记住了用户名
if 'username' in request.COOKIES:
    username = request.COOKIES.get('username')
    checked = 'checked'
else:
    username = ''
    checked = ''
```

### 邮件激活
- 通过激活过的账户,才能进行登录; 在注册时, 由于发送邮件, 可能会延时, 造成用户体验不好, 所以采用异步任务方式来进行;
- Celery 实现异步任务的一个即插即用的任务队列
```python
# 使用celery
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
import time

# 在任务处理者一端加这几句
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
# django.setup()

# 创建一个Celery类的实例对象, 这里broker采用redis
app = Celery('celery_tasks.tasks', broker='redis://172.16.179.130:6379/8')


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    # 组织邮件信息
    subject = '任务'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您成为会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)


# 在合适的地方调用该任务函数, 就把任务加入到broker
send_register_active_email.delay(email, username, token)

# 在worker 端, 同样需要导入该项目, 并需要在终端开启worker
celery -A tasks worker --loglevel=info
```

### 用户历史浏览记录
- 用户浏览商品之后会存在浏览记录, 这里采用redis来存储
- redis使用数据类型:
	- list:  history_userid:[1,2,3,4] 数字为浏览商品的ID
```python
# 存储浏览记录


# 获取用户的历史浏览记录
# from redis import StrictRedis
# sr = StrictRedis(host='172.16.179.130', port='6379', db=9)
# 这里直接使用django-redis库中的get_redis_connection方法
con = get_redis_connection('default')

history_key = 'history_%d'%user.id

# 获取用户最新浏览的5个商品的id
sku_ids = con.lrange(history_key, 0, 4) # [2,3,1]

# 从数据库中查询用户浏览的商品的具体信息
# goods_li = GoodsSKU.objects.filter(id__in=sku_ids)
#
# goods_res = []
# for a_id in sku_ids:
#     for goods in goods_li:
#         if a_id == goods.id:
#             goods_res.append(goods)

# 遍历获取用户浏览的商品信息
goods_li = []
for id in sku_ids:
    goods = GoodsSKU.objects.get(id=id)
    goods_li.append(goods)

```

### FastDFS分布式文件系统
- 优点: 
	1. 海量存储, 存储容量扩展方便
	2. 重复文件存储一份(文件内容重复)
	3. 结合nginx提高网站访问图片的效率
- 流程:

- Django的对接FastDFS
```python

```

### 用户的购物车记录
- 用户点击添加购物车, 则为用户增加购物车记录
- 当用户访问购物车时, 获取用户购物车记录,进行展示
- 采用redis数据库存储用户购物车记录
- 数据结构:
	- HASH: cart_用户id: {"sku_id1": 数量, "sku_id2": 数量}
```python

# 业务处理:添加购物车记录
conn = get_redis_connection('default')
cart_key = 'cart_%d' % user.id
# 先尝试获取sku_id的值 -> hget cart_key 属性
# 如果sku_id在hash中不存在，hget返回None
cart_count = conn.hget(cart_key, sku_id)
if cart_count:
    # 累加购物车中商品的数目
    count += int(cart_count)

# 校验商品的库存
if count > sku.stock:
    return JsonResponse({'res':4, 'errmsg':'商品库存不足'})

# 设置hash中sku_id对应的值
# hset->如果sku_id已经存在，更新数据， 如果sku_id不存在，添加数据
conn.hset(cart_key, sku_id, count)

```

### 静态页面index.html
- 对于经常访问的页面, 且页面的改动并不是非常频繁的情况下, 把动态页面转换为静态页面, 能提高服务器性能;
- 例如: 对于网站的主页, 可以先渲染, 然后存储为静态页面, 之后再次访问时, 直接访问静态页面即可;
- 静态页面会跟进页面数据的更改, 来更新;
- 这里使用异步任务来生成静态页面
```python
# celery异步任务函数
@app.task
def generate_static_index_html():
    '''产生首页静态页面'''
    # 获取商品的种类信息
    types = GoodsType.objects.all()

    # 获取首页轮播商品信息
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')

    # 获取首页促销活动信息
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品展示信息
    for type in types:  # GoodsType
        # 获取type种类首页分类商品的图片展示信息
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        # 获取type种类首页分类商品的文字展示信息
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        type.image_banners = image_banners
        type.title_banners = title_banners


    # 组织模板上下文
    context = {'types': types,
               'goods_banners': goods_banners,
               'promotion_banners': promotion_banners}

    # 使用模板
    # 1.加载模板文件,返回模板对象
    temp = loader.get_template('static_index.html')
    # 2.模板渲染
    static_index_html = temp.render(context)

    # 生成首页对应静态文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index_html)
        
# 通过管理类中, 数据表格进行增删改等操作时, 会重新更新静态页面

class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或更新表中的数据时调用'''
        super().save_model(request, obj, form, change)

        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        '''删除表中的数据时调用'''
        super().delete_model(request, obj)
        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')
        
class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)

# Nginx
通过Nginx配置index.html来实现, 静态页面的访问

```

### 数据库事务
- 特性:
	- 原子性: 一组事务操作, 要么全部成功, 要么全部失败
	- 一致性: 数据库只能从一种一致性状态变为另外一种一致性状态. (有加就有减)
	- 隔离性: 事务与事务之间独立运行
	- 持久性: 事务操作一旦成功, 作为永久性存在;

- 隔离级别
	- 未提交读: 可读取其他事务未提交的数据的更改, 而读到的数据属于脏数据
	- 已提交读: 读取其他事务提交了的数据, 不可重复读去, 当前事务读取数据后, 其他事务进行了更改, 当当前事务再读取数据时, 数据发生改变.
	- 可重复读: 读取数据不会随其他事务做的更改而改变, 当开启事务进行读取操作, 至到该事务结束,多次读取同一数据值一样. 但会存在"幻读", 例如: 多次读取同一范围数据, 出现幻读时, 会读取先前并未读取到的数据(由于其他事务进行了插入操作). 
	- 可串行化: 最高的隔离级别, 会使得事务之间按顺序执行. 后续事务处于阻塞状态

- 锁
	- 悲观锁: 认为数据一定会被其他所改变, 在对数据进行操作时, 先对数据上一把锁,在进行操作,例如行锁, 表锁,读锁,写锁等;
	- 乐观锁: 认为数据不会更改, 所以在进行数据操作时, 并不会上锁, 而是在提交时, 进行数据在该事务过程中是否被改变.(这一判断机制可通过 版本号机制来进行, 或CAS算法)
	
### 支付宝对接
- 流程:
	1. 用户提交订单, 并支付, 服务器收到请求, 会调用支付宝接口,并返回一个支付宝支付页面;
	2. 用户登录支付宝,进行支付.
	3. 服务器通过不断循环获取支付宝的响应接口,来获取支付结果
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	