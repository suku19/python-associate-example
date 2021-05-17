"""A lambda function is a function without a name (you can also call it an anonymous function). Of course,
such a statement immediately raises the question: how do you use anything that cannot be identified?

Fortunately, it’s not a problem, as you can name such a function if you really need, but, in fact, in many cases the
lambda function can exist and work while remaining fully incognito.

The declaration of the lambda function doesn’t resemble a normal function declaration in any way – see for yourself →

"""

two = lambda: 2
sqr = lambda x: x * x  # one-parameter anonymous function that returns the value of its squared argument.
pwr = lambda x, y: x ** y  # returns the value of the first one raised to the power of the second one.

for a in range(-2, 3):
    print("lambda x: x * x :: param:", a, "sqr(a): ", sqr(a), end=' ')
    print("lambda x, y: x ** y :: param: ", a, "pwr(a,two()):", pwr(a, two()))
print()

print("Increment by n Lambda function::")


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print("f(0) : ", f(0))
print("f(1) : ", f(1))
print()

print(" pure form – as anonymous parts of code intended to evaluate a result.")
'''
The printfunction() function takes two parameters:

the first, a list of arguments for which we want to print the results;
the second, a function which should be invoked as many times as the number of values that are collected 
inside the first parameter.
'''


def printfunction(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


printfunction([x for x in range(-2, 3)], poly)

#  Directly invoke print function with help of lambda
printfunction([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

print()

print("::How to use lambdas and what for?:: map(fun(), list)")

'''build the list1 with values from 0 to 4;'''
list1 = [x for x in range(5)]
print("list of 0 to 4: ", list1)

'''next, use map along with the first lambda to create a new list in which all elements have been evaluated as two 
raised to the power taken from the corresponding element from list1;'''
list2 = list(map(lambda x: 2 ** x, list1))

'''list2 is printed then;'''
print("list2: ", list2)

'''in the next step, use the map() function again to make use of the generator it returns and to directly print all 
the values it delivers; as you can see, we’ve engaged the second lambda here – it just squares each element from list2.'''
print("squares each element from list2:", end=' ')
for x in map(lambda x: x * x, list2):
    print(x, end=' ')
print()
print()

print("::How to use lambdas and what for?:: filter(function, list)")
from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print("Actual list: ", data)
print("filtered list: ", filtered)
print()

# Documentation Strings

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)


# Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
