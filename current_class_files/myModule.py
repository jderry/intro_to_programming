def euclidGCD(natA: int, natB: int) -> int:
    '''Returns the greatest common divisor of two natural numbers.
       Example:
       >>>euclidGCD(53667, 25527)
       201
    '''
    # garbage filters (make sure that input is expected input)
    assert (isinstance(natA, int) and natA > 0)\
       and (isinstance(natB, int) and natB > 0),\
       "Input must be natural numbers."
    # initialization
    # implemenation of algorithm into python (pseudocode)
    while natB:
        natA, natB = natB, natA % natB
    return natA
