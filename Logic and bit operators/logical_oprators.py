"""NOT"""

'''
var > 0  =>  not(var <= 0)
var != 0  =>  not(var == 0)
'''

i = 1

j = not i
print("value of 'not 1' : ", j)

j = not not i
print("value of 'not not 1' : ", j)


"""Logical values vs. single bits"""

'''
However, there are four operators that allow you to manipulate single bits of data. They are called bitwise operators. 
They cover all the operations we mentioned before in the logical context, and one additional operator. This is the xor 
(as in exclusive or) operator, and is denoted as ^ (caret). Here are all of them:

&     (ampersand)  bitwise conjunction
|        (bar)              bitwise disjunction
~     (tilde)            bitwise negation
^     (caret)           bitwise exclusive or (xor)
Let’s make it easier:

& requires exactly two 1s to provide 1 as the result;
| requires at least one 1 to provide 1 as the result;
^ requires exactly one 1 to provide 1 as the result.
Let us add an important remark: the arguments of these operators must be integers; we must not use floats here.
'''

a = 15
b = 22

# we are dealing with logical conjunction here. Both variable i and j is non zero, so will be deemed to represent True.
log = (a and b)
print("value of 'a and b' is : ", log)

# now bitwise operation
bit = a & b
print("value of 'a & b' is : ", bit)

# Let’s look at the negation operators now.

logneg = not i

print("value of 'not i' is", logneg)

bitneg = ~ i

print("value of '~ i' is", bitneg)

