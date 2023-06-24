#!/usr/bin/env python3

input_file="7-test-input.txt"

def loadData():
    input = open(input_file, 'r')
    data=[]

    for line in input:
        line = line.rstrip()
        #print(line)
        data.append(line)
    return(data)
    input.close()

my_data = loadData()

for i in my_data:
    print(i)
