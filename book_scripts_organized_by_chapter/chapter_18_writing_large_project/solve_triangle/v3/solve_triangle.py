''' solve_triangle. we put the function into its own module.
    v2, we use a string to ID the known parts of the triangle,
    and we remove the round bool and instead test dec_digs.
'''
# initialization
from math import degrees, radians, sin
from solve_triangle_sbr import \
    solve_sss, solve_aaa, solve_asa, solve_sas, solve_ssa, solve_ass, solve_aas, solve_saa

def solve_triangle(tri_type: str, \
                   val1: (int, float),\
                   val2: (int, float),\
                   val3: (int, float),\
                   deg=True,\
                   dec_digs=None) -> tuple:
    '''(str, pos real, pos real, pos real, bool, int) -> tuple, 
           where "pos real" means positive real; i.e., positive int or float
       Uses all built-in libraries.
       Given 3 parts of a triangle, return values for all sides and angles.
       Angles can be either all in degrees or all in radians. The default is degrees.
       Return tuple follows this ordering:
       (side1, side2, side3, angle1, angle2, angle3)
       Examples:
       >>>solve_triangle(side1=7, side2=5, angle3=49, rnd=True, decDigs=2)
       (7, 5, 5.3, 85.59, 45.41, 49.0) # angles in degrees, rounding to 2 decimal digits
       SSA and ASS triangles have 3 possible outcomes: NO SOLUTION, 1 solution, or 2 solutions.
       In the event of no solution, the function throws an assertion error.
       In the event of two solutions, the function returns tuples within the return tuple
       for values that have two solutions.
       Example:
       >>>solve_triangle('ssa', 22, 32, 32, dec_digs=4)
       (22, 32, (41.1535, 13.1216), 32.0, (50.425, 129.575), (97.575, 18.425))
       The first and second solutions are ordered. Hence:
       solution 1: (22, 32, 41.1535, 32.0, 50.425, 97.575)
       solution 2: (22, 32, 13.1216, 32.0, 129.575, 18.425)
    '''

    # ensure tri_type string passed into argument list is lowercase.
    tri_type = tri_type.lower()

    # begin garbage filter

    # assert that the sides and angles are positive reals.
    assert (isinstance(val1, (int, float)) and val1 > 0) and \
           (isinstance(val2, (int, float)) and val2 > 0) and \
           (isinstance(val3, (int, float)) and val3 > 0),\
           "triangle sides and angles must be positive reals"
    # assert that degrees is a bool.
    assert isinstance(deg, bool),\
        "the degrees argument must be either True or False"
    # assert that dec_digs value, if not None, is a natural number.
    if dec_digs is not None:
        assert isinstance(dec_digs, int) and dec_digs >= 0,\
        "the dec_digs argument must be a natural number, 0 or greater"
    # test if ASS or SSA triangle has no solution
    if (tri_type == 'ass') and sin(val1) > val3/val2:
        raise AssertionError('there is no solution for this angle-side-side')
    if (tri_type == 'ssa') and sin(val3) > val2/val1:
        raise AssertionError('there is no solution for this side-side-angle')
    # end garbage filter


    # we replace conditional branches with a dictionary
    # this dictionary updates values, if degrees (the default)
    # and not radians are specified
    if deg:
        deg_dict =\
            {'sss': (val1, val2, val3),\
             'aaa': (radians(val1), radians(val2), radians(val3)),\
             'asa': (radians(val1), val2, radians(val3)),\
             'sas': (val1, radians(val2), val3),\
             'ssa': (val1, val2, radians(val3)),\
             'ass': (radians(val1), val2, val3),\
             'aas': (radians(val1), radians(val2), val3),\
             'saa': (val1, radians(val2), radians(val3))
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

    has_embedded_tuple = False
    if tri_type in ('ass', 'ssa'):
        solution_list = list(solution_tuple)
        for index, value in enumerate(solution_list):
            if isinstance(value, tuple):
                has_embedded_tuple = True
                if index in (3, 4, 5):
                    temp_list = list(value)
                    for list_idx, list_value in enumerate(temp_list):
                        temp_list[list_idx] = degrees(list_value)
                    solution_list[index] = tuple(temp_list)
            else:
                if not isinstance(solution_list[index], tuple)\
                   and (index in (3, 4, 5)):
                    solution_list[index] = degrees(solution_list[index])
        solution_tuple = tuple(solution_list)

    # convert radians to degrees
    if deg and not has_embedded_tuple:
        # convert immutable tuple to mutable list
        solution_list = list(solution_tuple)
        # convert the angular values
        solution_list[3], solution_list[4], solution_list[5] =\
            degrees(solution_list[3]),\
            degrees(solution_list[4]),\
            degrees(solution_list[5])
        # coerce the list back into a tuple
        solution_tuple = tuple(solution_list)

    # return a tuple, with and without rounding
    if dec_digs is None:
        return solution_tuple

    # in this return statement, we render a new tuple from converted values
    # in solution_tuple. note that we preserve the order of the values.
    if not has_embedded_tuple:
        return round(solution_tuple[0], dec_digs), round(solution_tuple[1], dec_digs),\
               round(solution_tuple[2], dec_digs), round(solution_tuple[3], dec_digs),\
               round(solution_tuple[4], dec_digs), round(solution_tuple[5], dec_digs)

    # has embedded tuple. round values in embedded tuples,
    # and other values in solution_tuple
    solution_list = list(solution_tuple)
    for index, value in enumerate(solution_list):
        if isinstance(value, tuple):
            temp_list = list(value)
            for list_idx, list_value in enumerate(temp_list):
                temp_list[list_idx] = round(list_value, dec_digs)
            solution_list[index] = tuple(temp_list)
        else:
            solution_list[index] = round(solution_list[index], dec_digs)
    solution_tuple = tuple(solution_list)
    return solution_tuple
