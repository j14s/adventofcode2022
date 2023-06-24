#!/usr/bin/env python3

with open("6-input.txt", 'r') as file:
    input = file.read().rstrip()

def search_signal(start, length):
    for pos in input:
        end = start + length
        this_four = list(input[start:end])
        start += 1
        if len(this_four) == len(set(this_four)):
            return(end)

packet = search_signal(0, 4)
print(packet)

message = search_signal(packet, 14)
print(message)