gawk -F"\t" '{print $2}' datafile/hewitsoni_males.txt | uniq -c | sort -n | tail
