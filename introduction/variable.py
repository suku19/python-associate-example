"""Variables – data-shaped boxes"""

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5

print('Result is : ', c)

John = 3
Mary = 5
Adam = 6

# printing variables on one line
print(John, Mary, Adam, sep=",")

# adding variables and printing the result
print(John+Mary+Adam)

# creating the variable Total_Apples
Total_Apples = John + Mary + Adam
print(Total_Apples)

"""Shortcut operators"""

'''
If op is a two-argument operator (this is a very important condition) and the 
operator is used in the following context:

variable = variable op expression;

It can be simplified and shown as follows:

variable op= expression;

Take a look at the examples →
'''

