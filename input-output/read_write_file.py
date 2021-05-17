with open('abc.txt', 'a') as f:
    # Read a file
    # print(f.readline())
    # print(f.readline())
    # print(f.read())

    # For reading lines from a file, you can loop over the file object
    # for line in f:
    #     print(line, end='')

    # If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    # print(f.readlines())
    # print(list(f))

    # Write to a file
    f.write('This is a new line added through write\n')
    #f.write('This is a test\n')

    '''
    Other types of objects need to be converted – either to a 
    string (in text mode) or a bytes object (in binary mode) – before writing them:
    '''
    #value = ('the answer', 42)
    #s = str(value)  # convert the tuple to string
    #f.write(s)

    f.read


f.closed
