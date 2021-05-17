"""String methods: capitalize:"""

'''
1) if the first character inside the string is a letter (note: the first character is an element with an index equal to 0,
not just the first visible character), it will be converted to upper-case;
2) all remaining letters from the string will be converted to lower-case.
'''

str = 'aBcD'

print("Capitalize of 'aBcD' is:", str.capitalize())
print()

"""String methods: lower"""
'''replaces all upper-case letters with their lower-case counterparts'''
print("String methods: lower")
print("'SiGmA=60'.lower() : ", 'SiGmA=60'.lower())
print()

"""String methods: upper"""
'''replaces all lower-case letters with their upper-case counterparts'''
print("String methods: upper")
print("'SiGmA=60'.upper() : ", 'SiGmA=60'.upper())
print()

"""String methods: swapcase"""
'''The swapcase() method makes a new string by swapping the case of all letters within the source string'''
print("String methods: swapcase")
print("Swapcase: ", 'One thing I know, that I know nothing'.swapcase())
print()

"""String methods: title"""
'''it changes every word’s first letter to upper-case'''
print("String methods: title()")
print("title: ", 'One thing I know, that I know nothing'.title())
print()

"""String methods: lstrip"""
'''
The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading 
whitespaces.
'''
print("String methods: lstrip")
print("print('['+' tau '.lstrip()+']') : ", '[' + ' tau '.lstrip() + ']')
print()

'''
The one-parameterlstrip() method does the same as its parameterless version, but removes all characters 
enlisted in its argument (a string), not just whitespaces →
'''
print("'www.cisco.com'.lstrip('w.') : ", 'www.cisco.com'.lstrip('w.'))
print("'www.cisco.com'.rstrip('w.') : ", 'www.cisco.com'.rstrip('.com'))

#  The strip() method combines the effects caused by rstrip() and lstrip()
#  it makes a new string lacking all the leading and trailing whitespaces.
print("print('['+'  aleph  '.strip()+']') : ", '['+'  aleph  '.strip()+']')
print()
"""String methods: center::"""
'''
The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field 
of a specified width.
'''
print("String methods: center::")
print('[' + 'alpha'.center(10) + ']')

'''The two-parameter variant of center() makes use of the character from the second argument, instead of a space →'''
print('[' + 'alpha'.center(20, '*') + ']')
print()

"""String methods: endswith"""
print("String methods: endswith::")
if 'epsilon'.endswith('on'):
    print("'epsilon' ends with 'on'")

print("'omega'.startswith('meg') : ", 'omega'.startswith('meg'))
print()

"""String methods: find"""
print("String methods: find()::")
'''
The find() method is similar to index(), which you already know (it looks for a substring), but:
it’s safer – it doesn’t generate an error for an argument containing a non-existent substring (it returns -1 then)
it works with strings only – don’t try to apply it to any other sequence.
'''

print('Eta'.find('ta'))

# Note: don’t use find() if you only want to check if a single character occurs within a string – the in operator will be significantly faster.

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s
or earlier, when it was popularized by advertisements
for Letraset transfer sheets. It was introduced to
the Information Age in the mid-1980s by the Aldus Corporation,
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = txt.find('the')
print("fnd:", fnd)
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)
print()
print()

"""String methods: rfind"""
print("String methods: rfind()::")
'''
The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones 
devoid of the r prefix), but start their searches from the end of the string, not the beginning 
(hence the prefix r, for right).
'''
print("'abcabc'.rfind('ta'): ", 'abcabc'.rfind('c'))
print("'abcabc'.rfind('b', 5): ", 'abcabc'.rfind('a', 2))
print("'abcabc'.rfind('c', 1, 5): ", 'abcabc'.rfind('c', 1, 5))
print()

"""String methods: isalnum:"""
'''
The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters),
and returns True/False according to the result →
'''

print("String methods: isalnum::")

print("'lambda30'.isalnum(): ", 'lambda30'.isalnum())
print("''.isalnum() : ", ''.isalnum())
print("'aa bb'.isalnum(): ", 'aa bb'.isalnum())
print()

"""String methods: isalpha"""
'''The isalpha() method is more specialized – it’s interested in letters only.'''
print("String methods: isalpha")
print("'lambda30'.isalpha(): ", 'lambda30'.isalpha())
print("''.isalpha() : ", ''.isalpha())
print("'aa bb'.isalpha(): ", 'aa bb'.isalpha())
print("'aabb'.isalpha(): ", 'aabb'.isalpha())
print()

"""String methods: isdigit"""
'''The isdigit() method looks at digits only'''
print("String methods: isdigit")
print("'lambda30'.isdigit(): ", 'lambda30'.isdigit())
print("''.isdigit() : ", ''.isdigit())
print("'123'.isdigit(): ", '123'.isdigit())
print()

"""String methods: islower"""
'''The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.'''
print("String methods: islower()")
print("'aabb'.islower(): ", 'aabb'.islower())
print("'AAbb'.islower(): ", 'AAbb'.islower())
print("'aa bb'.islower(): ", 'aa bb'.islower())
print()

"""String methods: isspace"""
'''The isspace() method identifies whitespaces only – it disregards any other character (the result is False then).'''
print("String methods: isspace")
print("' \n '.isspace() : ", ' \n '.isspace())
print()

"""String methods: isupper"""
'''The isupper() is the upper-case version of islower() – it concentrates on upper-case letters only.'''
print("String methods: isupper")
print("'Xi'.isupper(): ", 'Xi'.isupper())
print()

"""String methods: join"""
'''The join() method is rather complicated, so let us guide you step by step thorough it:

1) as its name suggests, the method performs a join – it expects one argument as a list; it must be assured that all the 
list’s elements are strings – the method will raise a TypeError exception otherwise;
2) all the list’s elements will be joined into one string but . . .
3) . the string from which the method has been invoked is used as a separator, put among the strings;
the newly created string is returned as a result.
'''
print("String methods: join")
print("','.join(['aa', 'bb', 'cc'] : ", ','.join(['aa', 'bb', 'cc']))
print()

"""String methods: replace"""
'''The two-parameter method replace() returns a copy of the original string in which all occurrences  
of the first argument have been replaced by the second argument →'''
print("String methods: replace")
print("'this is it'.replace('is','are') : ", 'this is it'.replace('is', 'are'))
'this is it'.replace('is', 'are', 1)  # limit the no of replacement
print()

"""String methods: split"""
'''
The split() method does what it says – it splits the string and builds a list of all detected substrings.
The method assumes that the substrings are delimited by whitespaces – the spaces don’t take part in the 
operation, and aren’t copied into the resulting list.
'''
print("String methods: split:")
print("'phi   chi\npsi'.split() : ", 'phi   chi\npsi'.split())
# Note: the reverse operation can be performed by the join() method.
print()

""""""
''''''
print("")

print()

""""""
''''''
print("")
