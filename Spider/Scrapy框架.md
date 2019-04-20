## Scrape框架

### 概述：

![1555767561319](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555767561319.png)

![1555767722758](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555767722758.png)

### 安装

参考官方安装：<https://docs.scrapy.org/en/latest/>

### 文件目录

![1555750209130](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555750209130.png)

```python
scrapy.cfg ：项目的配置文件
mySpider/ ：项目的Python模块，将会从这里引用代码
mySpider/items.py ：项目的目标文件
mySpider/pipelines.py ：项目的管道文件
mySpider/settings.py ：项目的设置文件
mySpider/spiders/ ：存储爬虫代码目录
```

### Scrapy 关于日志的设置

```
# 日志设置在项目settings.py文件中
LOG_LEVEL = "WARNING"  # 设置日志的输出等级
LOG_FILE = "./log.log"  # 设置日志的保存文件位置
```

###  创建爬虫（mySpider/spiders/ 文件目录下）

```shell
# 命令行：创建爬虫，减少固定代码的输入 
# 格式：scrapy genspider 爬虫名	爬取的域名
scrapy genspider itcast "itcast.cn"

# 命令行：运行爬虫
# 格式：scrapy crawl 爬虫名
scrapy crawl itcast
```

```python
"""
	项目中的爬虫
	命令行创建：scrapy genspider 爬虫名	域名
"""
import scrapy

class ItcastSpider(scrapy.Spider):
    
    name = 'itcast'  # 爬虫的识别标识，scrapy通过该name识别爬虫，必须唯一
    allowed_domains = ['itcast.cn']  # 爬取域名的范围，约束爬虫只能爬取该域名下的网页，不存在url会被忽略
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]  # 开始爬取的url地址列表

    def parse(self, response):
        """
        解析的方法，爬取初始url地址下载后，会被调用
        response： 初始url地址的响应对象
        """
         # 提取数据
        data_list = response.xpath("//div[@class='tea_con']//li")

        for item in data_list:
            data_dict = {}

            data_dict["name"] = item.xpath(".//h3/text()").extract_first()
            data_dict["grade"] = item.xpath(".//h4/text()").extract_first()
            data_dict["introduce"] = item.xpath(".//p/text()").extract_first()

            yield data_dict  # 生成数据  经scrapy控制传递给pipeline管道

```

### 项目管道（mySpider/pipelines.py）

```python
# 数据的处理，存储
import json

class MyspiderPipeline(object):

    def process_item(self, item, spider):
        print(spider.name)
        with open("teacher.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(item, ensure_ascii=False, indent=4))
            f.write("\n")
        return item
```

