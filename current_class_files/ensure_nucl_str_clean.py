''' ensure_nucl_str_clean dev file
'''

def ensure_nucl_str_clean(nucl_str: str) -> dict:
    ''' Returns an empty dict if nucleotide string is clean, 
        if dirty returns index:value pairs of non-nucleotides in string.
        Examples
    '''
    # garbage filter
    assert isinstance(nucl_str, str), "Input must be a nucleotide string."
    # initialization
    bad_values = {}
    # implementation of algorithm
    for index, symbol in enumerate(nucl_str):
        if symbol not in 'acgtACGT':
            bad_values[index] = symbol
    return bad_values
