import os
home = os.path.expanduser('~')

with open(home + '/datafile/hewitsoni_males.txt') as inFile:
    LoS = inFile.read().splitlines()
    LoL = [] # initialization
    for record in LoS:
        LoL.append(record.split())

# then create an edge list from the LoL
edge_list = []
for index, record in enumerate(LoL[:-1]):
    if LoL[index][0] == LoL[index+1][0]:
        edge = [LoL[index][0], LoL[index][1], LoL[index+1][1]]
        edge_list.append(edge)

# if directory does not exist, create it           
from pathlib import Path
Path(home + '/pickle').mkdir(parents=True, exist_ok=True)

# write pickle file into pickle directory
from pickle import dump
with open(home + '/pickle/edge_list.pickle.bin', 'wb') as outFile:
    dump(edge_list, outFile)
    
# unpickle contents of file into session memory
from pickle import load
with open(home + '/pickle/edge_list.pickle.bin', 'rb') as inFile:
    edge_list = load(inFile)
