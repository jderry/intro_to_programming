'''
'''
def get_min_max(array: list|tuple) -> tuple:
    '''Given an unordered array of numbers, 
       return the largest and smallest numbers in the array.
    '''
    # garbage filter goes here
    # implementation of the algorithm
    minVal, maxVal = float('inf'), float('-inf')
    for number in array:
        if number < minVal:
            minVal = number
        if number > maxVal:
            maxVal = number
    return minVal, maxVal

def read_records_from_tab_datafile(file: str) -> list:
    '''Given a string that is the filepath to a tabular datafile as input,
       return the contents of the datafile as a list-of-tuples as output.
    '''
    # garbage filter goes here
    # tests if file exists, tests if a text file
    with open(file, 'r') as inFile:
        LoS = inFile.read().splitlines()
        LoT = []
        for record in LoS:
            LoT.append(tuple(record.split()))
    return LoT

def get_min_max_rec(array: list|tuple) -> tuple:
    '''Given an unordered array of numbers, 
       return the largest and smallest numbers in the array.
    '''
    # garbage filter goes here
    # implementation of the algorithm
    minRec, maxRec = [], []
    minVal, maxVal = float('inf'), float('-inf')
    for index, number in enumerate(array):
        if number < minVal:
            minVal = number
            minRec = [index, minVal]
        if number > maxVal:
            maxVal = number
            maxRec = [index, maxVal]
    return minRec, maxRec

