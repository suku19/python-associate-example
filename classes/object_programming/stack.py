"""The stack – the procedural approach"""
print("The stack – the procedural approach:::::::")
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


print("Stack Push: 3,2,1")
push(3)
push(2)
push(1)
print("Stack Pop:")
print(pop())
print(pop())
print(pop())
print()

"""A stack from scratch - Object Oriented approach"""

print("Stack : Object Oriented approach::::::::")


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


stack1 = Stack()
print("Stack Push: 3,2,1")
stack1.push(3)
stack1.push(2)
stack1.push(1)
print("Stack Pop:")
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print()

"""Extend stake functionality"""
print("Extend stake functionality:::")


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)  # Explicitly invoke superclass constructor
        self.__sum = 0  # private variable, not able to access outside of the class

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum;


stack2 = AddingStack()
for i in range(5):
    stack2.push(i)
print("Sum of the stack element: ", stack2.getSum())
for i in range(5):
    print("stack2.pop()) : ", stack2.pop())
