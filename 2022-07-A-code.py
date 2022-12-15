filename = "2022-07-input.txt"
with open(filename,'r') as f:
    input = f.read().splitlines()
    #input = str(input[0])

test_input = ["$ cd /","$ ls","dir a","14848514 b.txt","8504156 c.dat","dir d","$ cd a","$ ls","dir e","29116 f","2557 g","62596 h.lst","$ cd e","$ ls","584 i","$ cd ..","$ cd ..","$ cd d","$ ls","4060174 j","8033020 d.log","5626152 d.ext","7214296 k"]

#input = test_input

directory = "/"
directory_size = {}
files = {}
combined = {}
combined_2 = {}

def cd(input):
    global directory
    value = input[5:]
    if value == '/':
        directory = '/'
    elif value == '..':
        directory = directory[:-directory.find('/',len(directory)-4)]
    else:
        directory = directory + value + '/'

def command(input):
    if input[0:4] == "$ cd":
        cd(input)
    
def calculate_size(files):
    global combined_2
    global combined
    global directory_size
    for k,v in files.items():
        filename = k[k.rfind("/")+1:]
        folder = (k[:k.find(filename)])
        if folder in directory_size.keys():
            directory_size[folder] = directory_size[folder] + int(v)
        else:
            directory_size[folder] = int(v)

    for k,v in directory_size.items():
        if k not in combined.keys():
                combined[k] = int(v)
        for xk,xv in directory_size.items():
            if (k in xk) and (k != xk):
                if k in combined.keys():
                    combined[k] = combined[k] + int(xv)

    # Need recusion here to dial down into sub-folders    
    
def prune(folders):
    sum = 0
    for k,v in folders.items():
        if int(v) <= 100000:
            sum += int(v)
    print(sum)
    print(1501149)
        

def main():
    global files
    while len(input) > 0:
        if (input[0][0:4]) == ("$ cd"):
            command(input[0])
        if input[0][0].isdigit():
            files[directory+input[0][input[0].find(' ')+1:]] = input[0][:input[0].find(' ')+1]
        input.remove(input[0])
    calculate_size(files)
    prune(combined_2)
main()

#directory = cd(directory,value)
#print(directory)



