'''Inheritance'''

import ClassObj


class DerivedClassName(ClassObj.Bag):
    print('Inherited class')


x = DerivedClassName()

x.addtwice(22)
print(x.data)

'''
Multiple Inheritance:
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    <statement-N>

For most purposes, in the simplest cases, you can think of the search for attributes 
inherited from a parent class as depth-first, left-to-right, not searching twice in the 
same class where there is an overlap in the hierarchy. Thus, if an attribute is not found 
in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes 
of Base1, and if it was not found there, it was searched for in Base2, and so on.
'''

# Class hierarchy: https://www.python.org/download/releases/2.3/mro/


'''
Private Variables::
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.

Any identifier of the form __spam (at least two leading underscores, at most one trailing 
underscore) is textually replaced with _classname__spam, where classname is the current 
class name with leading underscore(s) stripped. This mangling is done without regard to 
the syntactic position of the identifier, as long as it occurs within the definition of a 
class.
'''


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


'''

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.
__class__ is int or some class derived from int.
    
    >>> isinstance(x,object)
    True
    >>> isinstance(x,Mapping)
    True
    >>> isinstance(x,MappingSubclass)
    True

Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a
subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
    
    >>> issubclass(MappingSubclass,Mapping)
    True
'''

'''
Bundling together a few named data items. An empty class definition will do nicely:
'''


class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


'''
Class dictionary stores functions, which become methods when they are accessed by attribute 
syntax (dot notation). With the help of descriptor protocol, every function has 
a __get__ method, which bounds function to an object.

Manual function bounding:

>>> class Test:
...     def square(self, x):
...         return x ** 2
>>> t = Test()
>>> def square(self, x):
...     return x ** 2
...
>>> print(square)
<function square at 0x109228730>
>>> bound_square = square.__get__(t,Test)
>>> print(bound_square)
<bound method square of <__main__.Test object at 0x10cdfdcf8>>
>>> print(bound_square(10))
100
>>> bound_square.__self__
<__main__.Test object at 0x10cdfdcf8>

'''


'''
Inheritance and attribute lookup order:

Method Resolution Order:

If an object defines both __get__() and __set__(), it is considered a data descriptor. 
Descriptors that only define __get__() are called non-data descriptors (they are typically 
used for methods but other uses are possible).
'''
class A:
    pass


class B:
    pass


class C(A, B):
    pass

C.mro()

# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]