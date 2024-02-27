''' functions created in class
'''
def isNuclStrClean(nuclStr: str) -> bool|dict:
    ''' Given a nucleotide string as input,
        return bool True if clean;
        otherwise, returns a dictionary of index/value pairs
        showing where in string there's a non-nucleotide,
        as well as the symbol in that position.
    '''
    badValues = {}
    for index, value in enumerate(nuclStr):
        if value not in 'ACGTacgt':
            badValues[index] = value
    if badValues:
        return badValues
    else:
        return True

def get_revcompl(nuclStr: str) -> str:
    ''' Given a nucleotide string as input,
        return its reverse complement.
        If nucleotide string is not clean,
        return a dictionary of index/value pairs
        showing where in string there's a non-nucleotide,
        as well as the symbol in that position.
    '''
    from myModule import isNuclStrClean
    isClean = isNuclStrClean(nuclStr)
    assert isinstance(isClean, bool), f"input string has non-nucleotide symbols at these index positions:\n\t\t{isClean}"
    # revcompl algorithm implemented
    complDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    outputStr = ''
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    return outputStr

def testFunc(testArg:str) -> str:
    if not isinstance(testArg, str):
        print('please enter string as input')
        return
    return testArg

def euclid_gcd(natA: int, natB: int) -> int:
    ''' Given two natural numbers as input, returns their greatest common divisor.
        >>> euclid_gcd(53667, 25527)
        201
    '''
    assert isinstance(natA, int) and (natA > 0), "natA must be a natural number greater than 0"
    assert isinstance(natB, int) and (natB > 0), "natB must be a natural number greater than 0" 
    while natB: # while natB is NOT zero
        natA, natB = natB, natA % natB
    return natA

