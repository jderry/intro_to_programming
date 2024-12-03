def make_dict_from_records(folder: str) -> dict:
    ''' Given path to folder holding 1 record/file,
        make a DoD from the files' contents.
    '''
    import os
    fileList = os.listdir(folder)
    # outer dictionary of DoD
    resultDict = {} # initialization
    for file in fileList:
        # full file path
        filepath = folder + file
        # inner dictionary of DoD
        contentsDict = {}
        with open(filepath) as inFile:
            LoS = inFile.read().splitlines()
            for line in LoS:
                # handle label but no value
                try:
                    # split only along 1st tab in line
                    label, value = line.split("\t", 1)
                except ValueError:
                    continue
                contentsDict[label] = value
        # add the inner dictionary to the outer one
        resultsDict[file] = contentsDict
    return resultsDict

