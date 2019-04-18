## Mongdb 数据库的使用

### mongdb 数据库的简介

-   NoSql

    

---

### mongdb数据库的安装

#### 方法一：

-   直接尝试安装:	

    ```shell
    sudo apt-get install -y mongodb-org
    ```

    结果：	E: 无法定位软件包 mongodb-org

#### 方法二：（参考：http://www.runoob.com/mongodb/mongodb-linux-install.html）

-   官网下载：https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.9.tgz

    ```shell
    # curl 下载工具
    curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.9.tgz
    ```

    

-   解压：

    ```shell
    tar -zxvf mongodb-linux-x86_64-3.0.6.tgz  
    ```

-   移动文件：

    ```shell
    sudo mv mongodb-linux-x86_64-ubuntu1604-4.0.9  /usr/local/mongdb
    ```

-   添加到 **PATH** 路径：   

    ```shell
    #  “/usr/local/mongodb”  上一步操作，移动之后的目录
    export PATH=/usr/local/mongodb/bin:$PATH
    ```

-   创建数据库目录：

    -   MongoDB的数据存储在data目录的db目录下，但是这个目录在安装过程不会自动创建，所以你需要手动创建data目录，并在data目录中创建db目录。

        注意：/data/db 是 MongoDB 默认的启动的数据库路径(--dbpath)。

        如果你的数据库目录不是/data/db，也可以通过 --dbpath 来指定。

        ```shell
        mkdir -p /data/db
        ```

-   创建日志目录：

    ```shell
    sudo mkdir -p /var/log/mongodb
    ```



---

### mongodb的启动：

```shell
# 添加环境变量后
sudo mongod --dbpath /data/db --logpath /var/log/mongodb/mongod.log --fork

# 切换到MongoDB的bin目录下
sudo ./mongod --dbpath /data/db --logpath /var/log/mongodb/mongod.log --fork

# 客户端启动
sudo mongo
sudo ./mongo
```

