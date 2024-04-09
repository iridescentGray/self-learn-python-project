import os

print(os.get_exec_path({}))
print(os.get_exec_path())


# execl、execle、execv、execve 不会利用 PATH 来定位可执行文件，需要指定完整的路径
# execlp、execlpe、execvp、execvpe 会利用PATH 来定位

# 自动忽略第一个参数foo,从第二个bar开始
os.execv("/bin/echo", ["foo", "bar"])
