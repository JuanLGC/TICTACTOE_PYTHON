current_player = "X"
position_played = ""
turn = 1
stop = False
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]

def play(position):
    if turn % 2 == 0:
        current_player = "X"
    else:
        current_player = "O"

    board[position] = current_player


def check_for_winner():
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for i in lines:
        [a, b, c] = i
        if board[a] != "-" and board[b] != "-" and board[c] != "-":   
            if board[a] == board[b] and board[a] == board[c]:
                print('YOU WON YOU SALAMAN BITCH')
                turn = 0
                new_game()
            else:
                return False    
    return False
    

def new_game():
    current_player ="X"
    for i in range(len(board)):
        board[i] = "-"
    print_board()
    

def print_board():
    if turn % 2 == 0:
        current_player = "O"
    else:
        current_player = "X"
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)

while stop == False:
    command = input("What do you want?: ")
    
    if command == "stop":
        stop = True
    elif "play" in command :
        position_played = int(command[len(command) - 1]) - 1
        if board[position_played] != "-":
            print_board() 
            print("This position is already taken, idiot... Try again!!")
        else:
            turn = turn + 1
            play(position_played)
            print_board()
            check_for_winner() 
    elif command == "reset":
        new_game()
