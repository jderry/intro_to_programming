# first, load the loadAsLoL() function in session memory
%run repo/intro_to_programming/script/loadAsLoL.py

# next, load the dataset into session memory as a list-of-lists
LoL = loadAsLoL('datafile/reformatted_Unigene.fa')

# now we create a list of all the strings' lengths
strLen = []
for record in LoL:
    strLen.append(len(record[6]))

# finally, we create a histogram of the string lengths
# 1000 bins gives a sufficient smoothness to the curve
# described by the top of the histogram
plt.hist(strLen, 1000)
plt.axis('equal')
plt.show()