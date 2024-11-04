def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
            
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
            
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
        
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def move(board, player):
    # Board mit zahlen füllen.
    winning_lines = [[0 for _ in range(3)] for _ in range(3)]

    # check rows
    for row_index in range(3):
        if all(board[row_index][coll_index] == player or board[row_index][coll_index] == " " for coll_index in range(3)):
            for coll_index in range(3):
                winning_lines[row_index][coll_index] += 1

    # check columns
    for coll_index in range(3):
        if all(board[row_index][coll_index] == player or board[row_index][coll_index] == " " for row_index in range(3)):
            for row_index in range(3):
                winning_lines[row_index][coll_index] += 1

    # check diagonals
    if all(board[index][index] == player or board[index][index] == " " for index in range(3)):
           for index in range(3):
                winning_lines[index][index] += 1
    if all(board[index][2-index] == player or board[index][2-index] == " " for index in range(3)):
           for index in range(3):
                winning_lines[index][2-index] += 1

    # find position with maximum winning lines
    row_index_max = 0
    coll_index_max = 0
    max = 0
    for row_index in range(3):
        for coll_index in range(3):
            if winning_lines[row_index][coll_index]>max:
                max = winning_lines[row_index][coll_index]
                row_index_max = row_index
                coll_index_max = coll_index

    return row_index_max, coll_index_max, max

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Best move
        row, coll, max = move(board, current_player)
        print(f"Best move is row {row} coll {coll} with {max} winning lines.")

        # Get player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers between 0 and 2.")
        
        # Make move
        board[row][col] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
            
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"

play_game()