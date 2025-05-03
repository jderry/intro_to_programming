# returns the number of specimens that made it into edge list
gawk -F"\t" '{print $1}' "$HOME"/datafile/edge_list |# extract column 1
uniq |# return a single instance of each contiguous identical group of specimens
wc -l # return the number of specimens
