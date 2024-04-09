import os
import stat

print(os.access("./1.png", os.F_OK))
print(os.access("./1.png", os.R_OK))
print(os.access("./1.png", os.W_OK))
print(os.access("1.png", os.X_OK))

print(os.access("python_basics/os/1.png", os.F_OK))

# chmod
print(os.chmod("python_basics/os/1.png", 0o777))

os.chmod("python_basics/os/1.png", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
