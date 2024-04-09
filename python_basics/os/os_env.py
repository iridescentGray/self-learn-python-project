import os

print(os.supports_bytes_environ)

if os.supports_bytes_environ:
    print(f"----------------------------------os.environb: \n {os.environb}")


print(f"----------------------------------os.environ: \n {os.environ}")
print(f"----------------------------------type(os.environ): \n {type(os.environ)}")
print(f"USER：  {os.environ['USER']}")
print(f"PATH：  {os.environ['PATH']}")


print(os.getenv("USER"))
print(os.getenv("USER1", "不存在"))  # 不存在
