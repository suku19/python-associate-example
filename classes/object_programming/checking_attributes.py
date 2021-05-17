"""
Python’s attitude to object instantiation raises one important issue – in contrast to other programming languages, you may not expect that all objects of the same class have the same sets of properties.
Just like here →
The object created by the constructor can have only one of two possible attributes: a or b.
"""


class Class:
    c = 1

    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


obj = Class(1)
print(obj.a)
# print(obj.b)

'''
Python provides a function which is able to safely check if any object/class contains a specified property. The function is named hasattr, and expects two arguments to be passed to it:

1) the class or the object being checked;
2) the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)
 
The function returns True or False.
'''

if hasattr(obj, 'b'):
    print(obj.b)
else:
    print("Object property 'b' not found..")

print("hasattr(Class, 'c'): ", hasattr(Class, 'c'))
print("hasattr(obj, 'c'): ", hasattr(obj, 'c')) # it return true as class attribute is present within object as well
