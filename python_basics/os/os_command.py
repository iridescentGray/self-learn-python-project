import os
import echo

# 返回值为 0 表示成功
# 1 表示失败，并且控制台显示的错误信息也会自动打印出来，只不过由于编码问题会显示乱码
print(os.system(f"python {echo.__file__}"))