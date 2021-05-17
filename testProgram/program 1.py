"""
We’ve written it using the following assumptions:

it accepts Latin letters only (note: the Romans used neither whitespaces nor digits)
all letters of the message are in upper case (note: the Romans knew only capitals)
Let’s trace the code:

line 01: ask the user to enter the open (unencrypted), one-line message;
line 02: prepare a string for an encrypted message (empty for now)
line 03: start the iteration through the message;
line 04: if the current character is not alphabetic . . .
line 05: . . . ignore it;
line 06: convert the letter to upper-case (it’s preferable to do it blindly, rather than check whether it’s needed or not)
line 07: get the code of the letter and increment it by one;
line 08: if the resulting code has “left” the Latin alphabet (if it’s greater than the Z code) . . .
line 09: . . . change it to the A code;
line 10: append the received character to the end of the encrypted message;
line 11: print the cipher.
"""

text = input("Enter message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    cipher += chr(code)
print(cipher)