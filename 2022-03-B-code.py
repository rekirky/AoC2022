import string
filename = "2022-03-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()


def counter(inputs):
    elves = []
    common = []
    counter = 1
    for i in range(len(inputs)):
        if counter%3 == 0:
            elves.append(inputs[i])
            common.append(list(set(elves[0])&set(elves[1])&set(elves[2])))
            elves = []
        else:
            elves.append(inputs[i])
        counter+=1
    return (value(common))
    
def value(common):
    sum = 0
    for i in common:
        if str(i).islower():
            value = (string.ascii_lowercase.index(i[0])+1) 
        else:
            value = ((string.ascii_uppercase.index(i[0])+1)+26)
        sum += value    
    return sum

print(f"The sum of the backpacks would be {counter(input)}")

# Answer - 2479 Correct!



            



