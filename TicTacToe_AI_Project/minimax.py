import time
from game import check_winner, EMPTY, PLAYER, AI

nodes = 0

def minimax(board, is_max):
    global nodes
    nodes += 1

    result = check_winner(board)
    if result == AI:
        return 1
    elif result == PLAYER:
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, False))
                board[i] = EMPTY
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                best = min(best, minimax(board, True))
                board[i] = EMPTY
        return best

def best_move(board):
    global nodes
    nodes = 0
    start = time.time()

    best_val = -100
    move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            val = minimax(board, False)
            board[i] = EMPTY
            if val > best_val:
                best_val = val
                move = i

    end = time.time()
    return move, nodes, end - start
