import random
from copy import deepcopy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# BFS move selection for the computer
def bfs_move(board, player):
    queue = [(deepcopy(board), [])]  # Queue stores (current board, moves taken to reach this state)
    while queue:
        state, moves = queue.pop(0)  # Dequeue the first element
        if check_win(state, player):
            return moves[0]  # Return the first move if a winning path is found
        # Explore all possible moves
        for r in range(3):
            for c in range(3):
                if state[r][c] == " ":
                    new_state = deepcopy(state)
                    new_state[r][c] = player
                    queue.append((new_state, moves + [(r, c)]))
    return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])

# DFS move selection for the computer
def dfs_move(board, player, depth=0, max_depth=5):
    stack = [(deepcopy(board), [])]  # Stack stores (current board, moves taken to reach this state)
    while stack:
        state, moves = stack.pop()  # Pop the last element
        if check_win(state, player):
            return moves[0]  # Return the first move if a winning path is found
        # Limit depth to avoid endless search
        if depth < max_depth:
            for r in range(3):
                for c in range(3):
                    if state[r][c] == " ":
                        new_state = deepcopy(state)
                        new_state[r][c] = player
                        stack.append((new_state, moves + [(r, c)]))
                        depth += 1
    return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])

# Uniform Cost Search move selection for the computer
def ucs_move(board, player):
    moves = [(0, deepcopy(board), [])]  # Priority queue with (cost, current board, moves)
    while moves:
        cost, state, path = moves.pop(0)
        if check_win(state, player):
            return path[0]
        for r in range(3):
            for c in range(3):
                if state[r][c] == " ":
                    new_state = deepcopy(state)
                    new_state[r][c] = player
                    new_cost = cost + 1
                    moves.append((new_cost, new_state, path + [(r, c)]))
        moves.sort()  # Sort by cost
    return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])

# Iterative Deepening Search for the computer
def ids_move(board, player, max_depth=5):
    for depth in range(1, max_depth + 1):
        result = dfs_move(board, player, depth, depth)
        if result:
            return result
    return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move as 'row col' (0, 1, or 2): ").split())
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
    play_game("bfs")
