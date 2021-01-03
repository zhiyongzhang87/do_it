import timeit

def TestFunction1(a, b, c, d):
    x = "%d-%d-%d-%d" % (a, b, c, d)

def TestFunction2(a, b, c, d):
    x = f"{a}-{b}-{c}-{d}"

def TestFunction2(a, b, c, d):
    x = f"{a}-{b}-{c}-{d}"

def TestFunction3(a, b, c, d):
    x = "{}-{}-{}-{}".format(a, b, c, d)

a = 55555555555
b = 55566666666
c = 55577777777
d = 55588777777

print("%d-%d-%d-%d" % (a, b, c, d))
print(f"{a}-{b}-{c}-{d}")
print("{}-{}-{}-{}".format(a, b, c, d))

print(timeit.timeit(lambda: TestFunction1(a, b, c, d), number=10000000))
print(timeit.timeit(lambda: TestFunction2(a, b, c, d), number=10000000))
print(timeit.timeit(lambda: TestFunction3(a, b, c, d), number=10000000))