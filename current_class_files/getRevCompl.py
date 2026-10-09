def getRevCompl(nuclStr: str) -> str:
    # garbage filter
    # initialization
    outputStr = ''
    complDict = {'a': 't', 'c':'g', 'g':'c', 't':'a', 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    # implentation of the algorithm
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
    return outputStr
