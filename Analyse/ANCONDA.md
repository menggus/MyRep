##  ANCONDA

### 概述

-   Anaconda指的是一个开源的[Python](https://baike.baidu.com/item/Python)发行版本，其包含了conda、Python等180多个科学包及其依赖项。 [1]  因为包含了大量的科学包，Anaconda 的下载文件比较大（约 531 MB），如果只需要某些包，或者需要节省带宽或存储空间，也可以使用**Miniconda**这个较小的发行版（仅包含conda和 Python）。
-   利于安装python相关包及其依赖，而且更容易安装
-   利于维护项目的依赖环境

### 使用

-   进入ANCONDA环境

    ```shell
    # 进入默认base环境
    activate  
    # 进入指定环境/切换环境	环境名： env_name
    activate env_name
    ```

-   创建环境

    ```shell
    # 环境名：env_name  解释器：python3 （python3最新版本，更精确可以写：python=3.5）
    conda create -n env_name python=3
    ```

-   切换环境

    ```shell
    # 切换环境 Windows，环境名： env_name
    activate env_name
    # Linux、MacOS下
    source activate env_name
    ```

-   查看所有环境

    ```shell
    # 查看所有环境列表
    conda env list
    ```

-   安装packages

    ```shell
    # 如需要安装包：requests
    conda install requests
    # 或者pip
    pip install requests
    ```

-   卸载packages

    ```shell
    # 如卸载包：requests
    conda remove requests
    # 或者
    pip uninstall requests
    # 删除 env_name(环境名) 下所有packages
    conda remove -n env_name --all
    ```

-   更新packages

    ```shell
    # 更新package  如：requests
    conda update requests
    ```

-   查看安装所有packages

    ```shell
    conda list
    ```

-   导出/导入环境下的packages信息

    ```shell
    # 导出packages信息到文件 environment.yaml
    conda env export > environment.yaml
    # 导入packages信息，并创建环境
    conda env creat -f environment.yaml
    ```

    