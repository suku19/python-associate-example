"""Operators – data manipulation tools"""

'''
An operator is a symbol of the programming language, which is able to operate on the values.

For example, just as in arithmetic, the + (plus) sign is the operator which is able to add two numbers, giving the result of the addition.

+
-
/
*
** - for exponential (2 ** 3) => 8
// - Find quotient  (5 // 2) => 2
% - Find Remainder (5 % 2) => 1
'''

print("(2 ** 3) value : ", 2 ** 3)

# 8 If both or any one is a float then result will be float too
print("(2 ** 3.) value : ", 2 ** 3.)
print("(2. ** 3) value : ", 2. ** 3)
print("(2. ** 3.) value : ", 2. ** 3.)

# division operator always return a float

print('(4 / 2) value will be always float: ', 4 / 2)

# Arithmetic operators – integer division

''' 
its result lacks the fractional part – it’s absent (for integers), or is always 
equal to zero (for floats); this means that the results are always rounded.
'''

print('(3 // 2) value will be always float: ', 3 // 2)
print('(3. // 2) value will be always float: ', 3. // 2)
print('(3. // 2.) value will be always float: ', 3. // 2.)

# For negative case::

print('(-6 // 4) value will be always float: ', -6 // 4)

'''The real (not rounded) result is −1.5 in both cases. 
The results are the subjects of rounding. The rounding goes toward the lesser 
integer value, and the lesser integer value is −2.
'''

"""Operators and their priorities"""
'''
rules of precedence: (acronym PEMDAS) - > Parentheses, Exponential, Multiplication, Division, Addition, Subtraction.

Next is : < <= > >=
Next : == !=
'''

print('value of (2 ** 2 ** 3) is', (2 ** 2 ** 3))  # Exponentiation operator uses right sided binding

# Sample Solution

print(2 ** 4)  # 16
print(-2 / 4)  # -0.5
print(2. * 4)  # 8.0
print(2 % -4)  # -2
print(2 ** 4.)  # 16.0
print(2 / 4)  # 0.5
print(2 // 4)  # 0
print(2 % 4)  # 2
print(-2 // 4)  # -1 because actual division value is -0.5 and -1 is
print(2 * 4)  # 8
