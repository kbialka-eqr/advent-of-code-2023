def extract_symbols(schematic: list) -> set:
    """Extract symbols from schematic set as list of strings."""

    symbols = set()

    for line in schematic:
        for char in line:
            if not char.isnumeric() and char != ".":
                symbols.add(char)

    return symbols


def find_numbers(schematic_line: str) -> list[tuple]:
    """Take a schematic line and return a list of tuples containing the starting
    indices of each number in the schematic line and the number itself."""

    starting_indices = []
    nums = []

    in_search = False
    search_num = ""

    for i, char in enumerate(schematic_line):
        if char.isnumeric():
            if in_search:
                search_num += char
            else:
                in_search = True
                starting_indices.append(i)
                search_num += char
        else:
            if in_search:
                nums.append(int(search_num))
                in_search = False
                search_num = ""

    if in_search:
        nums.append(int(search_num))

    return list(zip(starting_indices, nums))


def get_bounding_box(number: str, point: tuple) -> list:
    '''Get coordinate points around number.'''
    left = [(point[0], point[1] - 1)]
    right = [(point[0], point[1] + len(str(number)))]
    top = [(point[0] - 1, i) for i in range(point[1] - 1, point[1] + len(str(number)) + 1)]
    bottom = [(point[0] + 1, i) for i in range(point[1] - 1, point[1] + len(str(number)) + 1)]

    combined = left + right + top + bottom

    # Remove situations where indices become -1 bc it's a valid search
    # element but not how I'm going to use it
    return [point for point in combined if -1 not in point]


def is_symbol_adjecent(schematic, number, point, symbols):
    '''Determine if a number is adject to a symbol.'''
    bounding_box = get_bounding_box(number, point)

    for row, col in bounding_box:
        try:
            if schematic[row][col] in symbols:
                return True
        except:
            # I don't feel like handling out of index
            continue

    return False


if __name__ == "__main__":
    path = "../inputs/day3.txt"
    with open(path) as file:
        f = file.read()

    schematic = f.split("\n")
    symbols = extract_symbols(schematic)

    valid_nums = []

    for row_num, line in enumerate(schematic):
        num_data = find_numbers(line)

        for col_num, num in num_data:
            if is_symbol_adjecent(schematic, num, (row_num, col_num), symbols):
                valid_nums.append(num)

    print(f"Answer is: {sum(valid_nums)}")
