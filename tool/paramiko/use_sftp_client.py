import paramiko

# 创建一个 Transport 对象, 使用时会同步创建一个 paramiko.Channel 对象
# 参数传递一个由 IP 和 PORT 组成的元组即可
transport = paramiko.Transport(("192.168.64.2", 2222))

# 连接 ssh, 通过 username 和 password
transport.connect(username="root", password="qwe123")

# 获取 SFTPClient 实例, 它便相当于 Linux 下的 sftp, 我们通过它可以进行文件的一些操作
sftp = paramiko.SFTPClient.from_transport(transport)

"""

sftp 支持的方法

put(self, localpath, remotepath, callback=None, confirm=True)：将本地文件上传到服务器, callback 表示回调函数, 上传成功后调用; confirm 表示是否调用 stat 方法检查文件状态, 返回 ls -l 的结果
get(self, remotepath, localpath, callback=None)：将文件从服务器下载到本地
mkdir(self, path, mode=o777)：在服务器上创建目录, mode 表示权限, 默认为 511(o777 是一个变量, 等于 511)
rmdir(self, path)：删除服务器上的目录
remove(self, path)：删除服务器上的文件
rename(self, oldpath, newpath)：对服务器上目录进行重命名
stat(self, path)：查看文件或目录的状态
listdir(self, path='.')：列出服务器目录下的文件
getcwd(self)：查看工作区, 也就是当前所在路径
chmod(self, path, mode)：改变权限
chown(self, path, uid, gid): 改变用户和组
chdir(self, path)：改变工作区

"""
print(sftp.chdir("/usr/local/bin"))
print(f"sftp.getcwd():  {sftp.getcwd()}")

print(f'sftp.stat:   {sftp.stat("/root/.ssh/authorized_keys")}')

sftp.chmod("/root/.ssh/authorized_keys", 0o777)

print(f'sftp.stat:   {sftp.stat("/root/.ssh/authorized_keys")}')

print("dir" in sftp.listdir("/root"))  # False
sftp.mkdir("/root/dir", mode=0o777)
print("dir" in sftp.listdir("/root"))  # True

sftp.rmdir("/root/dir")
print("dir" in sftp.listdir("/root"))

sftp.put("README.md", "/root/README.md")

sftp.close()
transport.close()
