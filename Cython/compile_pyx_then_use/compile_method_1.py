"""

编译Cython(不够通用)

我们说构建扩展模块的过程分为两步:
1. 将 Cython 代码翻译成 C 代码(由 cython 编译器完成,即cythonize);
   a. cythonize 负责将 Cython 代码转成 C 代码, 这里我们可以传入单个文件, 也可以是多个文件组成的列表
   b. 或者一个glob模式, 会匹配满足模式的所有 Cython 文件
2. 根据 C 代码生成扩展模块(由 distutils完成 ,即distutils.core下的setup)


执行命令:
python compile_method_1.py build_ext --inplace
即可完成上述两步

执行命令后,在MacOS 中,我们能看到输出的文件: fib.cpython-311-darwin.so

"""

import os
from distutils.core import setup

from Cython.Build import cythonize

cython_file = os.path.join(os.path.abspath("."), "fib.pyx")
# #language_level=3 表示只需要兼容 python3 (默认是 2 和 3 )
setup(ext_modules=cythonize(cython_file, language_level=3))
