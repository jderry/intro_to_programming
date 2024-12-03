def revCompl_if(nuclStr):
    outputStr = ''
    for nucleotide in nuclStr:
        outputStr = getComplement(nucleotide) + outputStr

complDict = {'a':'t', 'c':'g', 'g':'c', 't':'a'}

def revCompl_dict(nuclStr, complDict):
    outputStr = ''
    for nucleotide in nuclStr:
        outputStr = complDict[nucleotide] + outputStr
%timeit revCompl_if('gattaca')
%timeit revCompl_dict('gattaca', complDict)
