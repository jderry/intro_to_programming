# coding: utf-8
''' the mass spec device generates datafiles using microsoft print chars and adds an empty column to the end of each record.
    this script drops the empty column using dropna(axis=1, how='all')
    specification: if a record contains two or three trials with non-zero float, 
    write arithmetic mean and std deviation of trials to end of record.
    otherwise, write out zeros in mean and std deviation columns.
    write out dataframe as csv file.
'''

import pandas as pd
import numpy as np

df = pd.read_csv('../datafile/mass_spec_data.csv')

df=df.dropna(axis=1,how='all') # drop empty column
df = df.replace(0, np.nan) # replace zeros with NaN
nanList = df.isnull().sum(axis=1).tolist() # create a list, each value a sum of NaNs in a row
df.loc[:,'average'] = 0. # add column for arithmetic mean, fill with float zeros --- this is a maintenance update
df.loc[:,'std_dev'] = 0. # add column for standard deviation, fill with float zeros

for row in range(len(nanList)): # this for-loop goes down the rows
    if nanList[row] < 2: # and if a row's NaN count is less than 2, then...
        df.iloc[row,4] = np.mean(df.iloc[row, 1:4]) # write the mean of columns 1,2,3 in column 4
        df.iloc[row,5] = np.std(df.iloc[row, 1:4]) # write their standard deviation in column 5 


df = df.replace(np.nan, 0) # replace NaNs with zeros, restoring the numerical format of the data

df.to_csv('../datafile/mass_spec_fixed_csv', float_format='%.9f', index=False) # write out the results
