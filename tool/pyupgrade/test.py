print("foo")

a = 1
b = 2
print("%r %2f" % (a, b))


print("foo".encode())


class C(object):
    def f(self):
        super(C, self)


def f(y: list):
    for x in y:
        yield x
