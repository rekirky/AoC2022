filename = "2022-01-input.txt"
with open(filename,'r') as f:
    numbers = f.read().splitlines()
    
total = 0
largest_sum = 0

for number in numbers:
  if number == "":
    if total > largest_sum:
      largest_sum = total
    total = 0
  else:
    total += int(number)

if total > largest_sum:
  largest_sum = total
print(largest_sum)