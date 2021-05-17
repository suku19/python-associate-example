t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable,
# and their elements are usually homogeneous and are accessed by iterating over the list.

t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v