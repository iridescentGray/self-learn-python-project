import datetime
import os

t = datetime.datetime(1981, 1, 1).timestamp()
os.utime("python_basics/os/1.png", (t, t))
