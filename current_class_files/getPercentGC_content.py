# development file for function

def getPercentCG_content(nuclStr: str) -> float:
    # garbage filter
    # initialization
    nuclStr = nuclStr.upper()
    # implentation of the algorithm
    return 100 * (nuclStr.count('C') + nuclStr.count('G')) / len(nuclStr)

