#  Write Fibonacci series up to n


def fib(n):
    """Print a Fibonacci series up ro n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


f100 = fib2(100)  # call it
print(f100)  # write the result


def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier
