tail -n +2 "$HOME"/datafile/hewitsoni_males.txt |# read into pipeline all records, removing label line
gawk -F"\t" '{print $2}' |# extract column 1
uniq |# return a single instance of each contiguous identical group of specimen labels
wc -l # return the number of unique specimen labels
