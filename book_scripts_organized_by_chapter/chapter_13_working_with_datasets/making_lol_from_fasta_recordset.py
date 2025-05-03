with open('datafile/reformatted_Unigene.fa') as inFile:
    LoS = inFile.read().splitlines() # method chaining
    LoL = [] # initialization
    for record in LoS:
        LoL.append(record.split())

