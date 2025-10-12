''' rev_compl dev file
'''

def rev_compl(nucl_str: str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>rev_compl('gattaca')
        'tgtaatc'
    '''
    # assert that the argument is a string
    assert isinstance(nucl_str, str),\
        "Input must be a clean nucleotide string."
    # ensure that the symbols in the nucleotide string are nucleotides.

    # initialization
    compl_dict, output_str =\
            {'a':'t', 'c':'g', 'g':'c', 't':'a'}, ''
    # implementation of algorithm
    for nucleotide in nucl_str:
        output_str = compl_dict[nucleotide] + output_str
    return output_str
