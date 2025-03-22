''' module of functions we're developing in class.
'''

def get_percent_gc_content(nucl_str: str) -> float:
    '''(str) -> float # type contract
       Returns the percent gc content of nucleotide string input.
       ### example ###
       >>>get_percent_gc_content('gattacagattaca')
       28.571428571428573

    '''
    # garbage filter
    assert isinstance(nucl_str, str), 'input must be a clean nucleotide string'
    # initialization
    nucl_str = nucl_str.upper()
    # implementation of the algorithm
    return 100 * (nucl_str.count('G') + nucl_str.count('C')) / len(nucl_str)

def euclid_gcd(nat_a: int, nat_b: int) -> int:
    ''' Given two natural numbers greater than zero,
        return their greatest common divisor.
        FYI: two natural numbers are relatively prime
             when the return value is 1.
        >>>euclid_gcd(53667, 25527)
        201
    '''
    ##### garbage filters
    assert isinstance(nat_a, int) and isinstance(nat_b, int),\
            'arguments must be integers greater than zero'
    assert (nat_a > 0) and (nat_b > 0),\
            'arguments must be integers greater than zero'
    ##### implementation of algorithm
    while nat_b:
        nat_a, nat_b = nat_b, nat_a % nat_b
    return nat_a
