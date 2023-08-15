''' this unittest code tests solve_triangle, v2
    test cases taken from google searches.
'''

import unittest
from solve_triangle import solve_triangle

class TestSolveTriangle(unittest.TestCase):
    ''' this class creates an object instance
        that applies unit tests
        to the garbage filter assertions
        and the main code.
    '''
    # garbage filter tests
    def test_garbage_filter_1(self):
        ''' assert val1 is a positive real
        '''
        with self.assertRaises(AssertionError):
            solve_triangle('sss', -3, 4, 5)
    def test_garbage_filter_2(self):
        ''' assert val2 is a positive real
        '''
        with self.assertRaises(AssertionError):
            solve_triangle('sss', 3, 4j, 5)
    def test_garbage_filter_3(self):
        ''' assert val3 is a positive real
        '''
        with self.assertRaises(AssertionError):
            solve_triangle('sss', 3, 4, -5)


    def test_solve_triangle_sss1(self):
        '''('sss', 3, 4, 5, dec_digs=2)
        '''
        result = solve_triangle('sss', 3, 4, 5, dec_digs=2)
        self.assertEqual(result, (3, 4, 5, 36.87, 53.13, 90.0))
    def test_solve_triangle_sss2(self):
        '''('sss', 5.1, 7.9, 3.5, dec_digs=1)
        '''
        result = solve_triangle('sss', 5.1, 7.9, 3.5, dec_digs=1)
        self.assertEqual(result, (5.1, 7.9, 3.5, 28.4, 132.6, 19.0))
    def test_solve_triangle_aaa1(self):
        '''('aaa', 95, 35, 50, dec_digs=5)
        '''
        result = solve_triangle('aaa', 95, 35, 50, dec_digs=5)
        self.assertEqual(result, (1.73681, 1.0, 1.33556, 95.0, 35.0, 50.0))
    def test_solve_triangle_sas1(self):
        '''('sas', 5, 49, 7, dec_digs=4)
        '''
        result = solve_triangle('sas', 5, 49, 7, dec_digs=4)
        self.assertEqual(result, (5, 7, 5.2987, 45.4117, 85.5883, 49.0))

        
    def test_solve_triangle_ssa1(self):
        '''('ssa', 22, 32, 32, dec_digs=4)
           2 solutions
        '''
        result = solve_triangle('ssa', 22, 32, 32, dec_digs=4)
        self.assertEqual(result, (22, 32, (41.1535, 13.1216), 32.0, (50.425, 129.575), (97.575, 18.425)))
    def test_solve_triangle_ass1(self):
        '''('ssa', 22, 32, 32, dec_digs=4)
           2 solutions
        '''
        result = solve_triangle('ass', 32, 32, 22, dec_digs=4)
        self.assertEqual(result, (22, 32, (41.1535, 13.1216), 32.0, (50.425, 129.575), (97.575, 18.425)))
        
if __name__== '__main__':
    unittest.main()
