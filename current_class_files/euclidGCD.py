def euclidGCD(natA: int, natB: int) -> int:
    '''Returns the greatest common divisor,
       given two natural numbers.
       >>> euclidGCD(53667, 25527)
       201
    '''
    # garbage filter
    assert (isinstance(natA, int) \
       and isinstance(natB, int)) \
       and (natA > 0 and natB > 0), \
       "Both numbers must be integers greater than zero."
    # implementation of the algorithm
    while natB:
        natA, natB = natB, natA % natB
    return natA

