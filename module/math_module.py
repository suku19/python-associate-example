"""To make a module usable, you must import it. All the entity in the math module is accessible."""

import math

print('Power of 3 to 3', math.pow(3, 3))
print('Value of pi: ', math.pi)

'''
In the second method, the import’s syntax precisely points out which module’s entity (or entities) are acceptable in the 
code. no other entities are imported.
'''

from math import pi

print("value of pi: ", pi)

'''
Aliasing causes the module to be identified under a different name than the original. 
This may shorten the qualified names, too.
'''

# import module as alias

# from module import entity as e

'''The phrase name as alias can be repeated – use commas to separate the multiplied phrases, like this:'''
# from module import entity1 as e1, entity2 as e2

from math import pi as PI, sin as sine

print(sine(PI / 2))

'''
dir(module) : it is able to reveal all the names provided through a particular module. There is one condition: 
the module has to have been previously imported as a whole (i.e., using the import module instruction – from module is not enough).

The function returns an alphabetically sorted list containing all entities’ names available in the module identified by a 
name passed to the function as an argument.

Note: if the module’s name has been aliased, you must use the alias, not the original name.
'''

print(dir(math))


"""Some function from math module"""

'''
trigonometry:::::::

sin(x)→ the sine of x;
cos(x)→ the cosine of x;
tan(x)→ the tangent of x.

asin(x)→ the arcsine of x;
acos(x)→ the arccosine of x;
atan(x)→ the arctangent of x.

pi→ a constant with a value that is an approximation of π;
radians(x)→ a function that converts x from degrees to radians;
degrees(x)→ acting in the other direction (from radians to degrees)

sinh(x)→ the hyperbolic sine;
cosh(x)→ the hyperbolic cosine;
tanh(x)→ the hyperbolic tangent;
asinh(x)→ the hyperbolic arcsine;
acosh(x)→ the hyperbolic arccosine;
atanh(x)→ the hyperbolic arctangent.

exponentiation::::::::::

e→ a constant with a value that is an approximation of Euler’s number (e)
exp(x)→ finding the value of ex;
log(x)→ the natural logarithm of x
log(x, b)→ the logarithm of x to base b
log10(x)→ the decimal logarithm of x (more precise than log(x,10))
log2(x)→ the binary logarithm of x (more precise than log(x,2))
Note: the pow() function:
pow(x,y)→ finding the value of xy (mind the domains)

The last group consists of some general-purpose functions like::::::::::::::

ceil(x)→ the ceiling of x (the smallest integer greater than or equal to x)
floor(x)→ the floor of x (the largest integer less than or equal to x)
trunc(x)→ the value of x truncated to an integer (be careful – it’s not an equivalent either of ceil or floor)
factorial(x)→ returns x! (x has to be an integral and not a negative)
hypot(x,y)→ returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x,2)+pow(y,2)) but more precise)
'''


