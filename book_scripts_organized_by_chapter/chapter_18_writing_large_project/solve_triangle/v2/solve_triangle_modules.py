# coding: utf-8
''' the subroutines of the solve_triangle module.
'''
from numpy import pi, sin, cos, arcsin, arccos

def solve_sss(side1, side2, side3) -> tuple:
    '''SSS
       we solve using the Law of Cosines.
       cos(C) =  a^2 + b^2 − c^2 / 2 * a * b
    '''

    # calculate angles
    angle1 = arccos((side2**2 + side3**2 - side1**2)/(2 * side2 * side3))
    angle2 = arccos((side1**2 + side3**2 - side2**2)/(2 * side1 * side3))
    angle3 = arccos((side1**2 + side2**2 - side3**2)/(2 * side1 * side2))

    return side1, side2, side3, angle1, angle2, angle3

def solve_aaa(angle1, angle2, angle3) -> tuple:
    '''AAA
       we solve using the Law of Sines.
       Because there are an infinite number
       of SSS solutions (complementary triangles),
       we normalize the result
       by setting the smallest side to 1.
    '''

    # calculate sines
    sin1, sin2, sin3 = sin(angle1), sin(angle2),\
                       sin(angle3)

    max_sin = max(sin1, sin2, sin3)
    if max_sin == sin1:
        side1 = 1 / max_sin
        side2 = side1 * sin2 / max_sin
        side3 = side1 * sin3 / max_sin
    elif max_sin == sin2:
        side2 = 1 / max_sin
        side1 = side2 * sin1 / max_sin
        side3 = side2 * sin3 / max_sin
    elif max_sin == sin3:
        side3 = 1 / max_sin
        side1 = side3 * sin1 / max_sin
        side2 = side3 * sin2 / max_sin
    else:
        pass

    # normalize values by setting smallest side to 1
    min_side = min(side1, side2, side3)
    side1, side2, side3 = side1/min_side, side2/min_side, side3/min_side

    return side1, side2, side3, angle1, angle2, angle3

def solve_asa(angle1, side3, angle2) -> tuple:
    '''ASA
       We can solve for 3d angle with: 180 - (ang1 + ang2).
       We can solve for missing sides using Law of Sines.
    '''

    # get missing angle
    angle3 = pi - (angle1 + angle2)

    # calculate missing sides
    side1, side2 = sin(angle1) * side3 / sin(angle3), sin(angle2) * side3 / sin(angle3)

    return side1, side2, side3, angle1, angle2, angle3

def solve_sas(side1, angle3, side2) -> tuple:
    '''SAS
       Given 2 sides, we can solve for the 3d using:
       a2 = b2 + c2 − 2bc cosA
       Given 3 sides, we can solve for the missing angles using
       the same formula, rearranged.
    '''

    # a2 = b2 + c2 − 2bc cosA
    side3 = (side1**2 + side2**2 - (2 * side1 * side2 * cos(angle3)))**(1/2)

    # calculate angles
    angle1 = arccos((side2**2 + side3**2 - side1**2)/(2 * side2 * side3))
    angle2 = arccos((side1**2 + side3**2 - side2**2)/(2 * side1 * side3))

    return side1, side2, side3, angle1, angle2, angle3

def solve_ssa(side1, side2, angle1) -> tuple:
    '''SSA
       We use the Law of Sines to solve for the 2d angle.
    '''

    # Law of Sines
    # a2 = b2 + c2 − 2bc cosA
    angle2 = arcsin(side2 * sin(angle1) / side1)
    angle3 = pi - (angle1 + angle2)
    side3 = (side1**2 + side2**2 - (2 * side1 * side2 * cos(angle3)))**(1/2)

    return side1, side2, side3, angle1, angle2, angle3

def solve_ass(angle1, side3, side1) -> tuple:
    '''ASS
       We use the Law of Sines to solve for the 2d angle.
    '''

    # Law of Sines
    # a2 = b2 + c2 − 2bc cosA
    angle3 = arcsin(side3 * sin(angle1) / side1)
    angle2 = pi - (angle1 + angle3)
    side2 = (side1**2 + side3**2 - (2 * side1 * side3 * cos(angle2)))**(1/2)

    return side1, side2, side3, angle1, angle2, angle3

def solve_aas(angle1, angle2, side1) -> tuple:

    '''AAS
       Given 2 angles, we use 180 - (angA + angB) to find the 3d.
       Then we use the Law of Sines to find the missing sides.
    '''

    angle3 = pi - (angle1 + angle2)
    sin1, sin2, sin3 = sin(angle1), sin(angle2), sin(angle3)
    side2 = side1 * sin2 / sin1
    side3 = side1 * sin3 / sin1

    return side1, side2, side3, angle1, angle2, angle3

def solve_saa(side1, angle3, angle1) -> tuple:

    '''SAA
       Given 2 angles, we use 180 - (angA + angB) to find the 3d.
       Then we use the Law of Sines to find the missing sides.
    '''
    angle2 = pi - (angle3 + angle1)
    sin1, sin2, sin3 = sin(angle1), sin(angle2), sin(angle3)
    side2 = side1 * sin2 / sin1
    side3 = side1 * sin3 / sin1

    return side1, side2, side3, angle1, angle2, angle3
