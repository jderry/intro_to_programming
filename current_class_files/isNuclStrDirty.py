# this function ensures that a nucleotide string is clean
# by testing if each symbol in the string is a nucleotide.
# if not, the symbol and its position in the string
# added to a dictionary called 'bad values'
def isNuclStrDirty(nuclStr: str) -> dict:
    # initialization
    badValues = {}
    for idx, symbol in enumerate(nuclStr):
        if symbol not in 'ACGTacgt':
            badValues[idx] = symbol
    return badValues

# here we develop how to make the function
# part of an assert statement
nuclStr = 'gaftaxa'
badValues = isNuclStrDirty(nuclStr)

# "assert that the nucleotide string is clean"
assert not isNuclStrDirty(nuclStr),\
("nucleotide string has bad index/value pairs here:\n\t\t"
 f"{badValues}")
