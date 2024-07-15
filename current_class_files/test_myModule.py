import unittest

'''
this is a template of a unit test module.
reference: https://docs.python.org/3/library/unittest.html
'''
'''
this template uses a module and a function we created in class to aid comprehension.
name your actual unit test module "test_<myModule WE'RE TESTING>.py"
'''

# 1. get the function to test or import the module to test.
from myModule import euclid_gcd, rev_compl, ensureNuclStrClean

# 2. create a class into which we pass the unit tests we want to perform.
class Test_myModule(unittest.TestCase):

   #### ensureNuclStrClean tests ####
   def test_ensureNuclStrClean_garbage_filter_1(self):
        ''' assert input must be a string
        '''
        with self.assertRaises(AssertionError):
            ensureNuclStrClean(2.3)

   def test_ensureNuclStrClean(self):
        ''' assert input must be a string
        '''
        with self.assertRaises(AssertionError):
            ensureNuclStrClean('gxttxca')

   #### euclid_gcd unit tests #####
   def test_euclid_gcd_garbage_filter_1(self):
        ''' assert input must be a string
        '''
        with self.assertRaises(AssertionError):
            euclid_gcd(53667., 25527)
   
   # create a method for each test to perform.
   def test_euclid_gcd(self):
       result = euclid_gcd(53667, 25527)
       # here, the test ensures that output of the function is indeed the expected output.
       self.assertEqual(result, 201)

   ##### rev_compl unit tests #####
   def test_rev_compl_garbage_filter_1(self):
        ''' assert input must be a string
        '''
        with self.assertRaises(AssertionError):
            rev_compl(45)
            
   def test_rev_compl_garbage_filter_2(self):
       ''' check each symbol in input string
           is a nucleotide. if not, return tuple
           with a) dictionary of index/non-nucleotide pairs,
           and b) string that explains the dictionary
       '''
       with self.assertRaises(AssertionError):
           rev_compl('gattaxa')

   # create a method for each test to perform.
   def test_rev_compl(self):
       result = rev_compl('gattaca')
       # here, the test ensures that output of the function is indeed the expected output.
       self.assertEqual(result, 'tgtaatc')


# 5. we run the unit tests defined within the class.
# we can modify verbosity level (default=1) to get more or less info as tests run. 
#unittest.main(verbosity=2)

# 6. we set up our unit tests so we can invoke them off the bash command line
if __name__ == '__main__':
    unittest.main()
