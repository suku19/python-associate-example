import math
import random

print(math)

degrees = 45
radians = degrees / 360 * 2 * math.pi
print(radians)
print(math.sin(radians))

print(4 / 2 * 2 * 2)

# math random
print('Generate random number: ')
for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))  # Range random

# To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
print(random.choice(t))
