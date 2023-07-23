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
    def test_solve_triangle_ssa1(self):
        '''('ssa', 8, 13, 31, dec_digs=4)
        '''
        result = solve_triangle('ssa', 8, 13, 31, dec_digs=4)
        self.assertEqual(result, (8, 13, 15.5216, 31.0, 56.8181, 92.1819))

if __name__== '__main__':
    unittest.main()
