#!/usr/bin/env python3

with open("6-input.txt", 'r') as file:
    input = file.read().rstrip()

def search_signal(start, length):
    start_position = start
    for pos in input:
        start_position_end = start_position + length
        this_four = list(input[start_position:start_position_end])
        start_position += 1
        if len(this_four) == len(set(this_four)):
            return(start_position_end)

signal_position_end = search_signal(0, 4)
print(signal_position_end)

message_position_end = search_signal(signal_position_end, 14)
print(message_position_end)

