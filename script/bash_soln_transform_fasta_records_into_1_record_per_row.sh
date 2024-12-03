# lines 4-7 to "linearize the sequences"
# from https://www.biostars.org/p/17680/ by Frédéric Mahé
# Creative Commons License
zcat All-Unigene.fa.zip |# read fasta recordset in zipped file into memory
sed -E -e 's/(^>.*$)/#\1#/' |# use egrep; enclose 1st line in each record with hash marks
tr -d "\n" |# delete newline characters
tr "#" "\n" |# replace hash symbols with newline characters
sed -e '/^$/d' |# delete empty lines
tr -d "\n" |# delete newline characters --- fasta record separator (>) is in place
tr '>' "\n" |# replace > with newline characters
sed -e 's/%/% /' |# insert a space after the percent sign. space is field separator.
tr -s ' ' |# replace each sequence of a repeated character with a single occurrence.
sed -e '/^$/d' # delete empty lines

