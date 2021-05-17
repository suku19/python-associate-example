""" Generator Expressions.."""

'''
A generator expression yields a new generator object. Its syntax is the same as 
for comprehensions, except that it is enclosed in parentheses instead of brackets 
or curly braces.
'''

'''
Experience with list comprehensions has shown their widespread utility throughout 
Python. However, many of the use cases do not need to have a full list created in 
memory. Instead, they only need to iterate over the elements one at a time.
'''

'''
For instance, the following summation code will build a full list of squares in 
memory, iterate over those values, and, when the reference is no longer needed, 
delete the list:
'''

# List comprehensions
x = sum([x * x for x in range(5)])
print('Sum square element using List comprehensions: ', x)

# Memory is conserved by using generator expression instead:
gen = (x * x for x in range(5))
y = sum(gen)
print('Sum square element using generator "{0}" Expression {1}'.format(gen, x))

"""Generator Functions with Yield Expressions"""

'''
The yield expression is used when defining a generator function or an asynchronous 
generator function and thus can only be used in the body of a function definition. 
Using a yield expression in a function’s body causes that function to be a generator,
and using it in an async def function’s body causes that coroutine function to be 
an asynchronous generator. For example:
'''


def gen():  # defines a generator function
    yield 123


async def agen():  # defines an asynchronous generator function
    yield 123


"""Generator-iterator methods"""

'''
Note that calling any of the generator methods below when the generator is already 
executing raises a ValueError exception.
'''

'''
generator.__next__() : Starts the execution of a generator function or resumes it at 
the last executed yield expression.

'''


def gen():  # defines a generator function
    yield 123
    yield 222
    yield 333


a = gen()
print(a.__next__())
print(a.__next__())

'''
generator.send(value): Resumes the execution and “sends” a value into the generator 
function. The value argument becomes the result of the current yield expression.
'''

'''
generator.throw(type[, value[, traceback]]): Raises an exception of type type at the 
point where the generator was paused, and returns the next value yielded by the 
generator function.
'''

'''
generator.close()
Raises a GeneratorExit at the point where the generator function was paused. 
If the generator function then exits gracefully, is already closed, or raises 
GeneratorExit (by not catching the exception), close returns to its caller.
'''


# Example of generator function

def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


# Call the above function

generator = echo(1)
print("next(generator) : ", next(generator))  # Execution starts when 'next()' is called for the first time.
print("next(generator) : ", next(generator))  # Default value will be print

print("generator.send(2) : ", generator.send(2))  # send value to generator
print("generator.__next__() :", generator.__next__())

generator.throw(TypeError, "Spam")

generator.close()  # will call the finally method as it exit from generator

print()

print("how to build a generator:: ")


def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print("Generator value: ", v)

print()

print("Generator to produce the first n powers of 2:: ")


def PowersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2


for v in PowersOf2(8):
    print("Square of integer: ", v)

print()
print("::Generators may also be used within list comprehensions::")


def PowersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2


t = [x for x in PowersOf2(5)]
print("List comprehensions: ", t)

print("::The list() function can transform a series of subsequent generator invocations into a real list::")
t = list(PowersOf2(5))
print("List comprehensions: ", t)

print()
print(":: Moreover, the context created by the in operator allows you to use a generator, too.::")
for i in range(10):
    if i in PowersOf2(4):
        print(i)

print()
print(":: Fibonacci number generator::")


def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            p, pp = pp, n
            yield n


fibs = list(Fib(10))
print("Fibonacci series: ", fibs)

print()
print("::list comprehensions::")

list = [1 if x % 2 == 0 else 0 for x in range(10)]

for v in list:
    print(v, end=" ")
print()

print()
print("::Parentheses make a generator::")
genr = (1 if x % 2 == 0 else 0 for x in range(10))
for v in genr:
    print(v, end=" ")
print()

# as it is generator, len(genr) will raise an exception,
# len(genr)  # TypeError: object of type 'generator' has no len()
