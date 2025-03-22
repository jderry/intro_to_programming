import unittest

'''
this is a template of a unit test scirpt.
reference: https://docs.python.org/3/library/unittest.html
'''
'''
this template uses a euclid_gcd (module or script) and a function we created in class to aid comprehension.
name your actual unit test script "test_<euclid_gcd WE'RE TESTING>.py"
'''

# 1. get the function to test or import the module to test.
from euclid_gcd import euclid_gcd

# 2. create a class into which we pass the unit tests we want to perform.
class Test_euclid_gcd(unittest.TestCase):

   # 3. create a method for each garbage_filter test to perform.    
   def test_GARBAGE_FILTER_1(self):
        ''' assert arguments are integers
        '''
        with self.assertRaises(AssertionError):
            euclid_gcd(201., 5)
   def test_GARBAGE_FILTER_2(self):
        ''' assert input must be greater than zero
        '''
        with self.assertRaises(AssertionError):
            euclid_gcd(-201, 5)
 
   # 4. create a method for each test to perform.
   def test_euclid_gcd(self):
       result = euclid_gcd(53667, 25527)
       # here, the test ensures that output of the function is indeed the expected output.
       self.assertEqual(result, 201)

# 5. we run the unit tests defined within the class.
# we can modify verbosity level (default=1) to get more or less info as tests run. 
#unittest.main(verbosity=2)

# 6. we set up our unit tests so we can invoke them off the bash command line
if __name__ == '__main__':
    unittest.main()
