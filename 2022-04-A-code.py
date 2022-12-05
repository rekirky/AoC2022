filename = "2022-04-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()

count = 0
for i in input:
    input_split = i.split(",")
    a = input_split[0].split("-")
    b = input_split[1].split("-")
    a = [eval(i) for i in a]
    b = [eval(i) for i in b]
    if (a[0] <= b[0] and a[1] >= b[1]) | (b[0] <= a[0] and b[1] >= a[1]):
        count += 1

print(f"The number of overlapping pairs is {count}")

# Answer - 567 Correct!


