# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def check_full():
    return ' ' not in board

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    current_player = 'X'
    while True:
        print("Player " + current_player + "'s turn.")
        position = int(input("Enter a position (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = current_player
            print_board()
            if check_win(current_player):
                print("Player " + current_player + " wins!")
                break
            if check_full():
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
