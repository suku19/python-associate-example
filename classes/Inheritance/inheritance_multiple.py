"""
Multiple inheritance occurs when a class has more than one superclass.

Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses after the
new class name – just like here →

"""


class SuperA:
    VarA = 10

    def funa(self):
        return 11


class SuperB:
    VarB = 20

    def funb(self):
        return 21


class Sub(SuperA, SuperB):
    pass


object = Sub()

print(object.VarA, object.funa())
print(object.VarB, object.funb())
