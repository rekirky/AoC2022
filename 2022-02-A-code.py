filename = "2022-02-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()

results = {'A X':4, 'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}
sum = 0
for i in input:
    sum += results[i]

print(f"The result of the games would be {sum}")

# Answer - 12535 Correct!
