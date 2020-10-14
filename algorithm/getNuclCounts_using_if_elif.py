def getNuclCounts(nuclStr):
    aCnt, cCnt, gCnt, tCnt = 0, 0, 0, 0
    for nucleotide in nuclStr:
        if nucleotide == 'a':
            aCnt += 1
        elif nucleotide == 'c':
            cCnt += 1
        elif nucleotide == 'g':
            gCnt += 1
        elif nucleotide == 't':
            tCnt += 1
        else:
            pass
    return (aCnt, cCnt, gCnt, tCnt)

