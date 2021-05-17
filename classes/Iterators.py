for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)

'''
 Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that 
 defines the method __next__() which accesses elements in the container one at a time. When there are no more elements,
 next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method 
 using the next() built-in function; this example shows how it all works:
'''

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

'''
Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior 
to your classes. Define an __iter__() method which returns an object with a __next__() 
method. If the class defines __next__(), then __iter__() can just return self:
'''


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)
        print('Input String is: ', data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

''':::Generators:::'''
'''
Generators are a simple and powerful tool for creating iterators. They are written like 
regular functions but use the yield statement whenever they want to return data. Each time 
next() is called on it, the generator resumes where it left off (it remembers all the data 
values and which statement was last executed).
'''


def reverse(data):
    print(len(data))
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

'''Generator Expressions'''

print('Sum of square: ',sum(i*i for i in range(10)))                 # sum of squares