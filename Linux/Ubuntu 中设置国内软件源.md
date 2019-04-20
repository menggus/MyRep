## Ubuntu 中设置软件源

### ubuntu 把软件源修改为国内源和更新

-   备份原始文件

    ```shell
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
    ```

-   修改文件并添加国内源

    ```shell
    vi /etc/apt/sources.list	
    ```

-   注释原文件内的源     并添加如下地址     复制代码

    ```shell
    # Ubuntu 官方源
    deb http://archive.ubuntu.com/ubuntu/ gutsy main restricted universe multiverse
    deb http://archive.ubuntu.com/ubuntu/ gutsy-security main restricted universe multiverse
    deb http://archive.ubuntu.com/ubuntu/ gutsy-updates main restricted universe multiverse
    deb http://archive.ubuntu.com/ubuntu/ gutsy-proposed main restricted universe multiverse
    deb http://archive.ubuntu.com/ubuntu/ gutsy-backports main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu/ gutsy main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu/ gutsy-security main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu/ gutsy-updates main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu/ gutsy-proposed main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu/ gutsy-backports main restricted universe multiverse
    ```

    ```shell
    # 阿里云
    deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
    ```

    ```
    # 网易163
    deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
    deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
    deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
    deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
    deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
    deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
    ```

    ```
    # 非官方包可能存在不完整情况，可在尾部添加官方源
    deb http://archive.ubuntu.org.cn/ubuntu-cn/ feisty main restricted universe multiverse
    ```

-   更新源

    ```shell
    sudo apt-get update
    ```

-   ##### 更新软件

    注意：

    由于包与包之间存在各种依赖关系。upgrade只是简单的更新包，不管这些依赖，它不和添加包，或是删除包。而dist-upgrade可以根据依赖关系的变化，添加包，删除包。upgrade:系统将现有的Package升级,如果有相依性的问题,而此相依性需要安装其它新的Package或影响到其它Package的相依性时,此Package就不会被升级,会保留下来. dist-upgrade:可以聪明的解决相依性的问题,如果有相依性问题,需要安装/移除新的Package,就会试着去安装/移除它. (所以通常这个会被认为是有点风险的升级)

    ```shell
    # 谨慎操作
    sudo apt-get dist-upgrade  
    sudo apt-get upgrade
    ```

-   常见的修复安装命令

    ```shell
    sudo apt-get -f install
    ```



---

### 国内主要软件源

#### 企业站

```
1.搜狐：http://mirrors.sohu.com/
2.网易：http://mirrors.163.com/
3.阿里云：http://mirrors.aliyun.com/
4.腾讯：http://Android-mirror.bugly.qq.com:8080/（仅针对APP开发的软件，限流，不推荐）
5.淘宝：http://npm.taobao.org/
```

#### 教育站

```
1.上海交通大学：http://ftp.sjtu.edu.cn/html/resources.xml（部分移动运营商出口状况不佳，无法访问）
2.华中科技大学：http://mirror.hust.edu.cn/（当前已用容量估计：4.83T）
3.清华大学：http://mirrors.tuna.tsinghua.edu.cn/（当前已用容量估计：9.8T）
4.北京理工大学：http://mirror.bit.edu.cn/web/
5.兰州大学：http://mirror.lzu.edu.cn/
6.中国科技大学：http://mirrors.ustc.edu.cn/（当前已用容量估计：21.32T）
7.大连东软信息学院：http://mirrors.neusoft.edu.cn/（当前已用容量估计：2.5T）
8.东北大学：http://mirror.neu.edu.cn/
9.大连理工大学：http://mirror.dlut.edu.cn/
10.哈尔滨工业大学：http://run.hit.edu.cn/html/（部分联通运营商出口状况不佳，无法访问）
11.北京交通大学：http://mirror.bjtu.edu.cn/cn/
12.天津大学：http://mirror.tju.edu.cn（无法访问，ping超时）
13.中国地质大学：http://mirrors.cug.edu.cn/（当前已用容量估计：2.3T）
14.浙江大学：http://mirrors.zju.edu.cn/
15.厦门大学：http://mirrors.xmu.edu.cn/
16.中山大学：http://mirror.sysu.edu.cn/
17.重庆大学：http://mirrors.cqu.edu.cn/（当前已用容量估计：3.93T）
18.北京化工大学：http://Ubuntu.buct.edu.cn/（Android SDK镜像仅供校内使用，当前已用容量估计：1.72T）
19.南阳理工学院：http://mirror.nyist.edu.cn/
20.中国科学院：http://www.opencas.org/mirrors/
21.电子科技大学：http://ubuntu.uestc.edu.cn/（无法访问，ping超时）
22.电子科技大学星辰工作室：http://mirrors.stuhome.net/（当前已用容量估计：1.08T）
23.西北农林科技大学：http://mirrors.nwsuaf.edu.cn/（只做CentOS镜像，当前已用容量估计：140GB） 
24.浙江大学：http://mirrors.zju.edu.cn/
25.台湾淡江大学: http://ftp.tku.edu.tw/Linux/
```

#### 其他

```
1.首都在线科技股份有限公司（英文名Capital Online Data Service）：http://mirrors.yun-idc.com/
2.中国电信天翼云：http://mirrors.ctyun.cn/
3.noc.im：http://mirrors.noc.im/（当前已用容量估计：3.74T）
4.常州贝特康姆软件技术有限公司：http://centos.bitcomm.cn/（只做CentOS镜像，当前已用容量估计：140GB）
5.公云PubYun（母公司为贝特康姆）：http://mirrors.pubyun.com/
6.Linux运维派：http://mirrors.skyshe.cn/（使用阿里云服务器，界面使用浙江大学的模板，首页维护，内容可访问）
7.中国互联网络信息中心：http://mirrors.cnnic.cn/（只做Apache镜像，当前已用容量估计：120GB）
8.Fayea工作室：http://apache.fayea.com/（只做Apache镜像，当前已用容量估计：120GB）
9.开源中国社区 http://mirrors.oss.org.cn/
```

### 软件版

#### 操作系统类

```shell
# Ubuntu
阿里云：http://mirrors.aliyun.com/ubuntu-releases/
网易：http://mirrors.163.com/ubuntu-releases/
搜狐：http://mirrors.sohu.com/ubuntu-releases/（搜狐在12年之后似乎不同步了）
首都在线科技股份有限公司：http://mirrors.yun-idc.com/ubuntu-releases/
```

```shell
# CentOS
网易：http://mirrors.163.com/centos/
搜狐：http://mirrors.sohu.com/centos/
阿里云：http://mirrors.aliyun.com/centos/
```

#### 服务器类

```shell
# Apache
中国互联网络信息中心：http://mirrors.cnnic.cn/apache/
华中科技大学：http://mirrors.hust.edu.cn/apache/
北京理工大学：http://mirror.bit.edu.cn/apache/
```

```shell
# MySQL
北京理工大学：http://mirror.bit.edu.cn/mysql/Downloads/
中国电信天翼云：http://mirrors.ctyun.cn/Mysql/
```

```shell
# PostgreSQL
浙江大学：http://mirrors.zju.edu.cn/postgresql/
```

```shell
# MariaDB
中国电信天翼云：http://mirrors.ctyun.cn/MariaDB/
```

```shell
# VideoLAN
大连东软信息学院：http://mirrors.neusoft.edu.cn/videolan/
中国科技大学：http://mirrors.ustc.edu.cn/videolan-ftp/
```

#### 开发工具类

```shell
# Eclipse
中国科技大学：http://mirrors.ustc.edu.cn/eclipse/
中国科学院：http://mirrors.opencas.cn/eclipse/
东北大学：http://ftp.neu.edu.cn/mirrors/eclipse/，http://mirror.neu.edu.cn/eclipse/
```

```shell
# 安卓SDK
中国科学院：http://mirrors.opencas.ac.cn/android/repository/
南洋理工学院：http://mirror.nyist.edu.cn/android/repository/
中国科学院：http://mirrors.opencas.cn/android/repository/
腾讯：http://android-mirror.bugly.qq.com:8080/android/repository/（限流，不推荐）
大连东软信息学院：http://mirrors.neusoft.edu.cn/android/repository/（同步效果不如中科院的镜像，不推荐）
```

```shell
# Xcode
腾讯：http://android-mirror.bugly.qq.com:8080/Xcode/（从7.2之后不再更新，建议直接从官网下载）
```

###  官方镜像列表状态地址

```
CentOS：http://mirror-status.centos.org/#cn
Archlinux：https://www.archlinux.org/mirrors/status/
Ubuntu：https://launchpad.net/ubuntu/+cdmirrors
Debian：http://mirror.debian.org/status.html
Fedora Linux/Fedora EPEL：https://admin.fedoraproject.org/mirrormanager/mirrors
Apache：http://www.apache.org/mirrors/#cn
Cygwin：https://www.cygwin.com/mirrors.html
```