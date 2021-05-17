class MyClass:
    """A simple example of class"""
    i = 12345

    def f(self):
        return "Hello World"

    def __init__(self, realpart, imagpart):  # Multiple init method not supported by python
        self.r = realpart
        self.i = imagpart


'''Class and Instance Variables'''

'''instance variables are for data unique to each instance and class variables are for 
attributes and methods shared by all instances of the class
'''

class Dog:
    kind = 'canine'             # class variable shared by all instances

    def __init__(self, name):
        self.name = name        # instance variable unique to each instance


'''
shared data can have possibly surprising effects with involving mutable objects such as 
lists and dictionaries. For example, the tricks list in the following code should not be 
used as a class variable because just a single list would be shared by all Dog instances:
'''

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('aaa')
e = Dog('bbb')
d.add_trick('added by obj d')
e.add_trick('added by obj e')
print(d.tricks)


# Correct design of the class should use an instance variable instead:

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('aaa')
e = Dog('bbb')
d.add_trick('added by obj d')
e.add_trick('added by obj e')
print(d.tricks)


'''
Any function object that is a class attribute defines a method for instances of that 
class. It is not necessary that the function definition is textually enclosed in the class 
definition: assigning a function object to a local variable in the class is also ok. 
For example:
'''
# Function defined outside the class


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


'''
Methods may call other methods by using method attributes of the self argument:
'''

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)