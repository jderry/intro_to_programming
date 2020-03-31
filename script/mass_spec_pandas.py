# coding: utf-8
import pandas as pd
import numpy as np

df = pd.read_csv('/home/james/datafile/rachel_data.csv')

df=df.dropna(axis=1,how='all') # drop empty column
df = df.replace(0, np.nan) # replace zeros with NaN
nanList = df.isnull().sum(axis=1).tolist() # create a list, each value a sum of NaNs in a row
df.loc[:,'average'] = 0 # add column for arithmetic mean, fill with zeros
df.loc[:,'std_dev'] = 0 # add column for standard deviation, fill with zeros

for row in range(len(nanList)): # this for-loop goes down the rows
    if nanList[row] < 2: # and if a row's NaN count is less than 2, then...
        df.iloc[row,4] = np.mean(df.iloc[row, 1:4]) # write the mean of columns 1,2,3 in column 4
        df.iloc[row,5] = np.std(df.iloc[row, 1:4]) # write their standard deviation in column 5 


df = df.replace(np.nan, 0) # replace NaNs with zeros, restoring the numerical format of the data

df.to_csv('rachel_fixed_csv', float_format='%.9f', index=False) # write out the results
