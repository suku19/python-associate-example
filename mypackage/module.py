# print("I like to be a module..")
print(__name__)

__counter = 0


def sum(list):
    global __counter
    __counter += 1
    sum = 0
    for e1 in list:
        sum += e1
    return sum


'''
when you run a file directly, its __name__ variable is set to __main__;
when a file is imported as a module, its __name__ variable is set to the file’s name (excluding .py)
'''

if __name__ == "__main__":
    print("Invoked from Module..")
    l = [i + 1 for i in range(5)]
    print(sum(l))
else:
    print("Invoked by the other user or module")
