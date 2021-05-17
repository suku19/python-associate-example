"""Nested functions in Python"""

'''
A function which is defined inside another function is known as nested function. 
Nested functions are able to access variables of the enclosing scope.

In Python, these non-local variables can be accessed only within their scope and not 
outside their scope. This can be illustrated by following example:
'''


# Python program to illustrate
# nested functions
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey!')

'''
As we can see innerFunction() can easily be accessed inside the outerFunction body 
but not outside of it’s body. Hence, here, innerFunction() is treated as nested 
Function which uses text as non-local variable.
'''

"""Python Closures"""


# Program Must have a function inside a function.
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.

# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis


if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()

'''
1. As observed from above code, closures help to invoke function outside their scope.

2. The function innerFunction has its scope only inside the outerFunction. But with the use 
of closures we can easily extend its scope to invoke a function outside its scope.
'''

"""When and why to use Closures:"""

'''
1. As closures are used as callback functions, they provide some sort of data hiding. 
This helps us to reduce the use of global variables.
2. When we have few functions in our code, closures prove to be efficient way. But if we 
need to have many functions, then go for class (OOP).

'''

print()


def makeclosure(par):
    loc = par

    def power(p):
        return p * loc

    return power


fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))
