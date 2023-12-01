path = "../inputs/day1_puzzle1.txt"

with open(path) as file:
    f = file.read()

# I think the only overlapping examples were in the sample?
text_map = {
    'eightwo' : '82',
    'oneight' : '18',
    'twone' : '21',
    'eight' : '8',
    'two' : '2',
    'one' : '1',
    'three' : '3',
    'four' : '4', 
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'nine' : '9'
}

input_lst = f.split("\n")

output_list = []

for input in input_lst:

    parsed_input = input

    for key, value in text_map.items():
        parsed_input = parsed_input.replace(key, value)

    first = -1
    last = -1
    
    for char in parsed_input:
        if char.isnumeric():
            
            if first == -1:
                first = char            
            
            last = char

    output_list.append(int(first + last))

print(f"Answer is: {sum(output_list)}")
