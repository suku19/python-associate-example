"""
The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the
for and in statements.

An object conforming to the iterator protocol is called an iterator.



An iterator must provide two methods:

__iter__() which should return the object itself and which is invoked once (it’s needed for Python to successfully start the iteration)

__next__() which is intended to return the next value (first, second, and so on) of the desired series – it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.


Does it look strange?

Not at all.

Look at the example →



We’ve built a class able to iterate through the first n values (where n is a constructor parameter) of the Fibonacci numbers.

Let us remind you – the Fibonacci numbers (Fibi) are defined as follows:





          Fib1 = 1
          Fib2 = 1
          Fibi = Fibi-1 + Fibi-2
"""


class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        return self.__iter;


object = Class(10)

for i in object:
    print(i)

'''
Look:

the iterator object is instantiated first;
next, Python invokes the __iter__ method to get access to the actual iterator;
the __next__ method is invoked 11 times – the first ten times produce useful values, while the 11th terminates the iteration.
'''
