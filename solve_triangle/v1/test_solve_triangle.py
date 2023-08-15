import unittest
from solve_triangle import *
from solve_triangle_sbr import *

class test_solve_triangle(unittest.TestCase):

    def test_garbage_filter_1(self):
        ''' over-defined error
        '''
        with self.assertRaises(AssertionError):
            solve_triangle(4, 5, 6, 90)
    def test_garbage_filter_2(self):
        ''' round without specifying number of decimal digits
        '''
        with self.assertRaises(AssertionError):
            solve_triangle(rnd=True)

    def test_solve_triangle_sss1(self):
        result = solve_triangle(side1=3, side2=4, side3=5, rnd=True, dec_digs=2)
        self.assertEqual(result, (3, 4, 5, 36.87, 53.13, 90.0))
    def test_solve_triangle_sss2(self):
        result = solve_triangle(side1=5.1, side2=7.9, side3=3.5, rnd=True, dec_digs=1)
        self.assertEqual(result, (5.1, 7.9, 3.5, 28.4, 132.6, 19.0))
    def test_solve_triangle_aaa1(self):
        result = solve_triangle(angle1=95, angle2=35, angle3=50, rnd=True, dec_digs=5)
        self.assertEqual(result, (1.73681, 1.0, 1.33556, 95.0, 35.0, 50.0))
    def test_solve_triangle_ssa(self):
        result = solve_triangle(side1=7, side2=5, angle3=49, rnd=True, dec_digs=2)
        self.assertEqual(result, (7, 5, 5.3, 85.59, 45.41, 49.0))
        
if __name__== '__main__':
    unittest.main()



