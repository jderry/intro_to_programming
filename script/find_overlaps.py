with open('exon.bed', 'r') as inFile:
    LoS = inFile.read().splitlines()
    LoL = []
    for record in LoS:
        LoL.append(record.split())
exonLoL = LoL
with open('test.sort.bed', 'r') as inFile:
    LoS = inFile.read().splitlines()
    LoL = []
    for record in LoS:
        LoL.append(record.split())
testLoL = LoL

outLoL = []
for testRec in testLoL:
    for exonRec in exonLoL:
        if testRec[0] == exonRec[0]\
        and len(testRec) > 3\
        and range(max(int(testRec[1]), int(exonRec[1])),\
                  min(int(testRec[2]), int(exonRec[2]))+1):
                outLoL.append([testRec[0],\
                str(max(int(testRec[1]), int(exonRec[1]))),\
                str(min(int(testRec[2]), int(exonRec[2]))+1)])
with open('matches', 'w') as outFile:
    for record in outLoL:
        outFile.write('\t'.join(record) + '\n')
        
        
