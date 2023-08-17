try:
    open("xxx")
except OSError as e:
    print(e.errno)  # 2
    print(e.strerror)


import os

print(os.strerror(2))  # No such file or directory
print(os.strerror(100))  # 如果是不存在的错误码，那么会返Protocol error

# 将每一个错误码都赋值给了一个变量
import errno
print(os.strerror(errno.EHOSTUNREACH)) 
