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

with open(home + '/datafile/overlaps', 'w') as outFile:
    for testRec in testLoL:
        for exonRec in exonLoL:
            if testRec[0] == exonRec[0]\
                and len(testRec) > 3\
                and range(max(int(testRec[1]), int(exonRec[1])),\
                          min(int(testRec[2]), int(exonRec[2]))+1):
                overlap = range(max(int(testRec[1]), int(exonRec[1])),\
                          min(int(testRec[2]), int(exonRec[2]))+1)
                record = (f"{exonRec[0]}\t{overlap[0]}\t"
                          f"{overlap[-1]}\t{exonRec[3]}\t"
                          f"{testRec[3]}\n")
                outFile.write(record)
        
        
