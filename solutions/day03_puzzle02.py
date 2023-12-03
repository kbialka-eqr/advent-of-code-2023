def find_stars(schematic_line: str) -> list:
    '''Return a list of indices for each `*` character.'''
    idxs = []

    for i, char in enumerate(schematic_line):
        if char == '*':
            idxs.append(i)

    return idxs


def get_bounding_box(number: str, point: tuple) -> list:
    '''Take a number (or *) represented as a string and it's (x,y) point on the schematic
    and generate a bounding box of (x, y) coords as a list.'''
    left = [(point[0], point[1] - 1)]
    right = [(point[0], point[1] + len(str(number)))]
    top = [(point[0] - 1, i) for i in range(point[1] - 1, point[1] + len(str(number)) + 1)]
    bottom = [(point[0] + 1, i) for i in range(point[1] - 1, point[1] + len(str(number)) + 1)]

    combined = left + right + top + bottom

    # Remove situations where indices become -1 bc it's a valid search 
    # element but not how I'm going to use it
    return [point for point in combined if -1 not in point]


def generate_int_coord_map(schematic: list) -> dict:
    '''Take a schematic line and return a list of tuples containing the starting 
    indices of each number in the schematic line and the number itself.'''
    
    starting_indices = []
    nums = []

    in_search = False
    search_num = ''
    coordinates = []
    int_coord_map = {}

    for row, line in enumerate(schematic):
        for i, char in enumerate(line):
            if char.isnumeric():
                if in_search:
                    search_num += char
                    coordinates.append((row, i))
                else:
                    in_search = True
                    starting_indices.append(i)
                    search_num += char
                    coordinates.append((row, i))
            else:
                if in_search:
                    nums.append(int(search_num))
                    #int_coord_map[int(search_num)] = coordinates
                    int_coord_map[coordinates[0]] = [int(search_num), coordinates]
                    in_search = False
                    search_num = ''
                    coordinates = []

        # End search at EOL
        if in_search:
            nums.append(int(search_num))
            int_coord_map[coordinates[0]] = [int(search_num), coordinates]
            in_search = False
            search_num = ''
            coordinates = []


        if in_search:
            nums.append(int(search_num))
            int_coord_map[coordinates[0]] = [int(search_num), coordinates]
        
    return int_coord_map


def is_gear(int_coord_map, bounding_box, schematic):
    '''Given a {int : coord} map and the bounding box for an asterisk 
    determine if the star in the bounding box is a gear'''
   
    matching_keys = set()
    matching_nums = []

    for start_idx, val in int_coord_map.items():

        num = val[0]
        coord_list = val[1]

        for bb_point in bounding_box:
            if bb_point in coord_list:
                matching_keys.add(start_idx)


    matching_nums = [int_coord_map[key][0] for key in matching_keys]

    if len(matching_keys) != 2:
        return (False, matching_nums)
        
    return (True, list(matching_nums))



if __name__ == "__main__":
    path = "../inputs/day3.txt"

    with open(path) as file:
        f = file.read()

    schematic = f.split('\n')
    int_coord_map = generate_int_coord_map(schematic)

    products = []
    
    for row, line in enumerate(schematic):
        stars = find_stars(line)

        for star_idx in stars:
            bounding_box = get_bounding_box('*', (row, star_idx))
            
            gear_bool, gear_parts = is_gear(int_coord_map, bounding_box, schematic)
            
            if gear_bool:
                product = gear_parts[0] * gear_parts[1]
                products.append(product)

    print(f"Answer is: {sum(products)}")
