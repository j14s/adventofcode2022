#!/usr/bin/env python3

def cratemove_model(model):
    stacks_map = [[],[],[],[],[],[],[],[],[],[]]
    start_stacks = open("5-stacks.txt", 'r')

    stack_position = 1
    for stack in start_stacks:
        stack = stack.rstrip()
        for box in stack:
            stacks_map[stack_position].append(box)
        stack_position += 1

    #print(stacks_map)
    moves_list = open("5-moves.txt", 'r')
    for move in moves_list:
        move = move.rstrip()
        #print(move)
        (junk1, count, junk2, from_stack, junk3, to_stack) = move.split(" ")
        count = int(count)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        move_counter = 1
        if model == "9000":
            while move_counter <= count:
                moving_box = stacks_map[from_stack].pop(0)
                stacks_map[to_stack].insert(0, moving_box)
                move_counter += 1
        elif model == "9001":
            while count >= move_counter:
                count -= 1
                moving_box = stacks_map[from_stack].pop(count)
                stacks_map[to_stack].insert(0, moving_box)
        else:
            print("dont know that model of crate mover")
            exit(1)

    stack_count=1
    tops = ""
    while stack_count < len(stacks_map):
        tops += stacks_map[stack_count][0]
        stack_count += 1

    print(len(tops))
    print(tops)

cratemove_model("9000")
cratemove_model("9001")
