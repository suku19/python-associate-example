"""
 the Var class variable and fun() method from Level1 class override the entities of the same names derived from the Level0 class.
"""


class Level0:
    Var = 100

    def fun(self):
        return 101


class Level1(Level0):
    Var = 200

    def fun(self):
        return 201


class Level2(Level1):
    pass


object = Level2()
print(object.Var, object.fun())

print()
print()

'''
We can say that Python looks for object components in the following order:
1) inside the object itself;
2) in its superclasses, from bottom to top;
3) if there is more than one class on a particular inheritance path, Python scans them from left to right.
'''
class Left:
    Var = 'L'
    VarL = 'LL'

    def fun(self):
        return 'left'


class Right:
    Var = 'R'
    VarR = 'RR'

    def fun(self):
        return 'right'


class Sub(Left, Right):
    pass


object = Sub()

print(object.Var, object.VarL, object.VarR, object.fun())
