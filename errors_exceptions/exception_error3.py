def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError as e:
        print("e: ", e)
        print("e.__str__() : ", e.__str__())
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say good bye")
        return n


print(reciprocal(2))
print(reciprocal(0))
print()
print("Print exception tree::")
print(BaseException.__subclasses__())
print()

def PrintExcTree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end='')
    if nest > 0:
        print("   +---", end='')
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        PrintExcTree(subclass, nest + 1)


PrintExcTree(BaseException)
