filename = "2022-08-input.txt"
with open(filename, 'r') as f:
    input = f.read().splitlines()
    for i in range(len(input)):
        input[i] = int(input[i])


test_input = [30373, 25512, 65332, 33549, 35390]
input = test_input
count = 0

def always_visible(input):
    global count
    for i in range(len(input)):
        # top and bottom trees
        if i == 0 or i == len(input)-1:
            count += len(str(input[i]))
        # perimeter trees
        else:
            count += 2

def sometimes_visible(input):
    global count
    for i in range(len(input)):
        print(f'i={i}')
        print(input[i])
        if i > 0:
            previous = current
            current = [int(x) for x in str(input[i])]
            for item in range(len(current)):
                print(f'{current[item]},{previous[item]}')
                
        else:
            current = [int(x) for x in str(input[i])]        
        



def main():
    always_visible(input)
    print(f'Peri-{count}')
    sometimes_visible(input)

main()


# 3 0 3 7 3
# 2 5 5 1 2
# 6 5 3 3 2
# 3 3 5 4 9
# 3 5 3 9 0
