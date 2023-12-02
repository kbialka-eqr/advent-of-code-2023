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


def game_is_viable(game: list[list]) -> bool:
    '''Determine whether a game is viable given limits.'''
    cube_limits = {
        'blue' : 14,
        'red' : 12,
        'green' : 13
    }

    for rnd in game:
        for cube_result in rnd:
            cube_result = cube_result.strip()
            value, color = cube_result.split(' ')
            value = int(value)

            if value > cube_limits[color]:
                return False
    
    return True



if __name__ == "__main__":
    
    path = "../inputs/day2.txt"
    indices, games = parse_games(path)
    viable_indices = []

    for index, game in zip(indices, games):
        if game_is_viable(game):
            viable_indices.append(index)


    print(f"Answer is: {sum(viable_indices)}")