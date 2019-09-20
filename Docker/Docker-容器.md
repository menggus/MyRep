## Docker 容器
- Dockerfile 指令
```
我们需要了解一些基本的Dockerfile 指令，Dockerfile 指令为 Docker 引擎提供了创建容器映像所需的步骤。这些指令按顺序逐一执行。以下是有关一些基本 Dockerfile 指令的详细信息。

1.FROM
FROM 指令用于设置在新映像创建过程期间将使用的容器映像。
格式：FROM 
示例：
FROM nginx
FROM microsoft/dotnet:2.1-aspnetcore-runtime


2.RUN
RUN 指令指定将要运行并捕获到新容器映像中的命令。 这些命令包括安装软件、创建文件和目录，以及创建环境配置等。
格式：
RUN ["", "", ""]
RUN
示例：
RUN apt-get update
RUN mkdir -p /usr/src/redis
RUN apt-get update && apt-get install -y libgdiplus
RUN ["apt-get","install","-y","nginx"]

注意：每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，例如：RUN apt-get update && apt-get install -y libgdiplus。在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。使用换行符时，可能会遇到一些问题，具体可以参阅下节的转义字符。

 
3.COPY
COPY 指令将文件和目录复制到容器的文件系统。文件和目录需位于相对于 Dockerfile 的路径中。
格式：
COPY
如果源或目标包含空格，请将路径括在方括号和双引号中。
COPY ["", ""]
示例：
COPY . .
COPY nginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html
COPY hom* /mydir/
 

4.ADD
ADD 指令与 COPY 指令非常类似，但它包含更多功能。除了将文件从主机复制到容器映像，ADD 指令还可以使用 URL 规范从远程位置复制文件。
格式：
ADD<source> <destination>
示例：
ADD https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe /temp/python-3.5.1.exe
此示例会将 Python for Windows下载到容器映像的 c:\temp 目录。

 
5.WORKDIR
WORKDIR 指令用于为其他 Dockerfile 指令（如 RUN、CMD）设置一个工作目录，并且还设置用于运行容器映像实例的工作目录。
格式：
WORKDIR
示例：
WORKDIR /app

 
6.CMD
CMD指令用于设置部署容器映像的实例时要运行的默认命令。例如，如果该容器将承载 NGINX Web 服务器，则 CMD 可能包括用于启动Web服务器的指令，如 nginx.exe。 如果 Dockerfile 中指定了多个CMD 指令，只会计算最后一个指令。
格式：
CMD ["<executable", ""]
CMD
示例：
CMD ["c:\\Apache24\\bin\\httpd.exe", "-w"]
CMD c:\\Apache24\\bin\\httpd.exe -w

 
7.ENTRYPOINT
配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。每个 Dockerfile 中只能有一个ENTRYPOINT，当指定多个时，只有最后一个起效。
格式：
ENTRYPOINT ["", ""]
示例：
ENTRYPOINT ["dotnet", "Magicodes.Admin.Web.Host.dll"]

 
8.ENV
ENV命令用于设置环境变量。这些变量以”key=value”的形式存在，并可以在容器内被脚本或者程序调用。这个机制给在容器中运行应用带来了极大的便利。
格式：
ENV==...
示例：
ENV VERSION=1.0 DEBUG=on NAME="Magicodes"

 
9.EXPOSE
EXPOSE用来指定端口，使容器内的应用可以通过端口和外界交互。
格式：
EXPOSE
示例：
EXPOSE 80

```
- Dockerfile文件指令优化
```
# '\'优化
Linux系统中Dockerfile中 '\'可作为换行, 但在windows系统 '\'表示路径 ,在window中可能出错
# 修改换行转义字符: 必须在 Dockerfile 最开始的行上放置一个转义分析程序指令
FROM microsoft/windowsservercore
注意: 只有两种字符可做转译换行 '和\

1. 选择合适的基础镜像
一个合适的基础镜像是指能满足运行应用所需要的最小的镜像，理论上是能用小的就不要用大的，能用轻量的就不要用重量级的，能用性能好的就不要用性能差的

2. 优化指令顺序
Docker会缓存Dockerfile中尚未更改的所有步骤，但是，如果更改任何指令，将重做其后的所有步骤。也就是指令3有变动，那么4、5、6就会重做。因此，我们需要将最不可能产生更改的指令放在前面，按照这个顺序来编写dockerfile指令。这样，在构建过程中，就可以节省很多时间。比如，我们可以把WORKDIR、ENV等命令放前面，COPY、ADD放后面。

3. 合并指令	
每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，例如：RUN apt-get update && apt-get install -y libgdiplus。

4. 删除多余文件和清理没用的中间结果
这点很易于理解，通常来讲，体积更小，部署更快！因此在构建过程中，我们需要清理那些最终不需要的代码或文件。比如说，临时文件、源代码、缓存等等。

5. 使用 .dockerignore
.dockerignore文件用于忽略那些镜像构建时非必须的文件，这些文件可以是开发文档、日志、其他无用的文件。
例如:

.dockerignore
.evn
.git
.gitignore

```

## 构建示例
- 构建Dockerfile
```
# Use an official Python runtime as a parent image
# 使用Python运行时作为父镜像
FROM python:2.7-slim

# Set the working directory to /app
# 设置工作目录
WORKDIR /app

# Copy the current directory contents into the container at /app
# 复制当前目录内容到容器文件系统
COPY . /app

# Install any needed packages specified in requirements.txt
# 安装需要的依赖
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# 设置容器对外的端口
EXPOSE 80

# Define environment variable
# 定义环境
ENV NAME World

# Run app.py when the container launches
# 当容器导入执行命令, 通过Python来执行app.py
CMD ["python", "app.py"]
```

- 创建Docker镜像
```
# build创建镜像, 会查找Dockerfile来进行创建,  命令行末尾的.表示  在当前path下查找
docker build --tag=friendlyhello .

# 查看镜像
docker image ls

[output]:

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
friendlyhello       latest              7e77fe4b6380        2 minutes ago       148MB
python              2.7-slim            f462855313cd        7 days ago          137MB
hello-world         latest              fce289e99eb9        8 months ago        1.84kB

# 这里标签TAG默认为 latest, 创建tag完整语法为
# image_name:version
--tag=friendlyhello:v0.0.1
```
- 使用Linux系统, 并有代理服务器时需要设置  和 DNS设置再进行build命令
```
# 代理服务器设置, 在Dockerfile中添加以下行
# Set proxy server, replace host:port with values for your servers
ENV http_proxy host:port
ENV https_proxy host:port

# 设置自己的DNS服务器, 更改Docker守护程序的DNS设置, 编辑/etc/docker/daemon.json
{
  "dns": ["your_dns_address", "8.8.8.8"]  # 配置多个dns, 第一个不可用, 可以使用第二个google的
}
# 保存daemon.json并重新启动docker服务生效
sudo service docker restart
# 重试运行该build命令

# MTU设置: 默认网桥上的MTU（默认值为1500）大于主机外部网络的MTU，则pip失败
# 通过/etc/docker/daemon.json使用mtu密钥编辑（或创建）配置文件来设置docker bridge网络的MTU以匹配主机的MTU 
{
  "mtu": 1450
}
# 保存daemon.json并重新启动docker服务生效
sudo service docker restart
# 重试运行该build命令
```
- 运行应用程序
```
# 计算机的端口4000映射到容器的已发布端口80 -p
docker run -p 4000:80 friendlyhello

[output]:
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

# 提示信息表示运行在  http://0.0.0.0:80/ 这个为容器对外的接口地址
# 而之前是映射到了本机地址 4000端口, 所以地址为下
http://localhost:4000/


# 分离模式运行应用程序, 不需要开启终端, 以类似服务方式运行  <后台运行>
docker run -d -p 4000:80 friendlyhello

[outpur]:
71489fedc31007ce53e63d5c769408ff1031836217ea15c6389e783ede00dc39
# 输出  容器的id

# 停止运行
docker container ls

[output]:
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                  NAMES
71489fedc310        friendlyhello       "python app.py"     2 minutes ago       Up 2 minutes        0.0.0.0:4000->80/tcp   sweet_germain

docker container stop sweet_germain 
docker container stop 71489fedc310
# 均可
```
- 推送镜像去存储库
```
# 注册docker ID
# 登录
docker login

# 标记镜像
# 语法: docker tag image username/repository:tag
docker tag friendlyhello:latest taoberry/first_repository:test_image

# 查看镜像
docker image ls

[output]:
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
friendlyhello               latest              7e77fe4b6380        2 hours ago         148MB
taoberry/first_repository   test_image          7e77fe4b6380        2 hours ago         148MB

# 上传镜像至存储库
 docker push taoberry/first_repository

# 从登录的远程存储库拉取运行
docker run -p 4000:80 taoberry/first_repository:test_image 

无论在哪里docker run执行，它都会提取您的镜像，以及Python和所有依赖项requirements.txt，并运行您的代码。它们都在一个整洁的小包中一起旅行，你不需要在主机上安装任何东西让Docker运行它

```
- 本栏命令汇总
```
docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a             # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>         # Force shutdown of the specified container
docker container rm <hash>        # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>            # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry

```