import inner_package_1
from inner_package_2 import a_model
from __all__package import *
from underscores_package import *

"""总结

通过inner_package_1 和 inner_package_2 可得出:
    1.“import” and “from import” 将会执行所有'被导入包'和'被导入包的__init__.py'的所有代码
    2.按导入顺序执行所有代码
    3.先执行'被导入包的__init__.py' ,后执行 '被导入包'
    4.使用'import package' 或 'from package import model'时, package和model中的变量,并不会被导入到当前作用域

通过__all_package可得出:
    1. from x import *  只会导入__all__指定的变量,其他任何全局变量不会被导入

通过underscores_package可得出:
    1. from x import *  不会导入下划线开头的所有变量,其他的都会被导入
    2. from x import *  会导致包中的所有 model被导入

"""

print("main.py run")
print("-" * 150)

# 查看当前作用域的所有变量,验证上述描述
for k, v in globals().copy().items():
    print(f"{k}          {v}")
