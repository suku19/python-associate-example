# lists in detail

# List is a collection which is ordered and changeable. Allows duplicate members.
list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#############################################################################################################################
# indexing
# Negative indices are legal
print(list[-1])  # equivalent to last element of the list

# slicing
# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
'''A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.'''
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[1:4])  # Print 2,3,4

# Advanced Python Slicing (Lists, Tuples and Arrays) Increments
'''
There is also an optional second clause that we can add that allows us to set how the list's index will increment between the indexes that we've set.
'''
a[1:4:2]  # Last clone define the slicing increment.

# Python slicing in reverse
a[::-1]  # -1 means to increment the index every time by -1, meaning it will traverse the list by going backwards.

# Using slice assignment with step sets a limitation on the list we provide for assignment. The provided list should exactly match the number of elements to replace. If the length does not match, Python throws the exception:

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# nums[::2] = [1, 1, 1]

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: attempt to assign sequence of size 3 to extended slice of size 5
# </module></stdin>

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Using Python Slice Objects:


a = [1, 2, 3, 4, 5]
sliceObj = slice(1, 3)
a[sliceObj]

# [2, 3]

##################################################################
# basic methods (append(), insert(), index())
list.append('ABC')  # Add an item to the end of the list. Equivalent to a[len(a):] = ['ABC']

list.extend(
    'iterable')  # Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable

list.insert(0,
            'ABC')  # Insert an item at a given position. Insert end of the list is equivalent to a.insert(len(a),'ABC')

list.remove('ABC')  # Remove the first item from the list whose value is equal to 'ABC'.

# list.pop([i]) # Remove the item at given position from the list and return it.
# If no index is given then it will remove last item from the list and return it.

list.clear()  # Remove all the element from the list

''' list.index(x[, start[, end]]) Return zero-based index in the list of the first item whose value is equal to x.
'''
# Raises a ValueError if there is no such item

list.count('ABC')  # Return the number of times x appears in the list.

list.reverse()  # Reverse the elements of the list in place.

list.copy()  # Return a shallow copy of the list. Equivalent to a[:]

##################################################################
# functions (len(), sorted(), etc.)

list.sort(key=None,
          reverse=False)  # Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# Bubble sort in python

unli = [8, 10, 6, 2, 4]  # list to sort
for x in range(1, 5):
    for i in range(len(unli) - 1):
        # compare adjacent elements
        if unli[i] > unli[i + 1]:
            # if we end up here it means that swap is required
            unli[i], unli[i + 1] = unli[i + 1], unli[i]
print("Sorted list is : ", unli)

newList = [11, 4, 20, 8, 10]
newList.sort(reverse=True)
print("Sorted List: ", newList)

# del instruction

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# iterating lists with the for loop,

for i in a:
    print(i)
# //////////////////////////////////////////////////
# initializing
# in and not in operators
3 not in [2, 3, 4]
3 not in [4, 5, 6]
# //////////////////////////////////////////////////
# list comprehension

# 1: List of square

squares = []

for x in range(10):
    squares.append(x ** 2)
print(squares)

# squares = list(map(lambda x: x**2, range(10)))
squares = [x ** 2 for x in range(10)]
print(squares)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if
       x != y])  # combines the elements of two lists if they are not equal:

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x * 2 for x in vec])
# filter the list to exclude negative numbers
print([x * 2 for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(10)])
# the tuple must be parenthesized, otherwise an error is raised
# print([x, x**2 for x in range(6)])


# copying and cloning

# Multiplication

[i * n for i in range(1, 4) for n in range(1, 11)]
