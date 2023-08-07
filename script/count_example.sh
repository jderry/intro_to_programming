#!/bin/bash

COUNTER=0

while true 
 do
    ((COUNTER++))
    printf "The value of the counter is COUNTER=%d\n" "$COUNTER"
 done
