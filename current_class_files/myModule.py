''' the functions that we develop in this class.
'''

def getPerGCContent(nuclStr:str) -> float:
    ''' Returns the percent GC content of a nucleotide string.
        >>>getPerGCContent('GATTACA')
        28.571428571428573
    '''
    return 100*(nuclStr.count('G')+nuclStr.count('C'))/len(nuclStr)

def revCompl(nuclStr:str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>revCompl('gattaca')
        'tgtaatc'
    '''
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
   while natB:
      natA, natB = natB, natA % natB
   return natA
