def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# valid call
print(parrot(1000))                                          # 1 positional argument
print(parrot(voltage=1000))                                  # 1 keyword argument
print(parrot(voltage=1000000, action='VOOOOOM'))             # 2 keyword arguments
print(parrot(action='VOOOOOM', voltage=1000000))             # 2 keyword arguments
print(parrot('a million', 'bereft of life', 'jump'))         # 3 positional arguments
print(parrot('a thousand', state='pushing up the daisies'))  # 1 positional, 1 keyword
print(parrot('1000', state=1000000))                         # non-keyword argument before a keyword argument

# Invalid call
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument



# function with list and dictionary

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("I am sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))