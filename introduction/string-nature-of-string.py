"""
Python’s strings (or simply strings, as we’re not going to discuss any other language’s strings) are immutable sequences
"""

word = 'by'
print("Length of string \"by\" is: ", len(word))

print()
empty = ''
print("A string can be empty, length of empty string is:", empty.__len__())

print()
print("A backslash (\\) used as an escape character is not included in the string’s total length.")
I_am = 'I\'am'
print("length of 'I\'am' is:", len(I_am))

print()
print("String occupying more than one line::")

multiline = '''abc
def'''

print("length of multiline string: ", len(multiline))

"""String has own set of permissible operations"""

print()
print("Concatenated::")

str1 = 'a'
str2 = 'b'
print('value of str1 + str2 is : ', str1 + str2)

print()
print("Replicated::")
print('value of (4 * a) is : ', 4 * 'a')
print('value of (b * 4) is : ', 'b' * 4)

"""ASCII CODE"""
'''
If you want to know a specific character’s ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).

The function needs a one-character string as its argument – breaching this requirement causes a TypeError exception, 
and returns a number representing the argument’s code point.
'''
print()
print("ASCII/UNICODE:: function ord(string) and chr(number)")

c1 = 'a'
print("ascii code of a is: ", ord(c1))

try:
    ord('ab')
except TypeError:
    print("Error: It's accepts a one-character string as its argument")

print("value of ascii code 97 is: ", chr(97))

"""String sequence::"""
print()
print("String sequence::")

str3 = 'abcdef'

for i in range(str3.__len__()):
    print(str3[i], end=' ')

# Sequence capabilities:

print("min('aAbByYzZ') : ", min('aAbByYzZ'))

t = 'The Knights Who Say "Ni!"'
print("t: ", t)
print('max of t is:', '[' + max(t) + ']')
t = [0, 1, 2]
print('In case of tuple [0, 1, 2]: ', max(t))

print("Index of b in string 'aAbByYzZ' : ", 'aAbByYzZ'.index('bB'))

# Iterating through the strings works, too. Look at the example →
print('\nIterating through the strings directly')
for ch in str3:
    print(ch, end=' ')

print()
print()
print("Slice:::")
alpha = "abdefg"
print("Value of alpha is: ", alpha)
print('alpha[3:]: ', alpha[3:])
print('alpha[:3]: ', alpha[:3])
print('alpha[3:-2]: ', alpha[3:-2])
print('alpha[-3:4]: ', alpha[-3:4])
print('alpha[::2]: ', alpha[::2])
print('alpha[1::2]: ', alpha[1::2])

print()
print("In and not in operator: ")
print("'a' in alpha: ", 'a' in alpha)
print("'y' not in alpha: ", 'y' not in alpha)

print()
print("Python’s strings are immutable. We can't do an index level deletion..")
print("String don't have the append() or insert() method as well..")
print()
print("The list() function takes its argument (a string) and creates a new list containing all the string’s characters, one per list element.:::")

print(list('abcabc'))

print()
print("The count method count all occurrences of the element inside the sequence::")
print("No of occurrence of b in string 'abcdabcdb' is: ", 'abcdabcdb'.count('b'))
