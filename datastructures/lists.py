# Using Lists as Stacks

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# List Comprehensions

squares = []
for x in range(10):
    squares.append(x ** 2)  # create a list of squares
print(squares)

# Note that this creates (or overwrites) a variable named x that still exists after the loop completes.
# We can calculate the list of squares without any side effects using:

squares = []
squares = [x ** 2 for x in range(10)]
print(squares)

squares = []
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
print([(x, x ** 2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# The del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# Effective way to swap value in python

var1 = 1
var2 = 2

var1, var2 = var2, var1
print("Swap value value of var1 is", var1, "and var2 is", var2)

# swap a list value

l = [10, 1, 8, 3, 5]
print("Before swap: ", l)
l[0], l[4] = l[4], l[0]
l[1], l[3] = l[3], l[1]
print("After swap: ", l)
