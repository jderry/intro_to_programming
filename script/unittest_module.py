''' the functions in this module come from corey schafer's tutorial on unit testing in python,
    https://www.youtube.com/watch?v=6tNS--WetLI
    i recommend watching the tutorial, as well.
'''

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    if int(y) == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
