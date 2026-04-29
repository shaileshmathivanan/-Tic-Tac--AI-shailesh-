EMPTY = " "
PLAYER = "X"
AI = "O"

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != EMPTY:
            return board[w[0]]

    if EMPTY not in board:
        return "Draw"

    return None
