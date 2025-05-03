# first, we read the contents
# of the hewitsoni_males datafile
# into an LoL in session memory
with open('datafile/hewitsoni_males.txt') as inFile:
    LoS = inFile.read().splitlines()
    LoL = [] # initialization
    for record in LoS:
        LoL.append(record.split())

# then we write out an edge list from the LoL
with open('datafile/edge_list', 'w') as outFile:
    # we shorten the range object by 1
    # to prevent an IndexError
    for index in range(len(LoL)-1):
        if LoL[index][0] == LoL[index+1][0]:
            edge_record = (f"{LoL[index][0]}\t"
                           f"{LoL[index][1]}\t"
                           f"{LoL[index+1][1]}\n")
            outFile.write(edge_record)

