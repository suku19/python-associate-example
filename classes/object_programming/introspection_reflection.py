"""
introspection, which is the ability of a program to examine the type or properties of an object at runtime;

reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or
functions of an object at runtime.
"""


class Class:
    pass


obj = Class()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

print("__dict__ keys()::: ", obj.__dict__.keys())


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

'''
Both reflection and introspection enable a programmer to do anything with every object, no matter where it comes from.

Analyze the following code →

 

The function named incIntsI() gets an object of any class, scans its contents in order to find all integer attributes with names starting with i, and increments them by one.

Impossible? Not at all!

 

This is how it works:

line 01: define a very simple class . . .

lines 03 through 10: . . . and fill it with some attributes;

line 12: this is the function!

line 13: scan the __dict__ attribute, looking for all attribute names;

line 14: if a name starts with i . . .

line 15: . . . use the getattr() function to get its current value; note: getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute’s value;

line 16: check if the value is of type integer, and use the function isinstance() for this purpose (we’ll discuss this later);

line 17: if the check goes well, increment the property’s value by making use of the setattr() function; the function takes three arguments: an object, the property name (as a string), and the property’s new value.
 

That’s all!

 

The code outputs:

 

{'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
{'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}
'''