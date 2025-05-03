import pickle
import os
def get_amino_acid(nuclStr: str, codon2amino: dict=None, path_to_pickled_dict: str=''):
    ''' Requires either codon2amino dict passed into function,
        or path to pickled codon2amino dict file passed into it.
        Returns tuple of amino-acid strings for three reading frames.
        >>>get_amino_acid('GATTACAGATTACA', codon2amino)
        ('AspTyrArgLeu', 'IleThrAspTyr', 'LeuGlnIleThr')
    '''
    # garbage filters
    # to do: garbage filter to ensure nuclStr is clean
    assert codon2amino or os.path.isfile(path_to_pickled_dict),\
        "function must have dict passed into it, or dict must exist to pickle dir"
    if not codon2amino and os.path.isfile(path_to_pickled_dict):
        with open(path_to_pickled_dict, 'rb') as inFile:
            codon2amino = pickle.load(inFile)
    # implementation of algorithm
    # assuming nuclStr is clean AND
    # dict may be incomplete or have bad items
    # initialization
    nuclStr = nuclStr.upper()
    rf0, rf1, rf2 = '', '', ''
    
    for index, value in enumerate(nuclStr[:-2]):
        remainder = index % 3
        codon = nuclStr[index:index+3]
        try:
            amino = codon2amino[codon]
        except KeyError as e:
            raise Exception(f"Codon {codon} not found in codon2amino dict.\n" \
                  f"\tPlease check dictionary for item and codon used as key.") \
                  from e
        if remainder == 0:
            rf0 = rf0 + amino
        elif remainder == 1:
            rf1 = rf1 + amino
        else:
            rf2 = rf2 + amino
    return rf0, rf1, rf2
