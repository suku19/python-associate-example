"""Opening syntax : stream = open(file, mode='r', encoding=None)"""

'''
“r” open mode: read

the stream will be opened in “read” mode
the file associated with the stream must exist and has to be readable, otherwise open() function raises exception
'''

'''
“w” open mode: write

the stream will be opened in “write” mode
the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists it will
truncated to the length of zero (erased);  if the creation isn't possible (e.g. due to system permissions) the open() 
function raises an exception
'''

'''
“a” open mode: append

the stream will be opened in “append” mode;
the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists the 
virtual recording head will be set at the end of the file (the previous content of the file remains untouched)
'''

'''
“r+” open mode: read and update

the stream will be opened in “read and update” mode;
the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception
both read and write operations are allowed for the stream
'''

'''
“w+” open mode: write and update

the stream will be opened in “write and update” mode;
the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; the previous content
of the file remains untouched
both read and write operations are allowed for the stream
'''

'''
If there is a letter b at the end of the mode string it means that the stream is to be opened in the binary mode. If 
the mode string ends with a letter t the stream is opened in the text mode. This is the default behaviour assumed 
when no binary/text mode specifier was used.

Finally, the successful opening of the file will set the current file position (the virtual reading/writing head) 
before the first byte of the file if the mode is not a and after the last byte of file if the mode is set to a.
'''

try:
    stream = open("C:/SuKu/Dev/Python/file_test/test.txt", "rt")
    # actual processing goes here
    stream.close()
except Exception as exc:
    print("open failed:", exc)

"""
Stream without open function::
We said earlier that any stream operation must be preceded by the open() function invocation. There are three 
well-defined exceptions to the rule. When our program starts the three streams are already opened and don't require 
any extra preparations. What's more, your program can use these streams explicitly if you take care to import the 
sys module:

import sys

because that's where the declaration of the three streams is placed.

The names of these streams look as follows →
"""

'''
1) stdin (as standard input):
the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source
for the running programs
the well-known input() function reads data from stdin by default
'''

'''
2) stdout (as standard output):
the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for 
outputting data by the running program
the well-known print()function outputs the data to stdout stream
'''

'''
3) stderr (as standard error output)
the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where
the running program should send information on the errors encountered during its work
'''

"""Closing Streams::"""
'''
the function expects exactly no arguments;  the stream doesn't need to be opened
the function returns nothing but raises IOError exception in case of error
most developers believe that the close() function always succeeds and thus there is no need to check if it's done its 
task properly. This belief is only partly justified. If the stream was opened for writing and then a series of write 
operations were performed it may happen that the data sent to the stream has not been transferred to the physical 
device yet (due to mechanism called caching or buffering). Since the closing of the stream forces the buffers to 
flush them, it may be that the flushes fail and therefore the close() fails too.
'''


"""Diagnosing stream problems"""
'''
The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can 
access it as follows →

The value of the errno attribute can be compared with one of the predefined symbolic constants defined in the 
errno module.
'''
from os import strerror
try:
    # some stream operations
    open('file', 'r')
except IOError as exc:
    print("File could not be opened:", strerror(exc.errno));
    print("exc.errno : ", exc, exc.errno, sep='***')
