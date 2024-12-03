''' dummy docstring for now
'''

def ensure_nucl_str_clean(nucl_str: str) -> dict:
    ''' Given a nucleotide string as input,
        return a dictionary of index:value pairs
        of bad values in string.
        If nucleotide string is clean,
        returns an empty dictionary.
    '''
    # garbage filter
    assert isinstance(nucl_str, str),\
           "input must be a nucleotide string."

    # implementation of algorithm
    bad_values = {} # initialization
    for index, letter in enumerate(nucl_str):
        if letter not in 'actgACTG':
            bad_values[index] = letter

    return bad_values
