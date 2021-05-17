"""WHILE LOOP"""

# We will store the current greatest number here

max = -999999999

# get the first number

number = int(input("Enter a value or -1 to stop: "))

# if the number is not equal to -1 we will continue

while number != -1:
    if number > max:
        max = number

    # get the next mumber
    number = int(input("Enter a value or -1 to stop: "))

print("The largest number is : ", max)

# note that these two forms are equivalent

num = 1

while num != 0:
    print("Inside while loop, num not equals to zero")
    num = 0

num1 = 0

while num1:
    print("Inside while loop, num1 not equals to zero")
    num1 = 0
