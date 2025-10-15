# read the contents of datafile into a list-of-strings
with open('datafile/reformatted_Unigene.fa') as inFile:
    LoS = inFile.read().splitlines()
# create the list-of-lists
LoL = []
for record in LoS:
    LoL.append(record.split())
# algorithm to smallest and largest
# nucleotide string lengths in the recordset
# first, create and initialize minLen, maxLen
minLen, maxLen = float('inf'), float('-inf')
# for loop goes through the recordset
# one record at a time
for record in LoL: # for current record
    strLength = len(record[-1]) # get string length
    if strLength < minLen: # compare to value in minLen
        minLen = strLength
    if strLength > maxLen: # compare to value in maxLen
        maxLen = strLength

