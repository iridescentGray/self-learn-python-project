import time

from pyinstrument import Profiler

profiler = Profiler()
profiler.start()


def a():
    b()
    c()


def b():
    d()


def c():
    d()


def d():
    e()


def e():
    time.sleep(1)


a()

profiler.stop()
profiler.print()
