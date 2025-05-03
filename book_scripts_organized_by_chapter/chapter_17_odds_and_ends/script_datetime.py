import pandas as pd
import datetime as dt
import os

home = os.path.expanduser('~')

# first, use powershell to change character encoding of file to utf8 so that python can read it.
#PS C:\Users\cns-jderry> powershell -Command "Get-Content python\daily.txt 
#     -Encoding Unicode | Set-Content -Encoding UTF8 python\daily_utf8.txt"
#
df = pd.read_csv(home + '/datafile/datetime_input.csv', sep=',', encoding='utf-8')

# convert datetime strings in datetime to datetime objects
# sort df: order first by subject, then by datetime
df['datetime'] = pd.to_datetime(df.datetime)
df.sort_values(by=['ID', 'datetime'], inplace=True)
df = df.reset_index(drop=True)
same_day_entries = 'same day entries for: '

newDF = pd.DataFrame(columns=df.columns)
newDF_row = 0

''' fill in gaps in dates with blank records
'''
#  if (df.loc[1, 'datetime'].date() - df.loc[0, 'datetime'].date()).days == 1:
for row in range(len(df)-1):
    # if subject is the same
    if df.loc[row, 'ID'] == df.loc[row+1, 'ID']:
        #...and if the dates are the same
        if (df.loc[row+1, 'datetime'].date() - df.loc[row, 'datetime'].date()).days == 0:
            # update newDF, increment newDF_row
            newDF.loc[newDF_row] = df.loc[row]
            print(f"same_day_entries {df.loc[row, 'ID']}")
            newDF_row += 1
        # ...and if the dates are in sequence
        elif (df.loc[row+1, 'datetime'].date() - df.loc[row, 'datetime'].date()).days == 1:
            # update newDF, increment newDF_row
            newDF.loc[newDF_row] = df.loc[row]
            newDF_row += 1
        #...and if the dates have a gap
        elif (df.loc[row+1, 'datetime'].date() - df.loc[row, 'datetime'].date()).days > 1:
            newDF.loc[newDF_row] = df.loc[row]
            newDF_row += 1
            # iterate over the difference between the two dates
            for date_diff in range((df.loc[row+1, 'datetime'].date() - df.loc[row, 'datetime'].date()).days-1):
                # increment newDF_row, insert new record into newDF
                newDF.loc[newDF_row, 'ID'] = df.loc[row, 'ID']
                newDF.loc[newDF_row, 'datetime'] = newDF.loc[newDF_row-1, 'datetime'] + dt.timedelta(days=1)
                newDF_row += 1
    else:
        # the subject is NOT the same
        newDF.loc[newDF_row] = df.loc[row]
        newDF_row += 1
newDF.loc[newDF_row] = df.loc[row+1]

'''update the df with the newDF, insert columns;
   append entries for ID counts less than 14.
'''
print("\n")
df = newDF
df.insert(loc=1, column='entry_no', value=0)

newDF = pd.DataFrame(columns=df.columns)
newDF_row = 0

entry_cnt = 1
for row in range(len(df)-1):
    # if subject is the same...
    if df.loc[row, 'ID'] == df.loc[row+1, 'ID']:
        df.loc[row, 'entry_no'] = entry_cnt
        entry_cnt += 1 # increment subject record counter
        newDF.loc[newDF_row] = df.loc[row]
        newDF_row += 1
    # if subject is not the same...
    elif df.loc[row, 'ID'] != df.loc[row+1, 'ID']:
        df.loc[row, 'entry_no'] = entry_cnt
        newDF.loc[newDF_row] = df.loc[row]
        newDF_row += 1
        if entry_cnt < 14:
            print(f"missing entries: {int(df.loc[row, 'ID'])} : {entry_cnt}")
            for date_diff in range(entry_cnt+1,15):
                # increment newDF_row, insert new record into newDF
                newDF.loc[newDF_row, 'entry_no'] = date_diff
                newDF.loc[newDF_row, 'ID'] = df.loc[row, 'ID']
                newDF.loc[newDF_row, 'datetime'] = newDF.loc[newDF_row-1, 'datetime'] + dt.timedelta(days=1)
                newDF_row += 1
        entry_cnt = 1 # reset to 1

newDF.to_csv(home + '/datafile/datetime_output.csv', sep='\t', index=False) 
