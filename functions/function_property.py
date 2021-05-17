""" property() function """

'''
In Python, the main purpose of Property() function is to create property of a class.

Syntax: property(fget, fset, fdel, doc)

Parameters:
fget() – used to get the value of attribute
fset() – used to set the value of atrribute
fdel() – used to delete the attribute value
doc() – string that contains the documentation (docstring) for the attribute

Return: Returns a property attribute from the given getter, setter and deleter.
'''


# Python program to explain property() function

# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        print('Getting value')
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

# print("Set value to GFG: ", x.value)

del x.value
print('After delete: ', x)

print()
print()
print("Using @property decorator..")


"""Using @property decorator"""


class PropertyDecorator:
    def __init__(self, value):
        self._value = value

    # getting a value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value


# Passing the value
x = PropertyDecorator('Peter')
print("Getting a value: ", x.value)

x.value='ddd'
print("Setting a value:  ", x.value)

print("Value deleted..")
del x.value