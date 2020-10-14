getMinMaxValues(LoL):
    minLen, maxLen = float('inf'), float('-inf')
    for record in LoL:
        if len(record[-1]) < minLen:
            minLen = len(record[-1])
        if len(record[-]) > maxLen:
            maxLen = len(record[-1])
    return (minLen, maxLen)
