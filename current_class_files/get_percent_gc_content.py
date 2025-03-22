''' gc content development file
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
