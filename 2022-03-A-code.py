import string
filename = "2022-03-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()
def counter(inputs):
    sum = 0
    for input in inputs:
        value = 0
        left = input[0:int(len(input)/2)]
        right = input[int(len(input)/2):]
        common = list(set(left)&set(right))
        for i in common:
            if i.islower():
                value = (string.ascii_lowercase.index(i)+1) 
            else:
                value = ((string.ascii_uppercase.index(i)+1)+26)
        sum += value    
    return sum


print(f"The sum of the backpacks would be {counter(input)}")

# Answer - 7875 Correct!



            



