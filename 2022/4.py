#!/usr/bin/env python3

f = open("4.txt", 'r')

pairs_list = []

hit = 0
overlap = 0
miss = 0

for line in f:
    line = line.rstrip()
    first_set, second_set = line.split(',')

    #print(first_set, second_set)
    first_set_begin, first_set_end = first_set.split('-')
    second_set_begin, second_set_end = second_set.split('-')

    first_set_begin  = int(first_set_begin)
    first_set_end    = int(first_set_end)
    second_set_begin = int(second_set_begin)
    second_set_end   = int(second_set_end)

    set_a = set()
    set_b = set()

    add_this_to_a = first_set_begin
    add_this_to_b = second_set_begin

    while add_this_to_a <= first_set_end:
        set_a.add(add_this_to_a)
        add_this_to_a += 1
    while add_this_to_b <= second_set_end:
        set_b.add(add_this_to_b)
        add_this_to_b += 1

    #print(set_a)
    #print(set_b)

    if set_a.issubset(set_b) or set_b.issubset(set_a):
        hit += 1
    elif set_a.intersection(set_b):
        overlap += 1
    else:
        miss += 1

    both = hit + overlap

print(" Total Contained Sets: %s\n Total Overlapping Sets: %s\n Total Contained/Overlapping Sets: %s\n Total not contained or overlapping: %s" % (hit, overlap, both, miss))


#This seemed to work but didn't.
#returned 603 hit and 397 miss out of 1000
# hit = 0
# miss = 0
# for line in f:
#     line = line.rstrip()
#     first_set, second_set = line.split(',')

#     #print(first_set, second_set)
#     fs_a, fs_b = first_set.split('-')
#     ss_a, ss_b = second_set.split('-')

#     #print(fs_a, fs_b, ss_a, ss_b)
#     if ss_a >= fs_a and ss_b <= fs_b:
#         hit += 1
#         print("%s : %s is contained within %s" % (line, second_set, first_set))
#     elif fs_a >= ss_a and fs_b <= ss_b:
#         hit += 1
#         print("%s : %s is contained within %s" % (line, first_set, second_set))
#     else:
#         miss += 1
#         print("%s : neither pair is contined fully in the other" % line)

# print("Total contained sets: %s Total not container: %s" % (hit, miss))