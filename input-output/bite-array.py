"""::!How to write bytes to the stream::"""
print("::!How to write bytes to the stream::")

from os import strerror

data = bytearray(10)  # declare byte array
for i in range(len(data)):
    data[i] = 10 + i  # add the data in byte array
try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

print()
print()
print("::How to read bytes from the stream::")

print("Approach 1::")
data = bytearray(10)
bf = open('file.bin', 'rb')
bf.readinto(data)
bf.close()

for b in data:
    print(hex(b), end=' ')

print()
print("Approach 2::")
from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
