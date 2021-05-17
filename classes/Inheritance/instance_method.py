print("::Find the valid subclass : issubclass()::")


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cl1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cl2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cl1, cl2), end='\t')
    print()

print()

print("::Find the valid instance : isinstance()::")

vehicle = Vehicle()
landvehicle = LandVehicle()
trackedvehicle = TrackedVehicle()

for ob in [vehicle, landvehicle, trackedvehicle]:
    for cl in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(ob, cl), end='\t')
    print()

print()

print("::is operator: checks whether two variables (object1 and object2 here) refer to the same object.")
print("landvehicle is vehicle : ", landvehicle is vehicle)
print("vehicle is vehicle : ", vehicle is vehicle)


class ThisIsClass:
    def __init__(self, val):
        self.val = val


ob1 = ThisIsClass(0)
ob2 = ThisIsClass(2)
ob3 = ob1
ob3.val += 1
print("ob1 is ob2 :", ob1 is ob2)
print("ob2 is ob3 :", ob2 is ob3)
print("ob3 is ob1 :", ob3 is ob1)
print("ob1.val, ob2.val, ob3.val : ", ob1.val, ob2.val, ob3.val)

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"
print("str1 == str2, str1 is str2::", str1 == str2, str1 is str2)
print()

print("How Python finds properties and methods?")


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):  # The Sub class defines its own constructor, which invokes the one from the superclass
        Super.__init__(self,
                       name)  # We’ve explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.


class Sub1(Super):
    def __init__(self, name):
        super().__init__(name)  # super() function, accesses the superclass without needing to know its name


obj = Sub("Sukanta")
print(obj)

obj1 = Sub1('Jhon')
print(obj1)

