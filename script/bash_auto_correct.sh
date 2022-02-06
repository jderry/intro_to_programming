#!/bin/bash

DICT=$(find /usr -name american-english 2>/dev/null)

tr -d '[:punct:]' | #
tr -s ' ' '\n' | #
tr '[:upper:]' '[:lower:]' | #
sort | #
uniq | #
egrep -xvf $DICT
