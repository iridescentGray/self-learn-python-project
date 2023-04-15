import subprocess as sp

if __name__ == '__main__':
    cmd = "ls"
    # 执行命令
    process = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    # 等待命令执行完成
    process.wait()

    # 获取命令的输出和错误信息
    output = process.stdout.read()
    error = process.stderr.read()

    # 将输出和错误信息解码为字符串
    output = output.decode(encoding="gbk")
    error = error.decode(encoding="gbk")

    # 返回命令的输出和错误信息
    result = {"output": output, "error": error}
    print(result)
