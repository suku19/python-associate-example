try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")

x = "\\\\"
print(len(x))


class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)


################################
class A:
    A = 1

    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))


###############################

class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C))

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))


    class I:
        def __init__(self):
            self.s = 'abc'
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i == len(self.s):
                raise StopIteration
            v = self.s[self.i]
            self.i += 1
            return v


    for x in I():
        print(x, end='')


    def o(p):
        def q():
            return '*' * p

        return q


    r = o(1)
    s = o(2)
    print(r() + s())

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
for x in d.keys():
    # print('x: ',x)
    print(d[x][1], end="")

Val = 1
Val2 = 0
Val = Val ^ Val2
Val2 = Val ^ Val2
Val = Val ^ Val2
print(Val, Val2)

i = 10
while i > 0:
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")

print()

# for i in range(1, 4, 2):
#     print("*")

# Example 2
# for i in range(1, 4, 2):
#     print("*", end="")
#
# Example 3
for i in range(1, 4, 2):
    print("*", end="**")
#
# # Example 4
# for i in range(1, 4, 2):
#     print("*", end="**")
# print("***")
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")

x = 5
f = lambda x: 1 + 2
print(f(x))


def fun(a, b=0, c=5, d=1):
    return a ** b ** c


print(fun(b=2, a=2, c=3))

i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2
print(i)

x = 0
try:
    print(x)
    print(1 / x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x + 1)
print(x + 2)


def gen():
    lst = range(5)
    for i in lst:
        yield i * i


for i in gen():
    print(i, end="")

lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')

try:
    print("Hello")
    raise Exception
    print(1 / 0)
except Exception as e:
    print('e', e)

x = "20"
y = "30"
print(x > y)

# line 02

z, y, x = 2, 1, 0
x, z = z, y
y = y - z
print(x, y, z)

lst1 = "12,34"
lst2 = lst1.split(',')
print(len(lst1) < len(lst2))

x = 1  # line 1


def a(x):  # line 2
    return 2 * x  # line 3


x = 2 + a(x)  # line 4
print(a(x))

dict = {'a': 1, 'b': 2, 'c': 3}
for item in dict:
    print(item)
