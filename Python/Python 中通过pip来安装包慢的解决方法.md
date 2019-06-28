### Python 中通过pip来安装包慢的解决方法

#### 临时解决办法

```shell
# 通过使用国内的源
# 例:  清华: https://pypi.tuna.tsinghua.edu.cn/simple
# pip直接装速度在 < 100kb/s   清华能到:1.1mb/s
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 安装包
```

#### 长久解决

```shell
# 通过配置下载源
# 创建一个隐藏目录名字是  .pip
mkdir ~/.pip
# 进入pip的目录创建一个pip.conf的文件
cd .pip====》touch pip.conf
# 编辑pip.conf文件
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host = pypi.douban.com
```

