def print_matrix(matrix):
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

def print_coordinates():
    print("Game coordinates")
    print_matrix([[7,8,9],[4,5,6],[1,2,3]])

def print_state(game):
    print("Game state:")
    print_matrix([list(game.values())[6:9], list(game.values())[3:6], list(game.values())[0:3]])

def print_game(game):
    print_coordinates()
    print("")
    print_state(game)

def occupied(coordinates):
     return game[coordinates] != symbols[2]

def get_input_value():
    return input("Please, enter coordinates (1-9):")

def get_input():
    coordinates = 0

    while coordinates == 0:
        value = get_input_value()

        if not value.isdigit():
            print("Not a number, try again")
            continue
            
        coordinates = int(value)
        if coordinates not in allowed_coordinates or occupied(coordinates):
            print("Not allowed number (1-9), try again")
            coordinates = 0
            continue

    return coordinates

def setCoordinates(coordinates):
     game[coordinates] = symbols[activePlayer]
     

def switch_player(activePlayer):
     return 0 if activePlayer == 1 else 1 

def check(game, coordinates, step, maxCoordinates):
     value = game[coordinates]
     actualStep = coordinates + step
     while actualStep <= maxCoordinates:
         if value == game[actualStep]:
             actualStep = actualStep + step
         else:
             return False

     return value != symbols[2]

def check_diagonals(game):
     return check(game, 1, 4, 9) or check(game, 3, 2, 7)
          
def check_rows(game):
    return check(game, 1, 1, 3) or check(game, 4, 1, 6) or check(game, 7, 1, 9)

def check_columns(game):
    return check(game, 1, 3, 7) or check(game, 2, 3, 8) or check(game, 3, 3, 9)

def end_of_game(game):
     return check_diagonals(game) or check_rows(game) or check_columns(game)

allowed_coordinates = range(1,10)
number_of_rows = 0
number_of_columns = 0
players = ["Player 1 [X]", "Player 2 [O]"]
symbols = ["X", "O", " "]
activePlayer = 0
game = {}

print("Welcome in Tic Tac Toe game")
for i in allowed_coordinates:
     game[i] = symbols[2]

# print(game)
# print_state(game)
# print(list(game.values())[6:9])

while not end_of_game(game):
     print_game(game)
     print(players[activePlayer])
     setCoordinates(get_input())
     activePlayer = switch_player(activePlayer)

winner = switch_player(activePlayer)
print_state(game)
print(f"Winner is: {players[winner]}")

