import paramiko

client = paramiko.SSHClient()

"""
set_missing_host_key_policy

AutoAddPolicy: 自动添加主机名以及主机秘钥到本地 HostKeys 对象, 不依赖 load_system_host_key 的配置, 即新建立 ssh 连接时不需要再输入 yes 或 no 进行确认
WarningPolicy: 用于记录一个未知的主机秘钥的 Python 警告、并且接收; 所以它的功能和 AutoAddPolicy 是类似的, 只不过会提示这是新连接
RejectPolicy: 自动拒绝未知的主机名和秘钥, 依赖 load_system_host_key 的配置, 该选项为默认选项

"""
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

"""
connect:实现远程服务器的连接与认证

hostname:连接的目的主机, 这个参数是必须的
port=SSH_PORT:指定的端口, 默认是 22
username=None:登陆的用户
password=None:用户密码
pkey=None:通过私钥进行身份验证
key_filename=None:一个文件名或文件列表, 指定私钥文件
timeout=None:可选的 tcp 连接超时时间
allow_agent=True:是否允许连接到 ssh 代理, 默认为 True
look_for_keys=True:是否在 ~/.ssh 中搜索私钥文件, 默认为 True, 表示允许
compress=False:是否打开压缩

"""
client.connect(hostname="192.168.64.2", port=2222, username="root", password="qwe123")

# 执行远程命令, 该方法会打开一个 paramiko.Channel 对象(类 socket, 一种安全的 SSH 传输通道)
# 会返回三个值, 分别是 stdin(标准输入)、stdout(标准输出)、stderr(错误输出)
stdin, stdout, stderr = client.exec_command("ls /root")

# 也可以通过 open_sftp 方法来创建 sftp 客户端
# sftp = client.open_sftp()

# 打印执行结果
print(stdout.read().decode("utf-8"))
