with open('datafile/reformatted_Unigene.fa') as inFile:
    LoS = inFile.read().splitlines() # method chaining
    LoL = [] # initialization
    for record in LoS:
        LoL.append(record.split())
        
def min_max_cond(LoL):
    minLen, maxLen = float('inf'), float('-inf')
    for record in LoL:
        if len(record[6]) > maxLen:
            maxLen = len(record[6])
        if len(record[6]) < minLen:
            minLen = len(record[6])
    for record in LoL:
        if len(record[6]) > maxLen:
            maxLen = len(record[6])
        if len(record[6]) < minLen:
            minLen = len(record[6])
    return minLen, maxLen
    
def min_max_builtins(LoL):
    minVal, maxVal = float('inf'), float('-inf')
    for record in LoL:
        minVal = min(minVal, len(record[6]))
        maxVal = min(maxVal, len(record[6]))
    return minVal, maxVal
    
%timeit min_max_cond(LoL)
%timeit min_max_builtins(LoL)

