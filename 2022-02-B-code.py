filename = "2022-02-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()
results = {'A X':3, 'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}
sum = 0
for i in input:
    sum += results[i]

print(f"The result of the games would be {sum}")

# Answer - 15457 Correct!
