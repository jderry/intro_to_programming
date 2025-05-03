import os
home = os.path.expanduser('~')
# if directory does not exist, create it           
from pathlib import Path
Path(home + '/pickle').mkdir(parents=True, exist_ok=True)
from pickle import dump

with open(home + '/datafile/codon_amino_tabs.txt') as inFile:
    LoS = inFile.read().splitlines()
    codon2amino = {}
    for line in LoS:
        codon, amino = line.split()
        codon, amino = codon.strip(), amino.strip()
        codon2amino[codon] = amino
        
with open(home + '/pickle/codon_amino_dict.bin', 'wb') as outFile:
    dump(codon2amino, outFile)
