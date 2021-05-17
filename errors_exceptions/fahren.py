prompt = "Enter Fahrenheit temperature:"
inp = input(prompt)
try:
    farh = float(inp)
    cel = (farh -32.0) *5/9
    print(cel)
except:
    print('Please enter a number value')
