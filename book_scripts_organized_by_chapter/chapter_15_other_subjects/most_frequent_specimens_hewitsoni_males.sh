gawk -F"\t" '{print $1}' datafile/hewitsoni_males.txt | uniq -c | sort -n | tail
