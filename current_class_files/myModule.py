''' the functions that we develop in this class.
'''

def getPerGCContent(nuclStr:str) -> float:
    ''' Returns the percent GC content of a nucleotide string.
        >>>getPerGCContent('GATTACA')
        28.571428571428573
    '''
    # garbage filter
    return 100*(nuclStr.count('G')+nuclStr.count('C'))/len(nuclStr)

def revCompl(nuclStr:str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>revCompl('gattaca')
        'tgtaatc'
    '''
    # garbage filter
    complDict = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
    outputStr = ''
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    return outputStr

def euclidGCD(natA:int, natB:int) -> int:
    ''' Given two natural numbers, returns their greatest common divisor.
        >>>euclidGCD(53667, 25527)
        201
    '''
    # garbage filter
    while natB:
        natA, natB = natB, natA % natB
    return natA

def char_count(someStr: str) -> dict:
    ''' Given a string, return a dictionary of char:count pairs
        >>>char_count('gattaca')
        {'g': 1, 'a': 3, 't': 2, 'c': 1} 
    '''
    # garbage filter
    # initialization
    char_cnt_dict = {}

    for char in someStr:
        try:
            char_cnt_dict[char] += 1
        except KeyError:
            char_cnt_dict[char] = 1
    return char_cnt_dict

def str2num(someStr: str) -> (int, float, str):
    ''' Given a numeric string, return an int or float.
        If the string is non-numeric, it is returned.
        >>>str2num('12')
        12
        >>>str2num('0.12')
        0.12
    '''
    # garbage filter
    try:
        outputVal = float(someStr)

        if outputVal.is_integer():
            outputVal = int(someStr)
    except ValueError:
        outputVal = someStr
    return outputVal

def get_min_max(someArray:(list, tuple)) -> tuple:
    ''' Given a list or tuple of items that can be logically compared,
        return the list's or tuple's smallest and greatest items in a tuple.
        >>>get_min_max([4, 5, 3])
        (3, 5)
    '''
    # garbage filter
    # initialization
    maxVal, minVal = float('-inf'), float('inf')
    for item in someArray:
        if item > maxVal:
            maxVal = item
        if item < minVal:
            minVal = item
    return minVal, maxVal
