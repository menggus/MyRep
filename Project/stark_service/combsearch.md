## 组合搜索

1.组合搜索的使用方式方式
```
class ModelConfig:

	# 给自定义类配置组合搜索字段
	search_field = [
		
	]	
```
2.组合搜索页面展示Row类
```
class Row(object):
    def __init__(self, data_list, option, query_dict):
        """
        元组
        :param data_list:元组或queryset
        """
        self.data_list = data_list
        self.option = option
        self.query_dict = query_dict

    def __iter__(self):
        yield '<div class="whole">'

        tatal_query_dict = self.query_dict.copy()
        tatal_query_dict._mutable = True

        origin_value_list = self.query_dict.getlist(self.option.field)  # [2,]
        if origin_value_list:
            tatal_query_dict.pop(self.option.field)
            yield '<a href="?%s">全部</a>' %(tatal_query_dict.urlencode(),)
        else:
            yield '<a class="active" href="?%s">全部</a>' %(tatal_query_dict.urlencode(),)


        yield '</div>'
        yield '<div class="others">'


        for item in self.data_list: # item=(),queryset中的一个对象
            val = self.option.get_value(item)
            text = self.option.get_text(item)

            query_dict = self.query_dict.copy()
            query_dict._mutable = True

            if not self.option.is_multi: # 单选
                if str(val) in origin_value_list:
                    query_dict.pop(self.option.field)
                    yield '<a class="active" href="?%s">%s</a>' %(query_dict.urlencode(),text)
                else:
                    query_dict[self.option.field] = val
                    yield '<a href="?%s">%s</a>' % (query_dict.urlencode(), text)
            else: # 多选
                multi_val_list = query_dict.getlist(self.option.field)
                if str(val) in origin_value_list:
                    # 已经选，把自己去掉
                    multi_val_list.remove(str(val))
                    query_dict.setlist(self.option.field,multi_val_list)
                    yield '<a class="active" href="?%s">%s</a>' % (query_dict.urlencode(), text)
                else:
                    multi_val_list.append(val)
                    query_dict.setlist(self.option.field, multi_val_list)
                    yield '<a href="?%s">%s</a>' % (query_dict.urlencode(), text)

        yield '</div>'

```
3.组合搜索配置类
```
class Option:
	"""组合搜索配置类"""
	
	def __init__(self, field, condition=None, is_choice=False, text_func=None, value_func=None, is_multi=False):
		"""
			初始化
		:param field: 数据库中表字段
		:param condition: 条件, 查询条件
		:param is_choice: 是否是选择choice类
		:param text_func: 页面组合搜索显示按钮的文字
		:param value_func: 对于choice选择时, 需要选择choice对象 第二个值
		:param is_multi: 对于同一行组合搜索, 是否可以多选
		"""
		self.field = field
		self.is_choice = is_choice
		if not condition:
			condition = {}
		self.condition = condition
		self.text_func = text_func
		self.value_func = value_func
		self.is_multi = is_multi

	def get_queryset(self, _field, model_class, query_dict):
		"""组合搜索"""
		if isinstance(_field, ForeignKey) or isinstance(_field, ManyToManyField):
			row = Row(_field.rel.model.objects.filter(**self.condition), self, query_dict)
		else:
			if self.is_choice:
				row = Row(_field.choices,self,query_dict)
			else:
				row = Row(model_class.objects.filter(**self.condition),self,query_dict)
		return row

	def get_text(self,item):
		if self.text_func:
			return self.text_func(item)
		return str(item)

	def get_value(self,item):
		if self.value_func:
			return self.value_func(item)
		if self.is_choice:
			return item[0]
		return item.pk
			
```



4.组合搜索类
```
class CombSearch:
	"""组合接口类"""
	
	def __init__(self, search_field, request, model_class):
		self.search_field = search_field
		self.request = request
		self.model_class = model_class
		
	def get_filter_condition(self):
		""" 获取组合搜索条件, 用于搜索查询条件的更改"""
		comb_condition = {}
		for option in self.get_list_filter():
			element = self.request.GET.getlist(option.field)
			if element:
			comb_condition['%s__in' % option.field] = element	
		return comb_condition
	
	def get_search_page(self):
		"""获取组合搜索模块页面的显示"""
		for option in self.get_list_filter():
			_field = self.config.model_class._meta.get_field(option.field)
			yield option.get_queryset(_field, self.model_class, self.request.GET)
	
	def get_list_filter(self):
		"""获取组合搜索配置字段"""
		val = []
		val.extend(self.search_field)
		return val

```
### 使用方式
1.	构建搜索配置
```
import Option
    # option类为配置类,通过传入参数进行配置
    search_field = [
        Option("depart", is_multi=True),
        Option("level", is_choice=True, text_func=lambda x:x[1])
    ]

```
2.  使用组合搜索接口
```
import CombSearch
# 在视图内使用,传入对应参数
# search_field: 搜索字段配置
# reqeust: 视图内获取的request对象
# model_class: 搜索的字段模型类
cs = CombSearch(search_field, request, model_class)
# 获取组合搜索的条件
search_condition = cs.get_filter_condition()
# 获取组合搜索的页面
search_page = cs.get_search_page()

```




























