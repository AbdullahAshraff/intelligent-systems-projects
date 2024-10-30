from search_algo import bfs_move, dfs_move, ucs_move, ids_move, check_win, check_draw, random_move


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def player_move(board):
    while True:
        try:
            row, col = map(
                int, input("Enter your move as 'row col' (0, 1, or 2): ").split()
            )
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell is already taken. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers (0, 1, or 2).")


def play_game(search_method="bfs"):
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and the computer is 'O'.")

    while True:
        print_board(board)

        # Player's turn
        player_move(board)
        if check_win(board, "X"):
            print_board(board)
            print("Congratulations! You won.")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer's turn with chosen search method
        if search_method == "bfs":
            move = bfs_move(board, "O")
        elif search_method == "dfs":
            move = dfs_move(board, "O")
        elif search_method == "ucs":
            move = ucs_move(board, "O")
        elif search_method == "ids":
            move = ids_move(board, "O")

        board[move[0]][move[1]] = "O"
        print(f"Computer chose {move}")

        if check_win(board, "O"):
            print_board(board)
            print("Computer won. Better luck next time!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game("ids")
