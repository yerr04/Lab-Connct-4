# This will take in the num_row and num_cols from user input and this will set each spot in the list to “-”. A 2D character
# list with each spot set to be “-” will be returned.
def initialize_board(num_rows, num_cols):
    board = []
    for row in range(num_rows):
        board.append([])
        for col in range(num_cols):
            board[row].append("-")
    return board

# This will take in the 2D character list for the board and print the board.
def print_board(board):
    for i in board:
        i = " ".join(i)
        print(i)

# This will take in the 2D character list for the board. This function places the token (‘x’ or ‘o’ denoted as ‘chip_type’) in the
# column that the user has chosen. Will find the next available spot in that column if there are already tokens there. The row
# that the token is placed in is returned.
def insert_chip(board, col, chip_type):
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row

# This will take in the 2D character list for the board. After a token is added, checks whether the token in this location, of
# the specified chip type, creates four in a row. Will return True if someone won, and False otherwise.
def check_if_winner(board, col, row, chip_type):
    # Check horizontal
    for i in range(len(board[0]) - 3):
        if board[row][i] == chip_type and board[row][i + 1] == chip_type and board[row][i + 2] == chip_type and board[row][i + 3] == chip_type:
            return True
    # Check vertical
    for i in range(len(board) - 3):
        if board[i][col] == chip_type and board[i + 1][col] == chip_type and board[i + 2][col] == chip_type and board[i + 3][col] == chip_type:
            return True
    return False


# main method
def main():
    num_rows = int(input("What would you like the height of the board to be?: "))
    num_cols = int(input("What would you like the width of the board to be?: "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    # Game loop
    while True:
        # Player 1
        p1_input = int(input("Player 1: Which column would you like to choose?:"))
        insert_chip(board, p1_input - 1, "x")
        print_board(board)
        p1_input = p1_input - 1
        # Check if player 1 won
        if check_if_winner(board, p1_input, insert_chip(board, p1_input, "x"), "x"):
            print("Player 1 won!")
            break

        # Player 2
        p2_input = int(input("Player 2: Which column would you like to choose?" ))
        insert_chip(board, p2_input - 1, "o")
        print_board(board)

        # Check if player 2 won
        if check_if_winner(board, p2_input, insert_chip(board, p2_input, "o"), "o"):
            print("Player 2 won!")
            break

if __name__ == "__main__":
    main()
