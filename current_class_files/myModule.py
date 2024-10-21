''' module used in class.
'''

def get_percent_gc_content(nuclStr: str) -> float:
    ''' Given a nucleotide string as input,
        return its percent g-c content as a float.

        >>>get_percent_gc_content('gattaca')
        28.571428571428573
    '''
    assert isinstance(nuclStr, str), "argument must be a clean nucleotide string."
    badValues = {}
    for index, letter in enumerate(nuclStr):
        if letter not in 'actgACTG':
            badValues[index] = letter
    assert not badValues, f"nucleotide string at these positions has bad values\n{badValues}"
    # implementation of algorithm
    nuclStr = nuclStr.lower()
    return 100 * (nuclStr.count('c') + nuclStr.count('g')) / len(nuclStr)

def euclid_gcd(nat_a: int, nat_b: int) -> int:
    ''' Given two natural numbers,
        return their greatest common divisor.

        >>>euclid_gcd(53667, 25527)
        201
    '''
    assert isinstance(nat_a, int) and nat_a > 0\
       and isinstance(nat_b, int) and nat_b > 0,\
       "input must be two integers greater than zero."
    # implementation of algorithm
    while nat_b:
        nat_a, nat_b = nat_b, nat_a % nat_b
    
    return nat_a

def rev_compl(nuclStr: str) -> str:
    ''' Given a clean nucleotide string as input,
        return its reverse complement.

        >>>rev_compl('gattaca')
        'tgtaatc'
    '''
    assert isinstance(nuclStr, str),\
           "input must be a clean nucleotide string."
    badValues = {}
    for index, letter in enumerate(nuclStr):
        if letter not in 'ACGTacgt':
            badValues[index] = value
    assert not badValues, f"nucleotide string at these positions has bad values\n{badValues}"
    # implementation of algorithm
    complDict, outputStr = {'a':'t', 'A':'T', 'c':'g', 'C':'G', 'g':'c', 'G':'C', 't':'a', 'T':'A'}, ''
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    
    return outputStr
