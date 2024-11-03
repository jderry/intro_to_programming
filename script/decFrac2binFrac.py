# development file

def decFrac2binFrac(decFrac: float, numBinDigits: int = 10) -> str:
    '''
    '''
    # garbage filters
    assert isinstance(decFrac, float) \
       and isinstance(numBinDigits, int),\
       "decFrac must be a positive float and numBinDigits must be an int"

    assert not decFrac - (decFrac % 1), \
       "decFrac must be a positive decimal fraction"

    # implementation of algorithm
    running_sum, binFrac = 0, '0.'
    for position in range(1, numBinDigits+1):
        pos_value = 2**-(position)
        running_sum = running_sum + pos_value
        if running_sum > decFrac:
            binFrac = binFrac + '0'
            running_sum = running_sum - pos_value
        else:
            binFrac = binFrac + '1'

    return binFrac
