#!/usr/bin/env python3

alphas = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("3.input", 'r')

def per_rucksack():
    commons_sum = 0
    line_count = 0

    for line in f:
        line_count = line_count +1
        found = False
        line = line.rstrip()
        first_bucket_len = int(len(line)/2)
        second_bucket_len = first_bucket_len
        first_bucket = line[:first_bucket_len]
        second_bucket = line[second_bucket_len:]
        #print("%s : %s" % (first_bucket, second_bucket))
        for a in first_bucket:
            #print("-------------------------------------")
            for b in second_bucket:
                if a == b:
                    a_index = alphas.rfind(a)
                    commons_sum = commons_sum + a_index
                    #print(a, a_index, commons_sum, line_count)
                    found = True
                    break
            if found is True:
                break
    print(commons_sum)

def badges_per_group():

    rucksacks_list = []
    groups = []

    for line in f:
        line = line.rstrip()
        rucksacks_list.append(line)

    while len(rucksacks_list) != 0:
        r1 = rucksacks_list.pop()
        r2 = rucksacks_list.pop()
        r3 = rucksacks_list.pop()

        found = False
        for a in r1:
            for b in r2:
                for c in r3:
                    if a == b == c:
                        a_index = alphas.rfind(a)
                        groups.append(a_index)
                        found = True
                        break
                if found is True:
                    break
            if found is True:
                break

    badge_sum = 0
    print(len(groups))
    for badge in groups:
        badge_sum = badge_sum + badge
        #print(badge)
    print(badge_sum)

#per_rucksack()
badges_per_group()

