## Docker - Stack(堆栈)

- 堆栈: 一组共享依赖关系的相互关联的服务, 可以一起进行整理和扩展; 单个堆栈能够定义和协调整个应用程序的功能(尽管非常复杂的应用程序可能要使用多个堆栈)

### 添加新服务并重新部署

- 编辑docker-compose.yml文件, 新增服务 **visulizer**

- volumes密钥，使可视化程序可以访问Docker的主机套接字文件

- placement密钥，确保此服务仅在群集管理器上运行，而不是工人

  ```
  version: "3"
  services:
    web:
      # replace username/repo:tag with your name and image details
      image: taoberry/first_repository:test_image
      deploy:
        replicas: 5
        resources:
          limits:
            cpus: "0.1"
            memory: 50M
        restart_policy:
          condition: on-failure
      ports:
        - "80:80"
      networks:
        - webnet
    visualizer:  # a service
      image: dockersamples/visualizer:stable
      ports:
        - "8080:8080"
      # volumes密钥，使可视化程序可以访问Docker的主机套接字文件
      volumes:  
        - "/var/run/docker.sock:/var/run/docker.sock"
      deploy:
       # placement密钥，确保此服务仅在群集管理器上运行，而不是工人
        placement:
          constraints: [node.role == manager]
      networks:
        - webnet
  networks:
    webnet:
  ```

- 确保与管理器myvm1的会话

  ```shell
  # 配置myvm1会话(ACTIVE=*)
  eval $(docker-machine env myvm1)
  
  docker-machine ls
  
  [output]:
  NAME    ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
  myvm1   *        virtualbox   Running   tcp://192.168.99.100:2376           v18.06.1-ce   
  myvm2   -        virtualbox   Running   tcp://192.168.99.101:2376           v18.06.1-ce   
  myvm3   -        virtualbox   Running   tcp://192.168.99.102:2376           v18.06.1-ce  
  
  ```

- 重新部署

  ```shell
  # 提醒: 最好提前在对应节点上pull 镜像, 否则可能服务达到启动数量需要一定时间
  docker stack deploy -c docker_/docker-compose.yml taoberry
  ```

### 添加redis服务

- 编辑docker-compose.yml

- 持久化注意:

  - `redis` 总是在管理器上运行，因此它始终使用相同的文件系统
  - volumes配置   /data 在容器内部访问主机文件系统中的任意目录，Redis 在该目录中存储数据。

  ```shell
  version: "3"
  services:
    web:
      # replace username/repo:tag with your name and image details
      image: taoberry/first_repository:test_image
      deploy:
        replicas: 9
        resources:
          limits:
            cpus: "0.1"
            memory: 50M
        restart_policy:
          condition: on-failure
      ports:
        - "80:80"
      networks:
        - webnet
    visualizer:  # a service
      image: dockersamples/visualizer:stable
      ports:
        - "8080:8080"
      volumes:  # 
        - "/var/run/docker.sock:/var/run/docker.sock"
      deploy:
        placement:
          constraints: [node.role == manager]
      networks:
        - webnet
    # 添加新的服务redis
    redis:
      image: redis
      ports:
        - "6379:6379"
      # 存储在./data指定主机上的文件将保留，从而实现连续性。
      volumes:
        - "/home/docker/data:/home/docker/data"  # 目标主机是否存在文件夹
      deploy:
        # Redis服务施加的放置约束，确保它始终使用同一主机
        placement:
          constraints: [node.role == manager]
      command: redis-server --appendonly yes
      networks:
        - webnet
  networks:
    webnet:
  ```

- 创建./data目录

  ```shell
  docker-machine ssh myvm1 "mkdir ./data"
  ```

- 再次部署

  ```
  docker stack deploy -c docker_/docker-compose.yml taoberry
  ```

  