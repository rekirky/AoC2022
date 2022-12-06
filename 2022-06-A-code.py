filename = "2022-06-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()
    input = str(input[0])

def find_marker(value):
    for i in range(len(value)):
        check = value[i:i+4]
        if len(set(check)) == len(check):
            return(i+len(check))

print(f"The position of first marker is {find_marker(input)}")

# Answer - 1093 Correct!



    