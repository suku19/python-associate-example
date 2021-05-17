def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in I(2):
    print(x, end='')


def o(p):
    def q():
        return '*' * p

    return q


r = o(1)
s = o(2)
print(r() + s())
