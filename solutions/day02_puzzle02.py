def parse_games(input_path: str) -> tuple[list, list]:
    '''Parse input into list of indices and list of results
    
    Where a game results is a list of rounds and a round is a list of strings
    representing cube counts like " 3 blue".
    '''
    with open(input_path) as file:
        f = file.read()

    games = f.split('\n')

    indices = []
    game_results = []

    for game in games:

        game_name, game_result = game.split(':')
        indices.append(int(game_name.split(' ')[-1]))
        rounds = game_result.split(';')
        rounds = [round.split(',') for round in rounds]
        game_results.append(rounds)

    return indices, game_results


def determine_fewest(game: list[list]) -> dict:
    '''Process each game determining fewest cubes necessary to complete.'''

    # Stores max cube count needed per color to complete all rounds
    maxes = {
        'red' : 0,
        'blue' : 0,
        'green' : 0
    }
    
    for rnd in game:
        # round is a list of strings w/poor spacing
        for cube_result in rnd:
            cube_result = cube_result.strip()
            value, color = cube_result.split(' ')
            value = int(value)

            if value > maxes[color]:
                maxes[color] = value

    return maxes


if __name__ == "__main__":
    path = "../inputs/day2.txt"
    indices, game_res = parse_games(path)

    products = []

    for game in game_res:

        fewest = determine_fewest(game)
        product = fewest['red'] * fewest['blue'] * fewest['green']
        products.append(product)

    print(f"Answer is: {sum(products)}")
