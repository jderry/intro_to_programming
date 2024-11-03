''' euclid_gcd development file.
'''

def euclid_gcd(natA: int, natB: int) -> int:
    ''' Given two natural numbers greater than zero,
        return their greatest common divisor.
        -------
        example
        -------
        >>>euclid_gcd(53667, 25527)
        201
    '''
    # garbage filter
    # ensure that ints are greater than zero.
    # we break the assert statement across multiple lines
    # to enhance readability of the compound logic statement.
    assert isinstance(natA, int) and (natA > 0)\
       and isinstance(natB, int) and (natB > 0),\
       "Both arguments must be ints greater than zero."

    # implementation of the algorithm
    while natB:
        natA, natB = natB, natA % natB

    return natA
