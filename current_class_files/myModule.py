# coding: utf-8

def ensureNuclStrClean(nuclStr: str):
    # garbage filter, ensure input is a string
    assert isinstance(nuclStr, str), "input must be a clean nucleotide string"
    
    # implementation of the algorithm
    bad_values = {}
    for index, value in enumerate(nuclStr):
        if value not in 'acgtACGT':
            bad_values[index] = value
    assert not bad_values, f"below is a dictionary of non-nucleotides in the input string, and their index positions in the string:\n{bad_values}"

def euclid_gcd(natA: int, natB: int) -> int:
    ''' Returns the greatest common divisor of two natural numbers.
        >>>euclid_gcd(53667, 25527)
        201
    '''
    # garbage filter
    assert isinstance(natA, int) and isinstance(natB, int)\
                  and (natA > 0) and (natB > 0),\
           "arguments must be natural numbers greater than zero."

    # implementation of algorithm
    while natB:
        natA, natB = natB, natA % natB

    return natA
    
def rev_compl(nuclStr: str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>rev_compl('gattaca')
        'tgaatc'
    '''
    # garbage filters
    assert isinstance(nuclStr, str), "the argument must be a clean nucleotide string."
    
    # ensure only nucleotides are in nuclStr
    # if non-nucleotide symbols are in string,
    # return dictionary of index/non-nucleotide pairs in string.
    from myModule import ensureNuclStrClean
    ensureNuclStrClean(nuclStr)
    
    # implementation of the algorithm
    outputStr, complDict = '', {'a':'t', 'c':'g', 'g':'c', 't':'a'}
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    
    return outputStr
