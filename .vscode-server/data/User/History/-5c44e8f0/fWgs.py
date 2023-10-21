def topten():

    yield 1

n = topten()

print(n.__next__())
