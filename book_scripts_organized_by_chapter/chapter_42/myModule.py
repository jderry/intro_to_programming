''' module used in class.
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

def get_percent_gc_content(nuclStr: str) -> float:
    ''' Given a nucleotide string as input,
        return its percent g-c content as a float.

        >>>get_percent_gc_content('gattaca')
        28.571428571428573
    '''
    assert isinstance(nuclStr, str), "argument must be a clean nucleotide string."
    from myModule import ensure_nucl_str_clean
    assert not ensure_nucl_str_clean(nuclStr), f"nucleotide string at these positions has bad values\n{badValues}"
    # implementation of algorithm
    nuclStr = nuclStr.lower()
    return 100 * (nuclStr.count('c') + nuclStr.count('g')) / len(nuclStr)

def euclid_gcd(natA: int, natB: int) -> int:
    ''' Given two natural numbers greater than zero,
        return their greatest common divisor.
        -------
        example
        -------
        >>>euclid_gcd(53667, 25527)
        201
    '''
    # garbage filter
    # ensure that ints are greater than zero.
    # we break the assert statement across multiple lines
    # to enhance readability of the compound logic statement.
    assert isinstance(natA, int) and (natA > 0)\
       and isinstance(natB, int) and (natB > 0),\
       "Both arguments must be ints greater than zero."

    # implementation of the algorithm
    while natB:
        natA, natB = natB, natA % natB

    return natA

def rev_compl(nuclStr: str) -> str:
    ''' Given a clean nucleotide string as input,
        return its reverse complement.

        >>>rev_compl('gattaca')
        'tgtaatc'
    '''
    assert isinstance(nuclStr, str),\
           "input must be a clean nucleotide string."
    from myModule import ensure_nucl_str_clean
    assert not ensure_nucl_str_clean(nuclStr), f"nucleotide string at these positions has bad values\n{badValues}"
    # implementation of algorithm
    complDict, outputStr = {'a':'t', 'A':'T', 'c':'g', 'C':'G', 'g':'c', 'G':'C', 't':'a', 'T':'A'}, ''
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    
    return outputStr

def get_symbol_count(someStr: str) -> dict:
    ''' Given an arbitrary string as input,
        return a dictionary of symbol:count items,
        in which the symbols come from the string.
    '''
    assert isinstance(someStr, str),\
        "input must be a string."
    symbolDict = {} # initialization
    for symbol in someStr:
        try:
            symbolDict[symbol] += 1 # increment symbol count
        except KeyError:
            # KeyError means key is not yet in dictionary,
            # so add key:value pair to dictionary.
            symbolDict[symbol] = 1

    return symbolDict

    
