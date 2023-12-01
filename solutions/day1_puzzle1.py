path = "../inputs/day1_puzzle1.txt"

with open(path) as file:
    f = file.read()

input_lst = f.split("\n")

output_list = []

for input in input_lst:
    first = -1
    last = -1
    
    for char in input:
        if char.isnumeric():
            
            if first == -1:
                first = char            
            
            last = char

    output_list.append(int(first + last))

print(f"Answer is: {sum(output_list)}")
