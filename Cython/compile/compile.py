from distutils.core import setup
from Cython.Build import cythonize

# 我们说构建扩展模块的过程分为两步: 1. 将 Cython 代码翻译成 C 代码; 2. 根据 C 代码生成扩展模块
# 而第一步要由 cython 编译器完成, 通过 cythonize; 第二步要由 distutils 完成, 通过 distutils.core 下的 setup
# #language_level=3 表示只需要兼容 python3 即可, 而默认是 2 和 3 都兼容
# 强烈建议加上这个参数, 因为目前为止我们只需要考虑 python3 即可
setup(ext_modules=cythonize("compile/fib.pyx", language_level=3))

# cythonize 负责将 Cython 代码转成 C 代码, 这里我们可以传入单个文件, 也可以是多个文件组成的列表
# 或者一个glob模式, 会匹配满足模式的所有 Cython 文件; 然后 setup 根据 C 代码生成扩展模块python setup.py build_ext --inplace

