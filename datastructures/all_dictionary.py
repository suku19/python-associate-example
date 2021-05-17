# building,
dic = {'jack':4098, 'sape':4139}

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('Using dict() constructor: ',tel)

#dict comprehensions

{x: x*2 for x in range(1,6)}
#///////////////////////////////////////////////////////////////////////////////////////
# indexing,
# /////////////////////////////////////////////////////////////////////////////////////
# adding and removing keys,
dic['guido']=4127
print(dic)

del dic['jack']
print(dic)
# //////////////////////////////////////////////////////////////////////////////////////
# iterating through dictionaries as well as their keys and values

for k,v in dic.items():
    print('Key:', k,' and Value:',v)

# # /////////////////////////////////////////////////////////////////////////////////////,
# checking key existence, 
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
'robin' in knights
# /////////////////////////////////////////////////////////////////////////////////////
# keys(), items() and values() methods
print(knights.keys()) # return list
print(knights.values()) # return list
print(knights.items()) # return key value tuples
