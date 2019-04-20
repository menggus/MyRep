## MongoDB的使用

### 客户端命令：

```shell
# 启动数据库客户端
sudo ./mongo

# 查看所有数据库
show databases
show dbs

# 使用数据库
use 数据库名

# 当前数据库
db

# 删除数据库
db.dropDatabase()
```

### MongoDB数据库存储的数据类型：

```markdown
Object ID： ⽂档ID
String： 字符串    最常⽤， 必须是有效的UTF-8
Boolean： 存储⼀个布尔值， true或false
Integer： 整数可以是32位或64位， 这取决于服务器
Double： 存储浮点值
Arrays： 数组或列表， 多个值存储到⼀个键
Object： ⽤于嵌⼊式的⽂档， 即⼀个值为⼀个⽂档
Null： 存储Null值
Timestamp： 时间戳， 表示从1970-1-1到现在的总秒数
Date： 存储当前⽇期或时间的UNIX时间格式
```

### 集合collection

```shell
# 注意：向不存在的集合中第⼀次加⼊数据时， 集合会被创建出来
# 手动创建集合：
# 参数capped： 默认值为false表示不设置上限,值为true表示设置上限
# 参数size： 当capped值为true时， 需要指定此参数， 表示上限⼤⼩,当⽂档达到上限时， 会将之前的数据覆盖， 单位为字节
db.createCollection(name,options)
db.createCollection("stu")
db.createCollection("sub", { capped : true, size : 10 } )

# 查看集合：
show collections

# 删除集合：
db.集合名称.drop()

# 注意点：
# 1.创建⽇期语句如下 ：参数的格式为YYYY-MM-DD
new Date('2017-12-20')
# 2.每个⽂档都有⼀个属性， 为_id， 保证每个⽂档的唯⼀性
# 可以⾃⼰去设置_id插⼊⽂档，如果没有提供， 那么MongoDB为每个⽂档提供了⼀个独特的_id， 类型为objectID

# 3._id 的格式：
objectID是⼀个12字节的⼗六进制数：
	前4个字节为当前时间戳
    接下来3个字节的机器ID
    接下来的2个字节中MongoDB的服务进程id
    最后3个字节是简单的增量值
```

### 数据的插入

![1555580152554](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555580152554.png)

```shell
# db.集合名称.insert(document)
db.person.insert({name: "小赵", age: 54})

# 指定_id插入数据
db.person.insert({_id: 20190418, name: "小刘", age: 31})

# 插⼊⽂档时， 如果不指定  _id参数， MongoDB 会为⽂档分配⼀个唯⼀的 ObjectId, 如下：
"_id" : ObjectId("5cb84091feb8b5e188fa453b")
```

### 数据的保存

![1555580916914](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555580916914.png)

```shell
# db.集合名称.save(document)
# 如果⽂档的_id已经存在则修改， 如果⽂档的_id不存在则添加
# 1._id存在，修改 如上图
# 2._id不存在，添加
```

### 数据的更新

![1555583093695](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555583093695.png)

```shell
# db.集合名称.update(<query> ,<update>,{multi: <boolean>})
# <query>: 查询条件
# <update>: 更新数据
# {multi: <boolean>}: 可选，默认是false，表示只更新找到的第⼀条记录， 值为true表示把满⾜条件的⽂档全部更新

# 更新小明数据
db.person.update({name:"小明"}, {name:"小明明", age:20})
# 设置单个字段，其他字段不变
db.person.update({name:"小明明"}, {$set:{age:18}})
# 更新全部,把所有的document都更新为 {name:"小小",age:0}
db.person.update({},{$set:{name:"小小",age:0}},{multi:true})  # 注意：multi书写
# 更新字段的名称
db.person.update({},{$rename:{"honetowm":"hometown"}},{multi:true})

# 注意："multi update only works with $ operators"
```

### 数据的删除

```shell
# db.集合名称.remove(<query>,{justOne: <boolean>})
# <query>: 查询条件
# {justOne: <boolean>}：删除一条条数 true  or  删除多条  默认 flase 删除多条
db.person.remove({name:"小小"},{justOne:true})  # 删除一条
```

### 数据的查询



```shell
# db.集合名称.find()  查看所有document
db.person.find()

# db.集合名称.find({条件})	返回所有符合条件
db.person.find({honetowm:"sz"})

# db.集合名称.findOne({条件})	  只返回第一个
db.person.findOne({honetowm:"sz"})

# pretty()   查询美化输出
db.person.find({honetowm:"sz"}).pretty()
# 如下输出
> db.person.find({honetowm:"sz"}).pretty()
{
	"_id" : ObjectId("5cb86bdde2fb78fe4ce3096b"),
	"name" : "xiaoxiao",
	"age" : 18,
	"honetowm" : "sz"
}
{
	"_id" : ObjectId("5cb86c19e2fb78fe4ce3096c"),
	"name" : "dada",
	"age" : 34,
	"honetowm" : "sz"
}
```

###   运算

```shell
# 比较运算符(英文的首字母)
# 小于：$lt	小于等于：$lte	大于:$gt	大于等于：$gte	不等于：$ne		默认：等于
# 查询年龄大于20的人
db.person.find({age:{$gt:20}})


# 逻辑运算
# 逻辑与(and):	{条件1，条件2}  -->  查询条件格式
# and:	查询年龄大于20 且家乡在sz的人
db.person.find({age:{$gt:20},honetowm:"sz"})
# 逻辑或(or):	{$or:[{条件一}，{条件二}]}  -->  查询条件格式
db.person.find({$or:[{age:{$lt:30}},{hometowm:"sz"}]})
# 查询年龄⼤于18或性别为男⽣， 并且姓名是郭靖
db.stu.find({$or:[{age:{$gte:18}},{gender:true}],name:'郭靖'})


# 范围运算
# 格式：$in:[a,b,c]  可选值：a, b, c
db.person.find({age:{$in:[18, 20, 30]}})


# 正则运算
# 格式：字段:/正则表达式/		字段:{$regex:'正则表达式'}
db.person.find({name:/^xiao/})
db.person.find({name:{$regex:'^xiao'}})


# limit &  skip
# limit： 用于读取指定数量的文档
db.person.find().limit(2)  # 读取两条
# skip：	 用于跳过指定数量的文档
db.person.find().skip(2)
# limit & skip	组合使用，注意：先skip().limit()效率更高
db.person.find().skip(2).limit(2)


# 自定义查询
# 格式：$where: function(){	条件	}  js
# 查询年龄大于20的人
db.person.find({
    $where: function(){
        return this.age>20;
	}
})
```

### 投影

```shell
# 查询返回的结果,只选择必要字段输出
# 格式：db.集合名称.find({条件},{字段1：1, 字段2: 0}) 	<默认为 1 >	1-->显示；	0-->不显示  
# _id值:	默认显示，不显示需设置为 0
db.person.find({}, {_id:0})
```

### 排序

```shell
# 对字段进行排序
# 格式：db.集合名称.find().sort({字段1:1，字段2,：-1})	1-->升序	-1-->降序
db.person.find().sort({age:1})	# 年龄按升序排序
db.person.find().sort({age:1, hometowm:-1})	# 先年龄升序排序，再家乡降序排序
```

### 统计

```shell
# 统计个数
# 格式： db.集合名称.find({条件}).count()		db.集合名词.count({条件})
db.person.find().count()
db.person.find({age:{$lt:30}}).count()
db.person.count({age:{$lt:30}})
```

### 消除重复

```shell
# 消除重复
# 格式: db.person.distinct(去重字段, {条件})
db.person.distinct('age')  # 对所有进行年龄去重

# 带条件去重
db.person.distinct('hometowm', {age:{$gte:20}})
```

### 聚合

-   聚合（aggregate）：是基于数据处理的聚合管道，每个文档通过一个由多个阶段组成的管道，可以对每个阶段的管道进行分组，过滤等功能，然后经过一系列的处理，输出相应的结果。
-   ![1555655220840](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555655220840.png)
-   ![1555656754989](C:\Users\tao_cp\AppData\Roaming\Typora\typora-user-images\1555656754989.png)

```shell
# 格式: db.集合名称.aggregate( {管道：{表达式}} )


# 管道：文档处理完成通过管道进行下一次处理
# $group: 将集合中的文档分组，用于统计结果
# $match: 过滤数据，只输出符合条件的文档
# $project: 修改输入文档的结构，如重命名，增加，删除字段，创建计算结果
# $sort: 将输入文档排序后输出
# $limit: 限制聚合管道返回的文档数
# $skip: 跳过指定数量的文档数
# $unwind: 将数组类型的字段进行拆分

# 文档处理表达式： 处理文档并输出
# $sum: 计算总和	$sum:1 表示以1倍计数
# $avg: 计算平均值  
# $min: 获取最小值
# $max: 获取最大值
# $push: 在结果文档中插入一值到一个数组中
# $first: 根据资源文档的排序获取第一个文档的数据
# $last: 根据资源文档的排序获取最后一个文档数据

# 添加性别字段
db.person.update({$or:[{name:/^xia/}, {name:/^qi/}]}, {$set:{gender:1}}, {multi:true})


# $group  分组
# 格式：
db.集合名称.aggregate({
    $group:{
        _id: '$gender', # 分组依据 引号
        counter: {$sum:1}
    }
})
# 根据性别来分组,并计算每组平均年龄
# {$sum:1}表示以1来计算，根据分组后每一组元素个数乘以 1来求和
db.person.aggregate(
	{$group:{_id:'$gender',counter:{$sum:1}, avg_age:{$avg:"$age"}}}
)
# 按多个字段分组，可以进行去重
db.prov.aggregate( 
	{$group:{_id:{country:"$country", province:"$province",user_id:"$user_id"}}} 
)
# 对去重后的数据，再进行分组
db.prov.aggregate(
	{$group:{_id:{country:"$country",province:"$province",user_id:"$user_id"}}},
	{$group:{_id:{country:"$_id.country", province:"$_id.province"}}}
)
# 统计分组下user_id的个数
db.prov.aggregate(
	{$group:{_id:{country:"$country", province:"$province", user_id:"$user_id"}}},
	{$group:{_id:{country:"$_id.country",province:"$_id.province"}, counter:{$sum:1}}},
	{$project:{country:"$_id.country",province:"$_id.province",counter:1, _id:0}}
)


# $project 修改输出、输入
# 不显示_id, 显示gender
db.person.aggregate(
	{$group:{_id:"$gender", counter:{$sum:1}, avg_age:{$avg:"$age"}}},
	{$project:{gender:"$_id", counter:1, avg_age:1, _id:0}}
)


# $sort   排序  1 -->升序   -1 -->降序
# $limit  &  $skip
# 统计男生，女生人数，按人数升序，取第二条数据
db.person.aggregate(
	{$group:{_id:"$gender", counter:{$sum:1}}},
	{$sort:{counter:1}},
	{$skip:1},
	{$limit:1},
	{$project:{gender:"$_id", counter:1, _id:0}}
)

# $unwind 对文档中数组字段进行拆分
# 格式：{$unwind:"$字段"}
# 注意：如果需要保留字段为空或者null的数据，需要采用了另外一种格式
# 格式：{$unwind:{path:"$字段名", preserveNullAndEmptyArrays: <true or false>}} 防止数据丢失
# 数据库中有一条数据：{"username":"Alex","tags": ['C#','Java','C++']}，如何获取该tag列表的长度？
db.dbtes.aggregate(
	{$unwind:"$tags"}   # 拆分
)
db.dbtes.aggregate(
	{$unwind:"$tags"},
	{$group:{_id:null, counter:{$sum:1}}}  # 统计
	
)
db.dbtes.aggregate(
	{$unwind:"$tags"},
	{$group:{_id:null, counter:{$sum:1}}},
	{$project:{counter:1,_id:0}}	# 输出
)
```



### 创建索引

```shell
# 索引：给字段简历索引，来提高查询效率
# 创建索引方法：
db.集合名称.ensureIndex({"字段名":<1 or -1>})  1-- 表示升序  -1 --表示降序

# db 操作.explain('executionStats') 可查看 查询时间，状态等
db.集合名称.find().explain('executionStats')

# 索引创建： 默认情况下，创建的均不是唯一索引。
# 唯一索引创建：需要加上 {"unique":true}
b.集合名称.ensureIndex({"字段名":1},{"unique":true})

# 创建唯一索引并消除重复
db.集合名称.ensureIndex({"name":1},{"unique":true,"dropDups":true})

# 创建联合索引
db.集合名称.ensureIndex({"name":1, "age":1})

# 查看当前集合的所有索引
db.集合名.getIndexes({"字段名":1})
```



### 数据的备份与数据恢复

备份：

```shell
# 格式：mongodump -h dbhost -d dbname -o dbdirectory
# 例：
mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak
```

-   -h	数据库地址，可以指定端⼝号   <192.168.196.128:27017>
-   -d    数据库名称   < test1 >
-   -o    数据库备份文件目录，存放位置  < ~/Desktop/test1bak >

恢复：

```shell
# 格式：mongorestore -h dbhost -d dbname --dir dbdirectory
# 例
mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1
```

-   -h： 服务器地址
-   -d： 需要恢复的数据库实例
-   --dir： 备份数据所在位置











