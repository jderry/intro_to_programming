''' these contents follow the python tutorial:
    Unit Testing Your Code With the unittest Module
    by Corey Schafer, https://www.youtube.com/watch?v=6tNS--WetLI
'''
# this file holds the unit tests

# rename this file to conform to unit testing convention to:
# test_calc.py

import unittest
import calc # the file with the functions we're testing as we develop our code

# create a class for testing that inherits unittest.TestCase
class TestCalc(unittest.TestCase):
   # write methods to test the defs in the calc.py file
   # method names must start with: test_
   def test_add(self):
      result = calc.add(10, 5)
      self.assertEqual(result, 15)
      # make sure to add edge cases
   
''' here we set the code up so that it can run on the command line
    without the -m option (import module)
'''
if __name__ == '__main__':
   unittest.main()
