# coding: utf-8
'''GIVEN: in home directory, an inFolder & an outFolder.
   SPECIFICATION: unzip raw run files to the inFolder. 
   this script extracts the data from each datafile to create a DoD
   called 'runDict'; the keys are the filenames, and the values are the file contents.
   OUTPUT: in 'files/processed', a pickle of the runDict, and in outFolder a workbook, 
   each sheet containing the formatted data of each raw file.
'''


def initialize(constFilePath='/home/james/python/calla_mcculley/constants_file.txt'):
    '''set up constDict.
       need expr0 for calculations later.
    '''
    # get constants from file, put into constantsDict
    with open(constFilePath, 'r') as inFile:
        LoS = inFile.read().splitlines()
    constDict = dict()
    for line in LoS:
        key, value = line.split('\t')
        constDict[key] = value
    return constDict


def put_datafile_contents_into_runDict(constDict):
    ''' import contents of datafiles as values in runDict
    runDict keys are datafile names
    '''
    import os
    import re
    from dateutil.parser import parse

    def is_date(string):
        try: 
            parse(string)
            return True
        except ValueError:
            return False

    inFolder = constDict['inFolder']
    fileList = os.listdir(inFolder)

    runDict = dict()
    for file in fileList: # iterate over files in inFolder
        with open(inFolder + file, 'r') as inFile:
            LoS = inFile.read().splitlines()
            LoL, fileDict, noTableFlag = [], dict(), True
        for line in LoS: # for each line in a file
            if noTableFlag: # top of each file has a key, value pair
                lineList = line.split('\t')
                key = lineList.pop(0)
                fileDict[key] = lineList
            if not(noTableFlag): # bottom of each file has tabular data
                LoL.append(line.split('\t'))
            if re.match(r'^V', line):
                noTableFlag = False
        fileDict['table'] = LoL
        #modify filename
        if file[-4:] == '.txt': # if filename ends in '.txt', remove suffix
            file = file[:-4]
        fileList = file.split(' ')
        # build new file name
        newFile = fileList[0] # IDVD or IDVG
        for index in range(len(fileList)):
            if fileList[index][-1] == 'K': # concatenate temp
                newFile = newFile + ' ' + fileList[index]
            if fileList[index][:3] == 'dev': # concatenate dev
                newFile = newFile + ' ' + fileList[index]
            if is_date(' '.join(fileList[index].split('_')))\
               and fileList[index][-3] != '_': # concatenate date and time
                newFile = newFile + ' ' + fileList[index]\
                                  + ' ' + fileList[index+1][:-3]

        runDict[newFile] = fileDict
    return runDict


def process_items_in_runDict(runDict, constDict):
  ''' this is the largest function in the code base.
  '''
  import numpy as np
  import pandas as pd
  import pickle
  import copy


  outFolder = constDict['outFolder']

  for file, value in runDict.items():
    column_list = list(range(int(value['Measurement.Secondary.Start'][0]),\
                             int(value['Measurement.Secondary.Count'][0])\
                            *int(value['Measurement.Secondary.Step'][0]),\
                             int(value['Measurement.Secondary.Step'][0])))
    
    row_range = np.arange(int(value['Measurement.Primary.Start'][0]),\
                          int(value['Measurement.Primary.Stop'][0])\
                       +float(value['Measurement.Primary.Step'][0]),\
                        float(value['Measurement.Primary.Step'][0]))

  ##### make the Vd column, the first column in the output sheet
    Vd_col = [] 
    for Vd in row_range: 
        Vd_col.append(round(Vd,1)) 
    for Vd in row_range[::-1]: 
        Vd_col.append(round(Vd, 1)) 

  ##### make outputList, the first table of data in the output sheet
  ##### outputList also serves as the template for computed tables in output sheet  
    outputList, tableRow = [], 0 
    for column in column_list: 
        outputCol = [] 
        for Id in row_range: 
            outputCol.append(value['table'][tableRow][1]) 
            tableRow += 1 
        for Id in row_range[::-1]: 
            outputCol.append(value['table'][tableRow][1]) 
            tableRow += 1 
        outputList.append(outputCol) 


  ##### make copies of outputList, do computations on column vectors
    # first, make deep copy of outputList
    absOutputList = copy.deepcopy(outputList) # make copy of outputList
    # second, make the copy into an nd-array
    absOutputList = np.array(absOutputList) # make absOutputList into ndarray
    # third, do computation
    absOutputList = np.absolute(absOutputList.astype(float)) # get absolute value

    # make idrain_polyfit_matrix
    # make linmob_matrix
    if file.split()[0] == 'IDVG':
        # first, make deep copy of outputList, Vd_col
        idvg_outputList, Vd_col_ndarray =\
        copy.deepcopy(outputList), copy.deepcopy(Vd_col)
        # second, make the copies into nd-arrays, get row and column counts
        idvg_outputList, Vd_col_ndarray =\
        np.array(idvg_outputList).astype(float).T, np.array(Vd_col).astype(float).T
        idvg_row, idvg_col = idvg_outputList.shape # returns tuple of (row, col)
        Vd_col_row = Vd_col_ndarray.shape # returns tuple of (row, col)
        # third, do computation: 
        # a) make polyfit matrix
        linmob_matrix = []
        for col in range(idvg_col):
            for row in range(idvg_row-2):
                # use np.polyfit() of degree 1 to get slope of best-fit line,
                # polyfit()[0], and append slope to polyfit matrix
                linmob_matrix\
                .append(np.polyfit(Vd_col_ndarray[row:row+3],\
                idvg_outputList[row:row+3, col], 1)[0])
        # b) convert list into nd-array and reshape into matrix
        polyfit_matrix_row = int(len(linmob_matrix)/idvg_col)
        linmob_matrix = np.array(linmob_matrix)\
        .reshape((polyfit_matrix_row, idvg_col))
        idrain_polyfit_matrix = copy.deepcopy(linmob_matrix)
        # c) multiply matrix elements by constDict['expr0']
        linmob_matrix = constDict['expr0']\
                            * linmob_matrix
        # d) divide elements of each column by column header
        for index in range(len(column_list)):
            if column_list[index]:
                linmob_matrix[:, index] =\
                linmob_matrix[:, index]/column_list[index]
        # e) create 2 rows of nan's and append to bottom of matrix
        # make empty bottom two rows, vstack
        bottom_rows = np.full_like(np.arange(2*idvg_col, dtype=int), \
                                   np.nan, dtype=np.double)\
                                   .reshape(2, idvg_col)
        idrain_polyfit_matrix = np.vstack((idrain_polyfit_matrix, bottom_rows))
        linmob_matrix = np.vstack((linmob_matrix, bottom_rows))

    # make satmob_matrix
    if file.split()[0] == 'IDVG':
        # first, make deep copy of absOutputList
        satmob_outputList = copy.deepcopy(absOutputList)
        # second, make the copy into an nd-array of floats, take sqrt
        sqrtVd_outputList = np.sqrt(satmob_outputList.astype(float)).T
        satmob_outputList = np.sqrt(satmob_outputList.astype(float)).T
        # third, do computation
        sqrtAbs_polyfit_matrix = []
        for col in range(idvg_col):
            for row in range(idvg_row-2):
                # use np.polyfit() of degree 1 to get slope of best-fit line,
                # polyfit()[0], and append slope to sqrtAbs_polyfit matrix
                sqrtAbs_polyfit_matrix\
                .append(np.polyfit(Vd_col_ndarray[row:row+3],\
                satmob_outputList[row:row+3, col], 1)[0])
        sqrtAbs_polyfit_matrix_row = int(len(sqrtAbs_polyfit_matrix)/idvg_col)
        # convert list into nd-array and reshape into matrix
        sqrtVd_matrix = sqrtVd_outputList.reshape(idvg_row, idvg_col)
        sqrtAbs_polyfit_matrix = np.array(sqrtAbs_polyfit_matrix)\
        .reshape((sqrtAbs_polyfit_matrix_row, idvg_col))
        # make empty bottom two rows, vstack
        bottom_rows = np.full_like(np.arange(2*idvg_col, dtype=int), \
                                   np.nan, dtype=np.double)\
                                   .reshape(2, idvg_col)
        sqrtAbs_polyfit_matrix = np.vstack((sqrtAbs_polyfit_matrix, bottom_rows))
        # square the sqrtAbs_polyfit_matrix, multiply by 2 and expr0
        satmob_matrix = np.square(sqrtAbs_polyfit_matrix)\
                                                        * 2 * constDict['expr0']


    # first, make deep copy of outputList
    dummyOutputList = copy.deepcopy(outputList) # make copy of outputList
    # second, make the copy into an nd-array
    dummyOutputList = np.array(dummyOutputList) # make absOutputList into ndarray
    # third, do computation
    dummyOutputList = dummyOutputList.astype(float)\
                      * float(constDict['ESiO2'])# do dummy calculation


  ########## PREPARE COLUMNS AND TABLES FOR WRITING OUT
    # first, stringify the values in the matrices
    absOutputList = absOutputList.astype(str)
    if file.split()[0] == 'IDVG':
        idrain_polyfit_matrix.astype(str)
        linmob_matrix = linmob_matrix.astype(str)
        sqrtVd_matrix = sqrtVd_matrix.astype(str)
        sqrtAbs_polyfit_matrix  =  sqrtAbs_polyfit_matrix.astype(str)
        satmob_matrix = satmob_matrix.astype(str)
    dummyOutputList = dummyOutputList.astype(str)

  ##### label Vd_col, make into ndarray
    Vd_col.insert(0, 'Vd')
    Vd_col = np.array(Vd_col)


  ##### add labels to columns
    #### add labels to outputList
    for index in range(len(outputList)):
        outputList[index].insert(0, 'Vg' + str(column_list[index]))

    #### for 2D nd-arrays of strings, we use vstack to add a label row
    #### first, make label row, then make into nd-array...
    absOutputListLabelRow = []
    for index in range(absOutputList.shape[0]): # make label row
        absOutputListLabelRow.append('Abs Vg' + str(column_list[index]))
    absOutputListLabelRow = np.array(absOutputListLabelRow)
    #### then, vstack abs label row & abs table...
    absOutputList = np.vstack((absOutputListLabelRow, absOutputList.T))
    #### finally, orient so axes align with those of outputList.
    absOutputList = absOutputList.T

    # idrain_polyfit_matrix
    if file.split()[0] == 'IDVG':
        #### first, make label row, then make into nd-array...
        idrain_polyfit_matrix_LabelRow = []
        for index in range(idrain_polyfit_matrix.shape[1]):
            idrain_polyfit_matrix_LabelRow.append('dId/dVg '\
                                               + str(column_list[index]))
        idrain_polyfit_matrix_LabelRow = np.array(idrain_polyfit_matrix_LabelRow)
        #### then, vstack label row & table...
        idrain_polyfit_matrix = np.vstack((idrain_polyfit_matrix_LabelRow,\
                                     idrain_polyfit_matrix))
        #### finally, orient so axes align with those of outputList.
        idrain_polyfit_matrix = idrain_polyfit_matrix.T

    # linmob_matrix
    if file.split()[0] == 'IDVG':
        #### first, make label row, then make into nd-array...
        linmob_matrix_LabelRow = []
        for index in range(linmob_matrix.shape[1]):
            linmob_matrix_LabelRow.append('linmob '\
                                               + str(column_list[index]))
        linmob_matrix_LabelRow = np.array(linmob_matrix_LabelRow)
        #### then, vstack label row & table...
        linmob_matrix = np.vstack((linmob_matrix_LabelRow,\
                                     linmob_matrix))
        #### finally, orient so axes align with those of outputList.
        linmob_matrix = linmob_matrix.T

    # sqrtVd__matrix
    if file.split()[0] == 'IDVG':
        #### first, make label row, then make into nd-array...
        sqrtVd_matrix_LabelRow = []
        for index in range(sqrtVd_matrix.shape[1]):
            sqrtVd_matrix_LabelRow.append('SqrtVd '\
                                              + str(column_list[index]))
        sqrtVd_matrix_LabelRow = np.array(sqrtVd_matrix_LabelRow)
        #### then, vstack label row & table...
        sqrtVd_matrix = np.vstack((sqrtVd_matrix_LabelRow,\
                                    sqrtVd_matrix))
        #### finally, orient so axes align with those of outputList.
        sqrtVd_matrix = sqrtVd_matrix.T

    # sqrtAbs_polyfit_matrix
    if file.split()[0] == 'IDVG':
        #### first, make label row, then make into nd-array...
        sqrtAbs_polyfit_matrix_LabelRow = []
        for index in range(sqrtAbs_polyfit_matrix.shape[1]):
            sqrtAbs_polyfit_matrix_LabelRow.append('dSqId/dVg '\
                                              + str(column_list[index]))
        sqrtAbs_polyfit_matrix_LabelRow = np.array(sqrtAbs_polyfit_matrix_LabelRow)
        #### then, vstack label row & table...
        sqrtAbs_polyfit_matrix = np.vstack((sqrtAbs_polyfit_matrix_LabelRow,\
                                    sqrtAbs_polyfit_matrix))
        #### finally, orient so axes align with those of outputList.
        sqrtAbs_polyfit_matrix = sqrtAbs_polyfit_matrix.T

    # satmob_matrix
    if file.split()[0] == 'IDVG':
        #### first, make label row, then make into nd-array...
        satmob_matrix_LabelRow = []
        for index in range(satmob_matrix.shape[1]):
            satmob_matrix_LabelRow.append('satmob '\
                                              + str(column_list[index]))
        satmob_matrix_LabelRow = np.array(satmob_matrix_LabelRow)
        #### then, vstack label row & table...
        satmob_matrix = np.vstack((satmob_matrix_LabelRow,\
                                    satmob_matrix))
        #### finally, orient so axes align with those of outputList.
        satmob_matrix = satmob_matrix.T

    dummyOutputListLabelRow = []
    for index in range(absOutputList.shape[0]): # make label row
        dummyOutputListLabelRow.append('ESiO2 Vg' + str(column_list[index]))
    dummyOutputListLabelRow = np.array(dummyOutputListLabelRow)
    #### then, vstack abs label row & abs table...
    dummyOutputList = np.vstack((dummyOutputListLabelRow, dummyOutputList.T))
    #### finally, orient so axes align with those of outputList.
    dummyOutputList = dummyOutputList.T
  ##### add labels to columns

  ##### make outputList into nd-array
    outputList = np.array(outputList) # make outputList into ndarray

  ##### here we concatenate the data in the order we want them in the sheets
  ##### vstack the Vd_col and ndarray lists, then transpose them
    if file.split()[0] == 'IDVG':
        outputSheet = np.vstack((Vd_col.T, outputList, absOutputList,\
                             idrain_polyfit_matrix, linmob_matrix,\
                             sqrtVd_matrix, sqrtAbs_polyfit_matrix,\
                             satmob_matrix)).T
    else:
        outputSheet = np.vstack((Vd_col.T, outputList, absOutputList)).T

  ##### finally, we save the data as a .csv in the outFolder
    np.savetxt(outFolder + file + '.csv', outputSheet, fmt="%s", delimiter='\t')
