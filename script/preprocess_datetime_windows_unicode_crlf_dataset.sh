#!/bin/bash

# we start by getting stats on our file
wc datetime_windows_unicode_crlf_dataset.txt 
# zero lines!
file datetime_windows_unicode_crlf_dataset.txt 
# ok --- the text encoding is neither ascii nor utf-8,
# and carriage return (CR), instead of newline characters end the lines.
# this file was generated on a windows/ms-dos machine that used non-standard text encoding.
# we need to fix these issues before we can work with the file.
# let's start by converting the encoded text into ascii
cat datetime_windows_unicode_crlf_dataset.txt | iconv -f UTF-16 -t ASCII//TRANSLIT > ascii.txt
# did it work?
file ascii.txt
# yes! now, let's replace the CR line terminators with newline characters...
cat ascii.txt | tr '\015' "\n" > newline.txt
# did it work?
file newline.txt 
# yes!
wc newline.txt
# the line count looks ok. we can process the file further.

