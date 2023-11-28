"""

编译Cython的第二种方法(推荐)

执行命令 
python compile_method_2.py build_ext --inplace
即可完成上述两步

执行命令后,在MacOS 中,我们能看到输出的文件: fib.cpython-311-darwin.so

"""

import os
from distutils.core import setup, Extension
from Cython.Build import cythonize

cython_file = os.path.join(os.path.abspath("."), "fib.pyx")
# #language_level=3 表示只需要兼容 python3 (默认是 2 和 3 )
# setup(ext_modules=cythonize(cython_file, language_level=3))
ext = Extension(name="fib", sources=[cython_file])
setup(ext_modules=cythonize(ext, language_level=3))
