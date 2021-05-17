# looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Looping through a sequence using enumerate

for i, v in enumerate([2,3,4,]):
    print(i,v)

# Looping over two sequence

question = ['name','age','state']
answer = ['Sukanta',24,'Scotland']

for q,a in zip(question,answer):
    print('What is your {0}? It is {1}.'.format(q,a))

# Loop over a sequence in reverse

for i in reversed(range(1, 10, 2)):
    print('Reversed Loop Data:',i)

# To loop over a sequence in sorted order

basket = ['apple', 'orange', 'apple', 'pear', 'orange','banana']
for f in sorted(basket):
    print('Sorted set: ', f)

'''
It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
'''

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print('filtered_data: ', filtered_data)