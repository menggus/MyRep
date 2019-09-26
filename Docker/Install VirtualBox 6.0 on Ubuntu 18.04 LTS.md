How To Install VirtualBox 6.0 on Ubuntu 18.04 LTS

- step1 - 更新软件包为最新版本
```
sudo apt update
sudo apt upgrade
```

- step2 - 建立virtualbox存放仓库
```
# Oracle公钥导入到系统签名的Debian软件包中
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -

# Oracle VirtualBox PPA添加到Ubuntu系统
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian bionic contrib"
# 此命令将在文件末尾添加一个条目到/etc/apt/sources.list中
```

- step3 - 在Ubuntu 18.04上安装VirtualBox
```
sudo apt update
sudo apt install virtualbox-6.0
```

- step4 - 运行VirtualBox
```
virtualbox
```
