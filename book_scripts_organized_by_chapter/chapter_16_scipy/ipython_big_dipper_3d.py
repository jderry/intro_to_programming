import pandas as pd
import matplotlib.pyplot as plt
import os

home = os.path.expanduser('~')

# we need the starTable's label line
starTable = pd.read_csv(home + '/datafile/hygdata_v41.zip',\
                        sep=',',\
                        compression='zip')
label_line = starTable.columns.tolist()

# now we label the columns in the big dipper dataframe
big_dipper = pd.read_csv(home + '/datafile/big_dipper.txt',\
                         index_col=0,\
                         names=label_line)

# make 3D rotatable plot of big dipper
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x, y, z = big_dipper['x'], big_dipper['y'], big_dipper['z']
ax.scatter(x, y, z)
plt.show()

