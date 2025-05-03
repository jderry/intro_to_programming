#!/bin/bash

zcat "$HOME"/datafile/hygdata_v41.zip |#
tail -n +2 |# drop the label line
sed -e 's/""//g' |# replace empty strings with empty space
grep -E '(Alkaid|Alcor|Mizar|Alioth|Megrez|Phecda|Merak|Dubhe)'\
        > big_dipper.txt
