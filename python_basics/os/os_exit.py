import os
import sys

try:
    # 退出 Python 程序的首选方法。使用 sys.exit(n) 会引发一个 SystemExit 异常,如果没有捕获这个异常，程序会直接退出。
    sys.exit(100)
except SystemExit:
    print("程序想要退出，被捕获了")

print(123)


os._exit(1000)
print(456)
