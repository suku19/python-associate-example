# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or
# when the condition becomes false (with while), but not when the loop is terminated by a break statement.
# This is exemplified by the following loop, which searches for prime numbers:

for n in range(2, 10):
    print(n, range(2, 2))
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# Find even and odd number

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number: ", num)
        continue
    print("Find an odd number: ", num)


# The pass statement does nothing.
# Pass can be used is as a place-holder for a function or conditional body when you are working on new code,
# allowing you to keep thinking at a more abstract level. The pass is silently ignored:

def initlog(*args):
    pass  # Remember to implement this!


"""Loops and else"""

for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2,1):
    print(i)
else:
    print("else:", i)
