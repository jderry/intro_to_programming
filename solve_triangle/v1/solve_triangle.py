
''' solve_triangle. we put the function into its own module.
'''
# initialization
from numpy import deg2rad, rad2deg
from solve_triangle_sbr import \
    solve_sss, solve_aaa, solve_asa, solve_sas, solve_ssa, solve_ass, solve_aas, solve_saa

def solve_triangle(side1=None, side2=None, side3=None,\
                   angle1=None, angle2=None, angle3=None,\
                   degrees=True, rnd=False, dec_digs=None) -> tuple:
    '''(pos real, pos real, pos real, pos real, pos real, pos real, bool, bool, int) -> tuple, 
           where "pos real" means positive real; i.e., positive int or float
       Requires NumPy.
       Given 3 parts of a triangle (sides or angles, as in 3 sides or 1 side and 2 angles),
           return values for all sides and angles.
       Angles can be either all in degrees or all in radians. The default is degrees.
       If rnd=True, results are rounded by the decimal degrees passed into the function.
           The default is no rounding.
       Output tuple follows the same ordering as the function's argument list:
       (side1, side2, side3, angle1, angle2, angle3)
       Examples:
       >>>solve_triangle(side1=7, side2=5, angle3=49, rnd=True, dec_digs=2)
       (7, 5, 5.3, 85.59, 45.41, 49.0) # angles in degrees, rounding to 2 decimal digits
    '''
    # begin garbage filter
    # ensure side and angle values are positive reals.
    pos_reals = True
    if side1 and not (isinstance(side1, (int, float)) and side1 > 0):
        pos_reals = False
    if side2 and not (isinstance(side2, (int, float)) and side2 > 0):
        pos_reals = False
    if side3 and not (isinstance(side3, (int, float)) and side3 > 0):
        pos_reals = False
    if angle1 and not (isinstance(angle1, (int, float)) and angle1 > 0):
        pos_reals = False
    if angle2 and not (isinstance(angle2, (int, float)) and angle2 > 0):
        pos_reals = False
    if angle3 and not (isinstance(angle3, (int, float)) and angle3 > 0):
        pos_reals = False
    assert pos_reals, "triangle sides and angles must be positive reals"
    # ensure degrees and rnd are bools.
    # ensure dec_digs is a natural number.
    # end garbage filter


    # convert degrees to radians for calculations.
    # numpy uses radians for angular measurements.
    if degrees:
        if angle1:
            angle1 = deg2rad(angle1)
        if angle2:
            angle2 = deg2rad(angle2)
        if angle3:
            angle3 = deg2rad(angle3)

    ##### BEGIN MAIN #####
    # the conditional branching determines which subroutine applies
    # for the given input
    if side1 and side2 and side3:
        solution_tuple = solve_sss(side1, side2, side3, angle1, angle2, angle3)

    elif angle1 and angle2 and angle3:
        solution_tuple = solve_aaa(side1, side2, side3, angle1, angle2, angle3)

    elif (angle1 and side3 and angle2) or \
         (angle2 and side1 and angle3) or \
         (angle3 and side2 and angle1):
        solution_tuple = solve_asa(side1, side2, side3, angle1, angle2, angle3)

    elif (side1 and side2 and angle3) or \
         (side2 and side3 and angle1) or \
         (side3 and side1 and angle2):
        solution_tuple = solve_sas(side1, side2, side3, angle1, angle2, angle3)

    elif (side1 and side2 and angle1) or \
         (side2 and side3 and angle2) or \
         (side3 and side1 and angle3):
        solution_tuple = solve_ssa(side1, side2, side3, angle1, angle2, angle3)

    elif (angle2 and side1 and side2) or \
         (angle3 and side2 and side3) or \
         (angle1 and side3 and side1):
        solution_tuple = solve_ass(side1, side2, side3, angle1, angle2, angle3)

    elif (angle1 and angle2 and side1) or \
         (angle2 and angle3 and side2) or \
         (angle3 and angle1 and side3):
        solution_tuple = solve_aas(side1, side2, side3, angle1, angle2, angle3)

    elif (side1 and angle3 and angle1) or \
         (side2 and angle1 and angle2) or \
         (side3 and angle2 and angle3):
        solution_tuple = solve_saa(side1, side2, side3, angle1, angle2, angle3)

    else:
        pass
    # each subroutine returns a return_tuple
    ##### END MAIN #####

    # convert radians to degrees
    if degrees:
        # convert immutable tuple to mutable list
        solution_list = list(solution_tuple)
        # convert the angular values
        solution_list[3], solution_list[4], solution_list[5] =\
            rad2deg(solution_list[3]),\
            rad2deg(solution_list[4]),\
            rad2deg(solution_list[5])
        # coerce the list back into a tuple
        solution_tuple = tuple(solution_list)

    # return a tuple, with and without rounding
    if not rnd:
        return solution_tuple

    # in this return statement, we render a new tuple from converted values
    # in solution_tuple. note that we preserve the order of the values.
    return round(solution_tuple[0], dec_digs), round(solution_tuple[1], dec_digs),\
           round(solution_tuple[2], dec_digs), round(solution_tuple[3], dec_digs),\
           round(solution_tuple[4], dec_digs), round(solution_tuple[5], dec_digs)
