"""
Inheritance is not the only way of constructing adaptable classes. You can achieve the same goals (not always, but very
often) by using a technique named composition.

Composition is the process of composing an object using other different objects. The objects used in the composition
deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a
more complicated structure.

It can be said that:

inheritance extends a class’s capabilities by adding new components and modifying existing ones; in other words, the
complete recipe is contained inside the class itself and all its ancestors; the object takes all the class’s belongings
and makes use of them;
composition projects a class as a container able to store and use other objects (derived from other classes) where each
of the objects implements a part of a desired class’s behavior.
"""

'''
This is how it could look →

There are two classes named Tracks and Wheels – they know how to control the vehicle’s direction. There is also a class
named Vehicle which can use any of the available controllers (the two already defined, or any other defined in the 
future) – the controller itself is passed to the class during initialization. In this way, the vehicle’s ability to 
turn is composed using an external object, not implemented inside the Vehicle’s class.

In other words, we have a universal vehicle and can install either tracks or wheels onto it.

The code produces the following output:

wheels:  True True

wheels:  True False

tracks:  False True

tracks:  False False
'''

import time


class Tracks:
    def changedirection(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def changedirection(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
