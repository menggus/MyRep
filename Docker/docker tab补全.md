## bash completion scripts

- 在bash能够通过tab键补全docker-machine的自命令和参数

  ```shell
  # 编辑脚本
  base=https://raw.githubusercontent.com/docker/machine/v0.14.0
  for i in docker-machine-prompt.bash docker-machine-wrapper.bash docker-machine.bash
  do
    sudo wget "$base/contrib/completion/bash/${i}" -P /etc/bash_completion.d
  done
  
  # 使脚本生效
  source /etc/bash_completion.d/docker-machine-prompt.bash
  
  #添加到 $HOME/.bashrc(永久生效)
  PS1='[\u@\h \W$(__docker_machine_ps1)]\$ '
  
  ```

  