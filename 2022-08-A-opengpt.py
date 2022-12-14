filename = "2022-08-input.txt"
with open(filename,'r') as f:
   tgrid = f.read().splitlines()

grid = []
for i in range(len(tgrid)):
    grid.append(list(tgrid[i]))

grid = [[int(i) for i in inner] for inner in grid]

# Initialize a variable to keep track of the count of numbers on the perimeter
perimeter_count = 0

# Iterate over the elements on the first and last rows, as well as the first and last columns of the grid
for row in [0, len(grid) - 1]:
  for col in range(len(grid[0])):
    perimeter_count += 1

for col in [0, len(grid[0]) - 1]:
  for row in range(1, len(grid) - 1):
    perimeter_count += 1

# Initialize a variable to keep track of the total number of visible trees
total_visible = 0

# Iterate over the grid
for row in range(len(grid)):
    for col in range(len(grid[0])):
    # Get the height of the current tree
        tree_height = grid[row][col]
           # Check the visibility of the current tree by looking at the other trees in the same row and column
        visible = True
        for i in range(len(grid)):
            if i != row and grid[i][col] > tree_height:
                    visible = False
                    break
        if visible:
            for j in range(len(grid[0])):
                if j != col and grid[row][j] > tree_height:
                    visible = False
                    break
    # If the current tree is visible, increment the total number of visible trees
        if visible:
            print(grid[row][col])
            total_visible += 1

# Initialize a variable to keep track of the count of numbers on the perimeter
perimeter_count = 0

# Iterate over the elements on the first and last rows, as well as the first and last columns of the grid
for row in [0, len(grid) - 1]:
  for col in range(len(grid[0])):
    perimeter_count += 1

for col in [0, len(grid[0]) - 1]:
  for row in range(1, len(grid) - 1):
    perimeter_count += 1


# Print the total number of visible trees
print(perimeter_count)
print(total_visible)
print(total_visible+perimeter_count)

