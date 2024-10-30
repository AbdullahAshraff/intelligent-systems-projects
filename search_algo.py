import random
from copy import deepcopy


random_move = lambda board: random.choice(
    [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
)


def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    return all(cell != " " for row in board for cell in row)


# Breadth First Search
def bfs_move(board, player):
    queue = [(deepcopy(board), [])]
    while queue:
        state, moves = queue.pop(0)
        if check_win(state, player):
            return moves[0]
        for r in range(3):
            for c in range(3):
                if state[r][c] == " ":
                    new_state = deepcopy(state)
                    new_state[r][c] = player
                    queue.append((new_state, moves + [(r, c)]))
                    # print('this is the queue:\n\n',queue)
    return random_move(board)


# Depth First Search
def dfs_move(board, player, depth=0, max_depth=5):
    stack = [(deepcopy(board), [])]
    while stack:
        state, moves = stack.pop()
        if check_win(state, player):
            return moves[0]
        if depth < max_depth:  # Limit depth to avoid endless search
            for r in range(3):
                for c in range(3):
                    if state[r][c] == " ":
                        new_state = deepcopy(state)
                        new_state[r][c] = player
                        stack.append((new_state, moves + [(r, c)]))
                        depth += 1
    return random_move(board)


# Uniform Cost Search
def ucs_move(board, player):
    moves = [(0, deepcopy(board), [])]
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
        moves.sort(key=lambda x: x[0])  # Sort by cost
    return random_move(board)


# Iterative Deepening Search
def ids_move(board, player, max_depth=5):
    for depth in range(1, max_depth + 1):
        result = dfs_move(board, player, depth, depth)
        if result:
            return result
    return random_move(board)
