# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)
# list = [x * x for x in range(5)]
#
#
# def fun(L):
#     del L[L[2]]
#     return L
#
#
# print(fun(list))
#
# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
# print(x, y, z)
# ############################
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
# ##############################
#
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
#
#
# print(fun(fun(2)))
#
# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']
# for k in range(len(dct)):
#     v = dct[v]
# print(v)
#
#
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y - 1)
#
#
# print(fun(0, 3))
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)
# dd = {"1": "0", "0": "1"}
# for x in dd.values():
#     print(x, end="")
#
# ########################
# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
# for x in dct.keys():
#     print(dct[x][1], end="")
############################
def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")