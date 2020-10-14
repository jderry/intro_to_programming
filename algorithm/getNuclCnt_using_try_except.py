def getNuclCnt(nuclStr):
    cntDict = {}
    for nucleotide in nuclStr:
        try:
            cntDict[nucleotide] += 1
        except KeyError:
            cntDict[nucleotide] = 1

