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

def rev_compl(nucl_str: str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>rev_compl('gattaca')
        'tgtaatc'
    '''
    # assert that the argument is a string
    assert isinstance(nucl_str, str),\
        "Input must be a clean nucleotide string."
    # ensure that the symbols in the nucleotide string are nucleotides.
    bad_values = ensure_nucl_str_clean(nucl_str)
    assert not bad_values, ("Non-nucleotides exist in the input string\n"
                            "\tin these index position:value pairs.\n"
                            f"\t{bad_values}")
    # initialization
    compl_dict, output_str =\
            {'a':'t', 'c':'g', 'g':'c', 't':'a'}, ''
    # implementation of algorithm
    for nucleotide in nucl_str:
        output_str = compl_dict[nucleotide] + output_str
    return output_str

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
