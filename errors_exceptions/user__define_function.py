'''

Programs may name their own exceptions by creating a new exception class
(see Classes for more about Python classes). Exceptions should typically be
derived from the Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are
usually kept simple, often only offering a number of attributes that allow information
about the error to be extracted by handlers for the exception. When creating a module
that can raise several distinct errors, a common practice is to create a base class for
exceptions defined by that module, and subclass that to create specific exception classes
for different error conditions:

'''

class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

class InputError (Error):
    '''Exception raised for errrors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    '''

    def __init__(self,expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    '''
    Raised when an operation attempts a state transition that's not allowed.

    Attritutes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    '''

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


try:
    raise InputError('abc','message')
except InputError as err:
    print(err)
    print(type(err))
    print(err.args)