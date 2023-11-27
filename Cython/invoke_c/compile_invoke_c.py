"""

编译Cython的第二种方法(推荐)

执行编译命令 
python compile_invoke_c.py build_ext --inplace


执行命令后,在MacOS 中,我们能看到输出的文件: fib.cpython-311-darwin.so
     
"""

from distutils.core import setup,Extension
from Cython.Build import cythonize

ext = Extension(name="wrapper_cfib", sources=["with_c_code.pyx", "cfib.c"])
setup(ext_modules=cythonize(ext, language_level=3))
