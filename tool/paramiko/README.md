# paramiko

Native Python SSHv2 protocol library.

## use

### Used by pyenv virtualenv paramiko

    pyenv virtualenv 3.10.12 paramiko
    pyenv activate paramiko
    python -m pip install --upgrade pip
    cd tool/paramiko
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    paramiko: https://github.com/paramiko/paramiko

#### doc

    paramiko 包含两大核心组件：SSHClient 和 SFTPClient

    SSHClient 的作用类似于 Linux 下的 ssh 命令，是对 SSH 会话的封装，通常用于执行远程命令。
    SFTPClient 的作用类似于 Linux 下的 sftp 命令，是对 SFTP 客户端的封装，用于实现远程文件的操作。比如：文件上传，下载、修改文件权限等操作。

## uninstall

    pyenv virtualenv-delete paramiko
