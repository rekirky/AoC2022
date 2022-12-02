filename = "2022-01-input.txt"
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

output.sort()
print(f"Sum of 3 largest workers - {sum(output[-3:])}")

# Answer - 205615 Correct!