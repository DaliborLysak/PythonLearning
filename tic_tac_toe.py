'''
Simple tic tac toe game for 2 players
'''

def print_matrix(matrix):
    '''
    shows matrix
    '''
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

def print_coordinates():
    '''
    shows game coordinates
    '''
    print("Game coordinates")
    print_matrix([[7,8,9],[4,5,6],[1,2,3]])

def print_state(game):
    '''
    shows game state
    '''
    print("Game state:")
    print_matrix([list(game.values())[6:9], list(game.values())[3:6], list(game.values())[0:3]])

def print_game(game):
    '''
    shows game state
    '''
    print_coordinates()
    print("")
    print_state(game)

def occupied(game, coordinates):
    '''
    detect cell occupation
    '''
    return game[coordinates] != symbols[2]

def get_input_value():
    '''
    reads input
    '''
    return input("Please, enter coordinates (1-9):")

def get_input(game):
    '''
    input validation
    '''
    coordinates = 0

    while coordinates == 0:
        value = get_input_value()

        if not value.isdigit():
            print("Not a number, try again")
            continue

        coordinates = int(value)
        if coordinates not in allowed_coordinates or occupied(game, coordinates):
            print("Not allowed number (1-9), try again")
            coordinates = 0
            continue

    return coordinates

def set_coordinates(game, coordinates):
    '''
    sets coordinates
    '''
    game[coordinates] = symbols[active_player]

def switch_player(player):
    '''
    player switching
    '''
    return 0 if player == 1 else 1

def check(game, coordinates, step, max_coordinates):
    '''
    checks game state
    
    '''
    value = game[coordinates]
    actual_step = coordinates + step
    while actual_step <= max_coordinates:
        if value == game[actual_step]:
            actual_step = actual_step + step
        else:
            return False

    return value != symbols[2]

def check_diagonals(game):
    '''
    checks daigonals state
    '''
    return check(game, 1, 4, 9) or check(game, 3, 2, 7)

def check_rows(game):
    '''
    checks rows state
    '''
    return check(game, 1, 1, 3) or check(game, 4, 1, 6) or check(game, 7, 1, 9)

def check_columns(game):
    '''
    checks columns state
    '''
    return check(game, 1, 3, 7) or check(game, 2, 3, 8) or check(game, 3, 3, 9)

def end_of_game(game):
    '''
    check game state
    '''
    return check_diagonals(game) or check_rows(game) or check_columns(game)

allowed_coordinates = range(1,10)
players = ["Player 1 [X]", "Player 2 [O]"]
symbols = ["X", "O", " "]
active_player = 0
active_game = {}

print("Welcome in Tic Tac Toe game")
for i in allowed_coordinates:
    active_game[i] = symbols[2]

# print(active_game)
# print_state(active_game)
# print(list(active_game.values())[6:9])

while not end_of_game(active_game):
    print_game(active_game)
    print(players[active_player])
    set_coordinates(active_game, get_input(active_game))
    active_player = switch_player(active_player)

winner = switch_player(active_player)
print_state(active_game)
print(f"Winner is: {players[winner]}")
