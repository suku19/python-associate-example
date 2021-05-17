'''
The last except clause may omit the exception name(s), to serve as a wildcard. 
Use this with extreme caution, since it is easy to mask a real programming error in this way! 
It can also be used to print an error message and then re-raise the exception 
(allowing a caller to handle the exception as well):
'''

import sys

try:
    f = open('abc.txt')
    s = f.readline()
    i = int(s.strip())
    # raise TypeError
except OSError as err:
    print("Os error : {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info())
    # raise

'''
The try … except statement has an optional else clause, which, when present, must follow all
 except clauses. It is useful for code that must be executed if the try clause does not 
 raise an exception.  For example:
'''
for arg in sys.argv[1:]:
    try:
        # raise ValueError
        # f = open(arg, 'r')
        f = open('abc.txt', 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

'''
When an exception occurs, it may have an associated value, also known as the exception’s argument.
The presence and type of the argument depend on the exception type. The variable is bound to an 
exception instance with the arguments stored in instance.args.
'''

try:
    raise Exception('arg1', 'arg2')
except Exception as exp:
    print(type(exp))  # the exception instance
    print(exp.args)  # arguments stored in .args
    print(exp)  # __str__ allows args to be printed directly
    # but may be overridden in exception subclasses
    x, y = exp.args  # unpack arguments
    print('X: ', x, ' and Y:', y)

'''
Exception handlers don’t just handle exceptions if they occur immediately in the try clause, 
but also if they occur inside functions that are called (even indirectly) in the try clause.
For example:
'''


def this_fail():
    x = 1 / 0


try:
    this_fail()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

'''
The raise statement allows the programmer to force a specified exception to occur. 
For example:
'''

# raise NameError('HiThere')
# raise ValueError  # shorthand for 'raise ValueError()'


'''
If you need to determine whether an exception was raised but don’t intend to handle it, 
a simpler form of the raise statement allows you to re-raise the exception:
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    #raise


'''
Finally:

The try statement has another optional clause which is intended to define clean-up actions that 
must be executed under all circumstances. 

A finally clause is always executed before leaving the try statement, whether an exception has 
occurred or not.

For example:
'''

def divide(x, y):
    try:
        result = x/y;
    except ZeroDivisionError:
        print('Division by zero!')
    else:
        print('Result is: ', result)
    finally:
        print("Executing finally clause.")

divide(10, 3)
divide(2, 0)
divide('3','4')

'''
Predefined Clean-up Actions:

The problem with this code is that it leaves the file open for an indeterminate
amount of time after this part of the code has finished executing. 
for line in open("myfile.txt"):
    print(line, end="")


The with statement allows objects like files to be used in a way that ensures they are always
cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
'''

