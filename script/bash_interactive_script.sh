#!/bin/bash

# an infinite loop. in this example, only the user's input of an empty string
# --- essentially, hitting RETURN instead of entering a project name when
# prompted --- will cause the program counter to leave the while loop.

while true; do # two statements on the same line are separated by a semicolon
               # here, "do" marks the start of the while loop's block of code,
               # while "done" below marks the end of it.

    # at the top of the loop, we prompt the user for input from the command line
    # and assign the input string to the variable PROJ
    # -p means "prompt"
    # "read without -r will mangle backslashes." ---shellcheck
    read -pr "please give a project name: " PROJ
    
    # next, we test whether the user's input satisfies the condition
    # to drop out of the infinite loop ---
    # in other words, has the user hit ENTER or RETURN,
    # (which generates the empty string),
    # instead of entering a project name?
    if [[ "$PROJ" == "" ]]
    then
        break # if the value of PROJ is the empty string, break out of while loop
    fi
    
    # otherwise, the user has entered a project name.
    # here, we tell the bash interpreter to make a directory
    # in the working directory with the project name as its name
    mkdir "$PROJ"

done # end of while loop

echo "and now we're out of the loop!"
