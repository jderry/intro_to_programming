# 1) create a temp file containing human-readable datetime of datafile's creation.
# append an empty line to the bottom of the file.
stat --format='%w' Guest.txt > guest_creation_date && echo "" >> guest_creation_date
# 2) create a text file named 'header.txt'. save dataset's provenance info
# in file. append an empty line to the bottom of the file.
echo "" >> header.txt
# catenate it and guest_creation_date to top of dataset file.
cat guest_creation_date header.txt Guest.txt > Guest_tmp && mv Guest_tmp Guest.txt
# 3) make read-only archive copy,
# name it with file's creation timedate in UNIX time
ARCHIVENAME=$(stat --format='%W' Guest.txt)_Guest.txt
cp Guest.txt $ARCHIVENAME && chmod 440 $ARCHIVENAME
# 4) create a bash variable and assign it the string that is the filepath
FILENAME=Guest.txt
# 5) through sed, instruct the machine to find the line
# containing the substring 'Date Time Temperature',
# replace the line with 'Date Time Temp(C)' --- the 'c' means 'change'
sed -i '/Date Time Temperature/c\Date Time Temp(C)' $FILENAME
# 6) through sed, tell the machine that starting on line 11,
# replace the last two chars at the end of every line with the empty string
sed -i '12,$ s/..$//' $FILENAME
