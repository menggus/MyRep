## Virtualenv虚拟环境

概论：虚拟环境其实就是对真实pyhton环境的复制，这样我们在复制的python环境中安装包就不会影响到真实的python环境。通过建立多个虚拟环境，在不同的虚拟环境中开发项目就实现了项目之间的隔离。

#### 创建

```shell
# 安装虚拟环境
sudo pip3 install virtualenv 

# 安装虚拟环境扩展包	
# 安装虚拟环境包装饰器的目的是使用更加简单的命令来管理虚拟环境
sudo pip3 install virtualenvwrapper

# 修改用户家目录下的配置文件.bashrc,添加如下内容
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# source .bashrc命令使配置文件生效
source .bashrc

# 创建虚拟环境	
# 格式：mkvirtualenv -p python3 虚拟环境名称
# 以python3 来创建环境
mkvirtualenv -p python3 Myspider

# 退出虚拟环境
deactivate

# 查看 
# workon 两次tab键  
# 使用虚拟环境
workon Mysipder

# 删除虚拟环境
# 先退出虚拟环境，再删除，如下：
deactivate
rmvirtualenv py_django

# 虚拟环境下的包操作
# pip install 包名称

# 查看所有已安装的包
pip list  
pip freeze
```



