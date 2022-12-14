filename = "2022-01-input.txt"
with open(filename,'r') as f:
    numbers = f.read().splitlines()

import heapq

total = 0
largest_groups = []

for number in numbers:
  if number == "":
    heapq.heappush(largest_groups, total)
    total = 0
  else:
    total += int(number)

heapq.heappush(largest_groups, total)
print(total)  

# Get the three largest groups
largest_groups = heapq.nlargest(3, largest_groups)
print(largest_groups)  

# Sum the three largest groups
result = sum(largest_groups)
print(result)  