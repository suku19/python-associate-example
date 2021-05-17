"""writing to text file"""
print("::writing to text file::")

from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        s = 'Line #' + str(i + 1) + '\n'
        fo.write(s)
        # for ch in s:
        #     fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
