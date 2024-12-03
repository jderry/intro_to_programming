#!/bin/bash

DICT=/usr/share/dict/american-english

# extended grep, case-insensitive matches
grep -Ei "^[BEHILOS]*$" $DICT
