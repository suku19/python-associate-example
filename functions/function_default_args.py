# The most useful form is to specify a default value for one or more arguments.


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


# Call the function in different way
print(ask_ok('Do you want to proceed? '))
print(ask_ok('Ok to overwrite? ', 2))
print(ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no please!'))


# The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))


# If you don’t want the default to be shared between subsequent

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
