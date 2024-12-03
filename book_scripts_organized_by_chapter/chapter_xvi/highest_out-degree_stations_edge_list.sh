gawk -F"\t" '{print $3}' datafile/edge_list | sort | uniq -c | sort -n | tail
