#!/usr/bin/python3
# we assume a fair player.

from math import ceil, log

# in this interactive while loop, the script explains the game, gets highest integer of range from user;
# and initializes floor and ceiling variables
while True:
    rules_of_game = \
   ("\nin this game you give me a range of integers from 1 to some number you choose.\n"
    "then you will pick a number within this range for me to guess.\n"
    "i will try to guess your number in the fewest number of tries.\n"
    "for each guess, you will tell me if your number is higher than (h),\n"
    "lower than (l), or equal to (=) your number. ready?\n")
    print(rules_of_game)
    floor = 1
    ceiling = input(f"please enter the highest number of your range: ")
    ceiling = int(ceiling)

    # 'continue' is related to 'break' ---
    # it returns the program counter to the top of the while loop.
    if not isinstance(ceiling, int) and\
       not ceiling > 1:
        print(f"that's not a legitimate value. please enter a counting number greater than 1.")
        continue
        
    else:
        break

# print the challenge of fewest guesses using this algorithm
# use the math module's ceil() and log() functions
nguesses = ceil(log(ceiling)/log(2))
print("\n")
print(f"i can guess your number in at most {nguesses} guesses!\n")

# initalize the guess counter
guessCnt = 0
while True:
    guessCnt = guessCnt + 1
    guess = (floor + ceiling)//2

    answer = input(f"i guess {guess}! Is your number higher (h), lower (l), or equal (=)? ")

    # several if-statements, each processing different user input
    if answer == 'h':
        floor = guess
    elif answer == 'l':
        ceiling = guess
    else:
        print(f"\nyee-haw! i guessed your number is {guess} in {guessCnt} guesses!\n")
        break

