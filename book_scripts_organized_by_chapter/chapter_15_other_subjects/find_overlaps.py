import os
home = os.path.expanduser('~')

with open(home + '/datafile/finding_interval_overlaps/exon.bed', 'r') as exonFile,\
     open(home + '/datafile/finding_interval_overlaps/test.sort.bed', 'r') as testFile:
    exonLoS, testLoS = exonFile.read().splitlines(),\
                       testFile.read().splitlines()
    exonLoL, testLoL = [], []
    for exonRec in exonLoS:
        exonLoL.append(exonRec.split('\t'))
    for testRec in testLoS:
        testLoL.append(testRec.split('\t'))
        

