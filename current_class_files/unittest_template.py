import unittest

'''
this is a template of a unit test scirpt.
reference: https://docs.python.org/3/library/unittest.html
'''
'''
this template uses a FILE (module or script) and a function we created in class to aid comprehension.
name your actual unit test script "test_<FILE WE'RE TESTING>.py"
'''

# 1. get the function to test or import the module to test.
from FILE import FUNC

# 2. create a class into which we pass the unit tests we want to perform.
class Test_FILE(unittest.TestCase):

   # 3. create a method for each garbage_filter test to perform.    
   def test_GARBAGE_FILTER_1(self):
        ''' assert input must be a string
        '''
        with self.assertRaises(AssertionError):
            FUNC(BAD_ARG)
   
   # 4. create a method for each test to perform.
   def test_FUNC(self):
       result = FUNC(ARG)
       # here, the test ensures that output of the function is indeed the expected output.
       self.assertEqual(result, RESULT)

# 5. we run the unit tests defined within the class.
# we can modify verbosity level (default=1) to get more or less info as tests run. 
#unittest.main(verbosity=2)

# 6. we set up our unit tests so we can invoke them off the bash command line
if __name__ == '__main__':
    unittest.main()
