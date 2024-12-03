def get_symbol_count(someStr: str) -> dict:
    ''' Given an arbitrary string as input,
        return a dictionary of symbol:count items,
        in which the symbols come from the string.
    '''
    assert isinstance(someStr, str),\
        "input must be a string."
    symbolDict = {} # initialization
    for symbol in someStr:
        try:
            symbolDict[symbol] += 1 # increment symbol count
        except KeyError:
            # KeyError means key is not yet in dictionary,
            # so add key:value pair to dictionary.
            symbolDict[symbol] = 1

    return symbolDict


