
def insertion_sort(arry):
    for j in range(len(arry)):
        k = j
        while k and arry[k-1] > arry[k]:
            arry[k-1], arry[k] = arry[k], arry[k-1]
            k -= 1
    return arry

def euclid_gcd(natA, natB):
    # garbage filter, ensuring expected input
    assert (isinstance(natA, int) and natA >= 1), "Both arguments must be natural numbers."
    assert (isinstance(natB, int) and natB >= 1), "Both arguments must be natural numbers."
    # rumpelstiltskin lines: euclid's gcd algorithm
    while natB:
        natA, natB = natB, natA % natB
    return natA

def getRevCompl(nuclStr):
    # garbage filter, ensuring expected input
    badStr, bad_nucleotides = False, dict()
    for index in range(len(nuclStr)):
        if nuclStr[index] not in 'acgt':
            badStr = True
            bad_nucleotides[index] = nuclStr[index]
    if badStr:
        assert badStr == False, f"Input nucleotide string must be clean.\nBad values listed below in index:value pairs:\n{bad_nucleotides}"
    complDict = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
    revComplStr = ''
    for nucleotide in nuclStr:
        revComplStr = complDict[nucleotide] + revComplStr
    return revComplStr

def getCompl(nucleotide):
    if nucleotide == 'a':
        complement = 't'
    elif nucleotide == 'c':
        complement = 'g'
    elif nucleotide == 'g':
        complement = 'c'
    elif nucleotide == 't':
        complement = 'a'
    else:
        pass
    return complement

def getRevCompl_if(nuclStr, getCompl=getCompl):
    revComplStr = ''
    for nucleotide in nuclStr:
        revComplStr = getCompl(nucleotide) + revComplStr
    return revComplStr

