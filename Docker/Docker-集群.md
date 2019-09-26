## docker集群
- 将应用程序部署到群集上，并在多台计算机上运行。通过将多台机器连接到一个称为swarm的“ Dockerized”集群中，可以实现多容器，多机器的应用程序。
- **节点**: 加入集群中的物理计算机或者虚拟计算机均称为节点
- **集群管理器**:集群中唯一可以执行命令或授权其他计算机作为工作人员加入群集的计算机. 加入的节点计算机只负责提供算力, 而不能负责管理集群
- 集群的方案: 虚拟机集群和物理集群
### 通过虚拟机创建集群
- Install **docker-machine**
- https://github.com/docker/machine/releases/
```
# 安装
curl -L https://github.com/docker/machine/releases/download/v0.16.1/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
chmod +x /tmp/docker-machine &&
sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

# 查看
docker-machine version

[output info]:
docker-machine version 0.16.1, build cce350d7
```

- Install **VirtualBox** on Ubuntu 18.04
```
https://tecadmin.net/install-virtualbox-on-ubuntu-18-04/
```

- 创建虚拟机myvm1 & myvm2
```
# 直接运行会下载 , 且较慢
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2

# 这里通过google下载, 然后进行指定ios路径创建
docker-machine create myvm1 -d virtualbox --virtualbox-boot2docker-url=/home/gram/.docker/machine/cache/boot2docker.iso 
docker-machine create myvm2 -d virtualbox --virtualbox-boot2docker-url=/home/gram/.docker/machine/cache/boot2docker.iso 

# 查看通过virtualbox创建的集群节点
docker-machine ls

[output info]:
NAME    ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
myvm1   -        virtualbox   Running   tcp://192.168.99.100:2376           v18.06.1-ce   
myvm2   -        virtualbox   Running   tcp://192.168.99.101:2376           v18.06.1-ce   

```
- 初始化群组并添加节点
	- 第一台(myvm1)充当管理器,执行管理命令并验证工作节点的加入
	- 第二台(myvm2)充当工作节点

```
# 初始化
#使用ssh发送指令方式，发生错误　（未找到解决方法）
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"

[output info]:
sh: syntax error: unexpected end of file
exit status 2

# 先直接连接myvm1
docker-machine ssh myvm1

# 再执行初始化操作
docker swarm init --advertise-addr 192.168.99.100:2377

# 连接myvm2加入群组
# 首先查看加入作为 工作节点的命令, https://www.cnblogs.com/songxingzhu/p/10669497.html
docker swarm join-token worker  # 在manager运行

[output info]:
To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5oru6i4crjaatw8r9sm2h055nrulbhj9iukurfouqfgwuwz7vq-0l41fmxdeq2zgwf78zpfh1wi4 192.168.99.100:2377

# 查看要加入作为管理节点的命令
docker swarm join-token manager

[output info]:
To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5oru6i4crjaatw8r9sm2h055nrulbhj9iukurfouqfgwuwz7vq-d7cjgcf4hp3pn135ynvst2k3g 192.168.99.100:2377

# 节点加入群, 作为工作节点
docker swarm join --token SWMTKN-1-5oru6i4crjaatw8r9sm2h055nrulbhj9iukurfouqfgwuwz7vq-0l41fmxdeq2zgwf78zpfh1wi4 192.168.99.100:2377

# 在管理器上查看节点列表
docker node ls

[output info]:
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
187wtx2rahw6f2dmctwntnnlt *   myvm1               Ready               Active              Leader              18.06.1-ce
1e2apharmmbut1pq60me5qfhe     myvm2               Ready               Active                                  18.06.1-ce

```

### 在群体集群上部署您的应用
- 配置与管理器对话的shell
```
# 获取对话连接命令
docker-machine env myvm1

[output info]:
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/sam/.docker/machine/machines/myvm1"
export DOCKER_MACHINE_NAME="myvm1"
# Run this command to configure your shell:
# eval $(docker-machine env myvm1)  # 这个就是对话连接命令

# 运行命令, 与docker相关命令就能与myvm1进行对话了, 就如同在myvm1的shell中执行命令
eval $(docker-machine env myvm1)

# 退出回话配置
 eval $(docker-machine env -u)
```
- 部署应用
```
# 这里的命令虽然不是在myvm1的shell执行, 经过上一步骤的配置, 就如同在myvm1执行一样
# service_taoberry自定义服务名, path/docker-compose.yml (这里是在该文件夹下运行的)
docker stack deploy -c docker-compose.yml service_taoberry

# 查看部署结果

[output info]:

ID                  NAME                IMAGE                                  NODE                DESIRED STATE       CURRENT STATE              ERROR               PORTS
590lvclhsmw3        taoberry_web.1      taoberry/first_repository:test_image   myvm2               Running             Preparing 12 seconds ago                       
ni4075fs9c7b        taoberry_web.2      taoberry/first_repository:test_image   myvm1               Running             Running 11 seconds ago                         
bgd42y3ud373        taoberry_web.3      taoberry/first_repository:test_image   myvm1               Running             Running 11 seconds ago                         
w47pv94apzlm        taoberry_web.4      taoberry/first_repository:test_image   myvm2               Running             Preparing 12 seconds ago                       
h5jkaz7nmzi4        taoberry_web.5      taoberry/first_repository:test_image   myvm1               Running             Running 11 seconds ago                         
  
# 注意: CURRENT STATE: Preparing的情况
# 一般为节点并没有服务所需的镜像资源,需要从  仓库进行  拉取, 所以跟进网络情况, 是比较耗时的
# 解决办法, 就是   在节点提前拉取对应服务的镜像
```




### 命令
```
# 节点加入操作相关token
swarm join-token ：可以查看或更换join token。
docker swarm join-token worker：查看加入woker的命令。
docker swarm join-token manager：查看加入manager的命令
docker swarm join-token --rotate worker：重置woker的Token。
docker swarm join-token -q worker：仅打印Token。
```

