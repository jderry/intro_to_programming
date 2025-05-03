''' chapter 42, Algorithm: Converting Positive Decimal Fractions Into Binary Fractions
'''

def dec_frac2bin_frac(dec_frac: float, num_bin_digits: int = 10) -> str:
    ''' Given a positive fractional float as input,
        returns its base-2 equivalent as a string.
        A second argument is the number of digits
        in the binary fraction. The default is 10
        digits.
        --------
        examples
        --------
        >>>dec_frac2bin_frac(.75)
        '0.1100000000'
        >>>dec_frac2bin_frac(.1, 20)
        '0.00011001100110011001'
    '''
    # garbage filters
    assert isinstance(dec_frac, float), \
        "dec_frac must be a positive fraction."
    # if dec_frac is a positive fraction,
    # the subtraction below yields zero.
    # we assert dec_frac must be a positive fraction
    # so we coerce that zero to a bool (False),
    # and negate it to True.
    # Other differences evaluate as False.
    assert not dec_frac - (dec_frac % 1), \
        "dec_frac must be a positive fraction."

    # implementation of algorithm
    # initialization
    running_sum, bin_frac = 0, '0.'

    # iterate through the positions of
    # the binary fraction. for each position,
    # calculate its base-10 value, then test
    # whether or not it contributes to the value
    # of the decimal fraction.
    for position in range(1, num_bin_digits+1):
        pos_value = 2**-(position)
        if (running_sum + pos_value) > dec_frac:
            # pos_value does NOT contribute
            # to decimal fraction
            bin_frac = bin_frac + '0'
        else:
            # pos_value contributes
            # to decimal fraction
            bin_frac = bin_frac + '1'
            # update running_sum
            running_sum = running_sum + pos_value

    return bin_frac
