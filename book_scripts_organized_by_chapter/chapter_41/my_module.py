def get_percent_gc_content(nuclStr: str) -> float:
    ''' Given a nucleotide string as input,
        return its percent g-c content as a float.
        >>>get_percent_gc_content('gattaca')
        28.571428571428573
    '''
    # garbage filters
    # assert that argument must be a string
    assert isinstance(nuclStr, str), "argument must be a clean nucleotide string."
    # assert that symbols in strings must be nucleotides
    # implementation of algorithm
    nuclStr = nuclStr.lower() # initialization
    # sum the values of the numerator BEFORE dividing by the denominator
    return 100 * (nuclStr.count('c') + nuclStr.count('g')) / len(nuclStr)
    
    
