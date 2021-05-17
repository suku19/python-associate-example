"""
As you already know, there are no obstacles to using multiple inheritance in Python. You can derive any new class from
more than one previously defined classes.

There is only one but. The fact that you can do it does not mean you have to.

Don’t forget that:

1) a single inheritance class is always simpler, safer, and easier to understand and maintain;
2) multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts
of the superclasses which will effectively influence the new class;
3) multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes  ambiguous;
4) multiple inheritance violates the single responsibility principle (more details here:
https://en.wikipedia.org/wiki/Single_responsibility_principle) as it makes a new class of two (or more) classes that
know nothing about each other;
5) we strongly suggest multiple inheritance as the last of all possible solutions – if you really need the many
different functionalities offered by different classes, composition may be a better alternative.
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B,A):
    pass


d = D()
