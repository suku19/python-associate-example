"""
A class variable is a property which exists in just one copy and is stored outside any object.

Note: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.

Class variables are created differently to their instance siblings.
"""

print("Class Variable::")


class Class:
    Counter = 0

    def __init__(self, val=1):
        self.__First = val
        Class.Counter += 1


object1 = Class()
object2 = Class(2)
object3 = Class(4)

print(object1.__dict__, object1.Counter)
print(object2.__dict__, object2.Counter)
print(object3.__dict__, object3.Counter)
print()

print("Mangling a class variable’s name has the same effects as those you’re already familiar with.")


class Class:
    __Counter = 0

    def __init__(self, val=1):
        self.__First = val
        Class.__Counter += 1


object1 = Class()
object2 = Class(2)
object3 = Class(4)

print(object1.__dict__, object1._Class__Counter)
print(object2.__dict__, object2._Class__Counter)
print(object3.__dict__, object3._Class__Counter)
print()

'''
class variables aren’t shown in an object’s __dict__ (this is natural as class variables aren’t parts of an object) 
but you can always try to look into the variable of the same name, but at the class level
'''

print("Class variable exist even when no class instance (object) had been created.")


class Class:
    Var = 1

    def __init__(self, val):
        Class.Var = val
        self.Var = val


print(Class.__dict__)
object = Class(2)
print(Class.__dict__)
print(object.__dict__)
print()
