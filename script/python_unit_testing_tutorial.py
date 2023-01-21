''' these contents follow the python tutorial:
    Unit Testing Your Code With the unittest Module
    by Corey Schafer, https://www.youtube.com/watch?v=6tNS--WetLI
'''
def add(x, y):
   return x + y
   
def subtract(x, y):
   return x - y
   
def multiply(x, y):
   return x * y
   
def divide(x, y):
   if y == 0:
      raise ValueError("Division by zero: Illegal operation!")
   return x / y
