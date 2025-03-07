def getGCcontent(nuclStr: str) -> float:
    return (nuclStr.count('G') + nuclStr.count('C')) / len(nuclStr)
