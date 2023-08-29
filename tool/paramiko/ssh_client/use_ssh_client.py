import paramiko

client = paramiko.SSHClient()

# 自动添加策略, 保存服务器的主机名和密钥信息; 如果不添加, 那么不再本地 know_hosts 文件中的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接 SSH 服务端,，该过程会创建一个 session, 它是 client 和 server 保持连接的对象
client.connect(hostname='192.168.64.2', port=2222, username='root', password='qwe123')

# 执行远程命令, 该方法会打开一个 paramiko.Channel 对象(类 socket, 一种安全的 SSH 传输通道)
# 会返回三个值, 分别是 stdin(标准输入)、stdout(标准输出)、stderr(错误输出)
stdin, stdout, stderr = client.exec_command("ls /")

# 打印执行结果, 显然我们要通过 stdout 来查看, 我们可以调用 stdout.read 获取执行的结果
# 但是返回的是字节, 所以需要先获取对应的编码, 然后再进行 decode
print(stdout.read().decode("utf-8"))