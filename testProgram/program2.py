"""
The third program shows a simple method allowing you to input a line filled with numbers, and to process them easily. Note: the routine input()function, combined together with the int() or float() functions, is unsuitable for this purpose.

The processing will be extremely easy – we want the numbers to be summed.

This is the code →

Using list comprehension may make the code slimmer. You can do that if you want.

Let’s present our version:

line 01: ask the user to enter a line filled with any number of numbers (the numbers can be floats)
line 02: split the line receiving a list of substrings;
line 03: initiate the total sum to zero;
line 04: as the string → float conversion may raise an exception, it’s best to continue with the protection of the try-except block;
line 05: iterate through the list . . .
line 06: . . . and try to convert all its elements into float numbers; if it works, increase the sum;
line 07: everything is good so far, so print the sum;
line 08: the program ends here in the case of an error;
line 09: print a diagnostic message showing the user the reason for the failure.

"""

line = input("Enter line full of numbers - separate them with spaces: ")
strings = line.split()
sum = 0
try:
    for substr in strings:
        sum += float(substr)
    print("Sum =", sum)
except:
    print("It's not a number:", substr)
