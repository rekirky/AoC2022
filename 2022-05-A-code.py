import pandas as pd
import numpy as np
filename = "2022-05-input.txt"

# First 9 lines are a start state
# Remainder are commands
r1,r2,r3,r4,r5,r6,r7,r8,r9 = [],[],[],[],[],[],[],[],[]

with open(filename,'r') as f:
    input = [next(f) for x in range(8)]
    for value in input:
        chunk = [value[i:i+4].strip("\n").strip(" ") for i in range(0,len(value),4)]
        r1.append(chunk[0])
        r2.append(chunk[1])
        r3.append(chunk[2])
        r4.append(chunk[3])
        r5.append(chunk[4])
        r6.append(chunk[5])
        r7.append(chunk[6])
        r8.append(chunk[7])
        r9.append(chunk[8])

def clean(input):
    cleaned=""
    input.reverse()
    input[:] = [x for x in input if x]
    for i in input:
        cleaned += i[1]
    return cleaned

r1 = clean(r1)
r2 = clean(r2)
r3 = clean(r3)
r4 = clean(r4)
r5 = clean(r5)
r6 = clean(r6)
r7 = clean(r7)
r8 = clean(r8)
r9 = clean(r9)

df = pd.DataFrame(data=(r1,r2,r3,r4,r5,r6,r7,r8,r9))

with open(filename,'r') as f:
    input = f.readlines()

input = input[10:]
input = [i.strip("\n") for i in input]

def move(input,string):
    string = string.split()
    moves = int(string[1])
    move_from = int(string[3])-1
    move_to = int(string[5])-1
    for i in range(moves):
        value = (input[0][move_from][-1:])
        input[0][move_from] = input[0][move_from][:-1]
        input[0][move_to] += value
    return(input)

for i in input:
    df = move(df,i)

number = ""
for i in df[0]:
    number += i[-1]

print(f"The string is {number}")

# Answer - JRVHHCSJ Correct!



            
    





