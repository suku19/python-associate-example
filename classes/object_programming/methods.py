"""
a method is a function embedded inside a class.

There is one fundamental requirement – a method is obliged to have at least one parameter (there are no such thing as
parameterless method – a method may be invoked without an argument, but not declared without parameters).
"""


class Classy:
    variable = 1

    def __method1(self):  # hidden method, can't be access from outside
        print("Inside the method1..")

    def method2(self, var):
        print("Inside the method2..", var)

    # The self parameter is used to obtain access to the object’s instance and class variables.
    def method3(self):
        print("Inside the method3..", self.variable, self.var)
        self.__method1()  # self can be used to invoke other method


obj = Classy()
# obj.__method1()  # hidden method, can't be access from outside
obj.method2(12)  # Invoke method

obj.var = 44  # add a new property to the object
obj.method3()
print("obj.__dict__ : ", obj.__dict__)
print("Classy.__dict__ : ", Classy.__dict__)
print()

print("__name__::")
print("Classy.__name__ : ", Classy.__name__)
print("obj.__name__ : ", type(obj).__name__)
print()

print("__module__:: any module named __main__ is actually not a module, but the file currently being run")
print("Classy.__module__: ", Classy.__module__)
print("obj.__module__: ", obj.__module__)
print()

"""__init__ constructor::::::::::::::"""

'''
If you name a method __init__, it won’t be a regular method – it will be a constructor.

If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.
'''

print("__init__ constructor::")


class Classy:
    def __init__(self, value):
        self.var = value


obj1 = Classy("object")
print("obj1.var: ", obj1.var)
print()

'''
Note that the constructor:

1) cannot return a value,as it is designed to return a newly created object and nothing else;

2) cannot be invoked directly either from the object or from inside the class (you can invoke a constructor from any of
   the object’s superclasses, but we’ll discuss this issue later).
'''


"""
__bases__::: is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

Note: a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.
"""


class Super1:
    pass


class Super2:
    pass


class Sub(Super1, Super2):
    pass


def printbases(cls):
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printbases(Super1)
printbases(Super2)
printbases(Sub)
