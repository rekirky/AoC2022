filename = "2022-04-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()

count = 0
for i in input:
    input_split = i.split(",")
    a = [eval(i) for i in input_split[0].split("-")]
    b = [eval(i) for i in input_split[1].split("-")]
    overlap = list(set(range(a[0],a[1]+1))&set(range(b[0],b[1]+1)))
    if len(overlap) >0:
        count +=1
    
print(f"The number of overlapping pairs is {count}")

# Answer - 907 Correct!


