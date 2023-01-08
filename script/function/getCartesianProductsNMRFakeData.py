def getCombinatoricLoTFrom(file):
    '''(str) -> list
       Given a path to a csv file, create and partition matrix into submatrix and column vector,
       and generate Cartesian products from elements of submatrix, and output a list of
       tuples of products, column vector elements.
    '''
    import numpy as np
    import itertools
    
    M = np.loadtxt(file, delimiter=',', dtype=str)
    Mpart = M[1:,:-1] # submatrix
    z = M[1:, -1]     # column vector
    #generate combinatoric tuple of tuples
    possibilities = tuple(itertools.product(*Mpart))
    # ^^^ the star operator prepended to a variable name instructs the interpreter
    # to unpack all of its elements into the argument list.
    # this allows Mpart to be of arbitrary size.
    desiredOutput = []
    for record in possibilities:
        recordList = []
        for index in range(len(record)):
            recordList.append((record[index], z[index]))
        desiredOutput.append(recordList)
    return desiredOutput

