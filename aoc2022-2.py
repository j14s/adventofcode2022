#!/usr/bin/env python3
from sys import exit

# ROCK     = A = X = 1
# PAPER    = B = Y = 2
# SCISSORS = C = Z = 3

# WIN = 6
# TIE = 3
# LOSS = 0

# AX = BY = CZ = "tie"
# AY = BZ = CX = "win"
# BX = CY = AZ = "loss"

total_points = 0

try:
    f = open("aoc2022-2-input", 'r')
    for set in f:
        results = my_points = 0
        pair = set.replace(" ","")
        pair = pair.rstrip()
        (them, me) = set.split(" ")
        me = me.rstrip()
        print(me)
        if me == "X":
            my_points = 1
        elif me == "Y":
            my_points = 2
        elif me == "Z":
            my_points = 3
        else:
            print("Didn't match XYZ")
            exit()
        print(pair)
        if pair in ['AX', 'BY', 'CZ']:
            result = my_points + 3
        elif pair in ['AY', 'BZ', 'CX']:
            result = my_points + 6
        elif pair in ['BX', 'CY', 'AZ']:
            result = my_points + 0
        else:
            print("not in set")
            exit()
        print(result)
        total_points = total_points + result

    print(total_points)

finally:
    f.close()