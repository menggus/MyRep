## Docker 命令
- 测试docker的安装
```
docker run hello-world
```

- 查看已下载的镜像
```
# 查看镜像的属性
docker image ls

# 查看镜像的退出后的状态信息
docker container ls --all
```
- 备忘 docker/镜像和容器操作命令
```
## List Docker CLI commands  docker命令查看与帮助
docker
docker container --help

## Display Docker version and info 版本信息
docker --version
docker version
docker info

## Execute Docker image  执行镜像
docker run hello-world

## List Docker images 列出已下载镜像
docker image ls

## List Docker containers (running, all, all in quiet mode)  列出容器(运行, 所有, 退出的容器ID)
docker container ls  
docker container ls --all
docker container ls -aq
```
