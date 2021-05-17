'''
omparing strings against numbers is generally a bad idea.

The only comparisons you can perform with impunity are these symbolized by the == and != operators. The former always gives False, while the latter always produces True.

Using any of the remaining comparison operators will raise a TypeError exception.

Let’s check it →

'''

print("'10' == 10 : ", "10" == 10)
print("'10' != 10 : ", '10' != 10)

"""Sorting strings, and not only strings"""


Greek = ['omega', 'alpha', 'pi', 'gamma']

'''Method 1: returns a new list, filled with the sorted argument’s elements. '''
Greek2 = sorted(Greek)  #

print("without sort: ", Greek)
print("After sort: ", Greek2)

'''Method 2: affects the list itself – no new list is created.'''
Greek.sort()
print("Greek.sort() : ", Greek)
