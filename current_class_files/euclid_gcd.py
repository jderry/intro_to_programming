
def euclid_gcd(nat_A: int, natB: int) -> int:
    ''' Given two natural numbers greater than zero,
        return their greatest common divisor.
        FYI: two natural numbers are relatively prime
             when the return value is 1.
        >>>euclid_gcd(53667, 25527)
        201
    '''
    ##### garbage filters
    assert isinstance(nat_A, int) and isinstance(natB, int),\
            'arguments must be integers greater than zero'
    assert (nat_A > 0) and (natB > 0),\
            'arguments must be integers greater than zero'
    ##### implementation of algorithm
    while natB:
        nat_A, natB = natB, nat_A % natB
    return nat_A
