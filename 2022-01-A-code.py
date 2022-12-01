filename = "2022-01-A-input.txt"

with open(filename,'r') as f:
    input = f.read().splitlines()

output=[]
a=0
for i in input:
    if i != "":
        a+=int(i)
    else:
        output.append(a)
        a = 0

print(f"Max calories is {max(output)} carried by robot {output.index(max(output))}")

# Answer - 69289 Correct!