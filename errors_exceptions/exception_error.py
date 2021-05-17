# Syntax Errors
# while True print('Hello world')

# Exceptions: Errors detected during execution are called exceptions.

# 10*(1/0) # ZeroDivisionError: division by zero

# 4 + span * 3  # NameError: name 'span' is not defined

# '2' + 2 # TypeError: can only concatenate str (not "int") to str


# Handling Exceptions:

while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    except (KeyboardInterrupt, BufferError, StopIteration):
        print("Aborted")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

"""Argument of an Exception"""

'''
An exception can have an argument, which is a value that gives additional information 
about the problem. The contents of the argument vary by exception. You capture an exception's 
argument by supplying a variable in the except clause as follows −
'''

# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError, Argument:
#         print("The argument does not contain numbers", Argument)


# Call above function here.
# temp_convert("xyz");

# str = input()

'''
If you want to handle two or more exceptions in the same way, you can use the following syntax →
try:
    :
except(exc1, exc2):
    :
'''


def badfun(n):
    raise ZeroDivisionError


try:
    badfun(0)
except (ZeroDivisionError, ArithmeticError):
    print('What did you do? Arithmetic problem')
print('THE END')

""":::::::Assert:::::::"""

'''
Assert is a keyword.

How does it work?

It evaluates the expression;
if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different 
than None, it won’t do anything else;
otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)
'''
print()
print("Assert ::: ")
import math

x = float(input("Enter number not less than 0.0.."))
assert x >= 0.0
x = math.sqrt(x)
print(x)

"""BaseException ← Exception ← LookupError ← IndexError"""
print()
print("BaseException ← Exception ← LookupError ← IndexError")

# the code shows an extravagant way of leaving the loop
list = [1, 2, 3, 4, 5]
ix = 0
doit = True
while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False
print('Done')

"""BaseException ← KeyboardInterrupt"""

# this code cannot be terminated by pressing Ctrl-C

print()
print("BaseException ← KeyboardInterrupt")
'''from time import sleep

seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that..")'''

"""BaseException ← Exception ← MemoryError"""

# this code causes the MemoryError exception
# warning: executing this code may be crucial for your OS
# don't run it in production environments!
print()
print("BaseException ← Exception ← MemoryError")
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

"""BaseException ← Exception ← ArithmeticError ← OverflowError"""
print()
print("BaseException ← Exception ← ArithmeticError ← OverflowError")
# the code prints subsequent values of exp(k), k = 1,2,4,8,16,…
from math import exp

ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('Number is too big.')

"""BaseException ← Exception ← StandardError ← ImportError"""

print()
print("BaseException ← Exception ← StandardError ← ImportError")
# one of this imports will fail - which one?
try:
    import math
    import time
    import abracadabra
except:
    print('One of your imports has failed. ')

"""BaseException ← Exception ← LookupError ← KeyError"""
print()
print("BaseException ← Exception ← LookupError ← KeyError")

# how to abuse the dictionary and how to deal with it
dict = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)
