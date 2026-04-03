import random

# Board initialize
board = [" " for _ in range(9)]

# Function to print board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check winner
def check_winner(player):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main game loop
while True:
    print_board()
    
    # Player move
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] != " ":
        print("Position already taken!")
        continue
    board[move] = "X"
    if check_winner("X"):
        print_board()
        print("🎉 You won!")
        break
    
    # Check draw
    if " " not in board:
        print_board()
        print("It's a draw!")
        break
    
    # Computer move
    empty = [i for i, v in enumerate(board) if v == " "]
    comp_move = random.choice(empty)
    board[comp_move] = "O"
    if check_winner("O"):
        print_board()
        print("😎 Computer won!")
        break