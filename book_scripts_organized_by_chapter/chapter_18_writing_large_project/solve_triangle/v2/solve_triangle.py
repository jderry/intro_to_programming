''' solve_triangle. we put the function into its own module.
    v2, we use a string to ID the known parts of the triangle,
    and we remove the round bool and instead test dec_digs.
    TO DO: solve for multiple possible solutions,
    as with SSA and AAS triangles.
'''
# initialization
from numpy import deg2rad, rad2deg
from solve_triangle_modules import \
    solve_sss, solve_aaa, solve_asa, solve_sas, solve_ssa, solve_ass, solve_aas, solve_saa

def solve_triangle(tri_type: str, val1: (int, float), val2: (int, float),val3: (int, float),\
                             degrees: bool=True, dec_digs=None) -> tuple:
    '''(str, pos real, pos real, pos real, bool, int) -> tuple, 
           where "pos real" means positive real; i.e., positive int or float
       Requires NumPy.
       Given 3 parts of a triangle, return values for all sides and angles.
       Angles can be either all in degrees or all in radians. The default is degrees.
       Return tuple follows this ordering:
       (side1, side2, side3, angle1, angle2, angle3)
       Examples:
       >>>solve_triangle(side1=7, side2=5, angle3=49, rnd=True, decDigs=2)
       (7, 5, 5.3, 85.59, 45.41, 49.0) # angles in degrees, rounding to 2 decimal digits
    '''
    # begin garbage filter

    # assert that the sides and angles are positive reals.
    assert (isinstance(val1, (int, float)) and val1 > 0) and \
           (isinstance(val2, (int, float)) and val2 > 0) and \
           (isinstance(val3, (int, float)) and val3 > 0),\
           "triangle sides and angles must be positive reals"
    # assert that degrees is a bool.
    assert isinstance(degrees, bool),\
        "the degrees argument must be either True or False"
    # assert that dec_digs value, if not None, is a natural number.
    if dec_digs is not None:
        assert isinstance(dec_digs, int) and dec_digs >= 0,\
        "the dec_digs argument must be a natural number, 0 or greater"
    # end garbage filter

    # ensure tri_type string passed into argument list is lowercase.
    tri_type = tri_type.lower()

    # we replace conditional branches with a dictionary
    # this dictionary updates values, if degrees (the default)
    # and not radians are specified
    if degrees:
        deg_dict =\
            {'sss': (val1, val2, val3),\
             'aaa': (deg2rad(val1), deg2rad(val2), deg2rad(val3)),\
             'asa': (deg2rad(val1), val2, deg2rad(val3)),\
             'sas': (val1, deg2rad(val2), val3),\
             'ssa': (val1, val2, deg2rad(val3)),\
             'ass': (deg2rad(val1), val2, val3),\
             'aas': (deg2rad(val1), deg2rad(val2), val3),\
             'saa': (val1, deg2rad(val2), deg2rad(val3))
             }
        val1, val2, val3 = deg_dict[tri_type]

    ##### BEGIN MAIN #####
    # we replace conditional branches with a dictionary
    # this dictionary selects which function to invoke,
    # given the triangle type
    func_dict =\
        {'sss': solve_sss, 'aaa': solve_aaa, 'asa': solve_asa,\
         'sas': solve_sas, 'ssa': solve_ssa, 'ass': solve_ass,\
         'aas': solve_aas, 'saa': solve_saa}

    solution_tuple = func_dict[tri_type](val1, val2, val3)
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
    if dec_digs is None:
        return solution_tuple

    # in this return statement, we render a new tuple from converted values
    # in solution_tuple. note that we preserve the order of the values.
    return round(solution_tuple[0], dec_digs), round(solution_tuple[1], dec_digs),\
           round(solution_tuple[2], dec_digs), round(solution_tuple[3], dec_digs),\
           round(solution_tuple[4], dec_digs), round(solution_tuple[5], dec_digs)
