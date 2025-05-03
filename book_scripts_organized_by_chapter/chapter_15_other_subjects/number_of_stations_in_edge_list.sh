# returns the number of stations in the edge list
# write out station labels in columns 2 and 3
gawk -F"\t" '{print $2}' "$HOME"/datafile/edge_list > "$HOME"/all_stations
gawk -F"\t" '{print $3}' "$HOME"/datafile/edge_list >> "$HOME"/all_stations

cat "$HOME"/all_stations |# read all stations into pipeline
sort |# sort station labels
uniq |# return a single instance of each contiguous identical group
wc -l # return the number of feeding stations in edge_list
