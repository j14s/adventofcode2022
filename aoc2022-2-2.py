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
        them = them.rstrip()
        print(pair)
        if pair in ['AX', 'BX', 'CX']:
            if them == "A":
                my_points = 3
            elif them == "B":
                my_points = 1
            elif them == "C":
                my_points = 2
            else:
                print("no match")
            result = my_points + 0
        elif pair in ['AY', 'BY', 'CY']:
            if them == "A":
                my_points = 1
            elif them == "B":
                my_points = 2
            elif them == "C":
                my_points = 3
            else:
                print("no match")
            result = my_points + 3
        elif pair in ['BZ', 'CZ', 'AZ']:
            if them == "A":
                my_points = 2
            elif them == "B":
                my_points = 3
            elif them == "C":
                my_points = 1
            else:
                print("no match")
            result = my_points + 6
        else:
            print("not in set")
            exit()
        print(result)
        total_points = total_points + result

    print(total_points)

finally:
    f.close()