# """Read individual characters:: stream.read(no_of_char):"""
# print("Read individual characters:: stream.read(1):")
# from os import strerror
#
# try:
#     cnt = 0
#     s = open('abc.txt', "rt")
#     # read a desired number of characters (including just one) from the file, and return them as a string;
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("Characters in file:", cnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))
#
# print()
#
# print("Read whole file..read()")
# # read the whole file to the memory at once, you can do it – the read() function, invoked
# # without any arguments or with an argument that evaluates to None, will do the job for you.
# try:
#     cnt = 0
#     s = open('abc.txt', 'rt')
#     content = s.read()
#     for ch in content:
#         print(ch, end='')
#         cnt += 1
#     s.close()
#     print("Characters in file:", cnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))
#
# print()
#
# print("::Read individual line from file: readline():")
#
# from os import strerror
#
# try:
#     ccnt = lcnt = 0
#     s = open("abc.txt", 'rt')
#     line = s.readline()
#     while line != "":
#         lcnt += 1
#         for ch in line:
#             print(ch, end='')
#             ccnt += 1
#         line = s.readline()
#     s.close()
#     print("Characters count in file:", ccnt)
#     print("Line count in file:", lcnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))
#
# print()
#
# print("Read all the line from file: readlines():")
#
# from os import strerror
#
# try:
#     ccnt = lcnt = 0
#     for line in open('text.txt', 'rt'):  # object returned by the open() function in text mode is an instance of the iterable class.
#         lcnt += 1
#         for ch in line:
#             print(ch, end='')
#             ccnt += 1
#     print("Characters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))


for x in open('abc.txt','rt'):

    print(x)
