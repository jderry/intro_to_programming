gawk -F"\t" '{print $2}' datafile/edge_list | sort | uniq -c | sort -n | tail
