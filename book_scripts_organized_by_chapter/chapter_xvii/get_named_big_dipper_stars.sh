#!/bin/bash

zcat "$HOME"/datafile/hygdata_v41.zip |# extract the star catalog from the zip file
tail -n +2 | #
sed -e 's/""//g' |# replace empty strings with empty space
grep -E '(Alkaid|Alcor|Mizar|Alioth|Megrez|Pheca|Merak|Dubhe)' > big_dipper.txt
