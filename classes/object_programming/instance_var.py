# class OurClass:
#     def __init__(self, val=1):
#         self.first_var = val
#
#     def setSecondVar(self, val):
#         self.second_var = val
#
#
# cls = OurClass()
# print("Type of cls is: ", type(cls))
#
# object1 = OurClass()
# object2 = OurClass(2)
# object2.setSecondVar(3)
# object3 = OurClass(4)
# object3.__Third = 5
#
# print("object1 property: ", object1.__dict__)
# print("object2 property: ", object2.__dict__)
# print("object3 property: ", object3.__dict__)

class Class:
    def __init__(self, val=1):
        self.__First = val

    def setSecond(self, val=2):
        self.__Second = val


object1 = Class()
object2 = Class(2)
object2.setSecond(3)
object3 = Class(4)
object3.__Third = 5

print(object1.__dict__)
print(object2.__dict__)
print(object3.__dict__)
