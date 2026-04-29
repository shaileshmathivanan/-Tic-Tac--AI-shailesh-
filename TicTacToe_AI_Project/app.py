from flask import Flask, render_template, request, jsonify
from minimax import best_move as minimax_move
from alphabeta import best_move as ab_move

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    board = data["board"]
    algo = data["algo"]

    if algo == "minimax":
        move, nodes, time_taken = minimax_move(board)
    else:
        move, nodes, time_taken = ab_move(board)

    board[move] = "O"

    return jsonify({
        "board": board,
        "nodes": nodes,
        "time": time_taken
    })

if __name__ == "__main__":
    app.run(debug=True)
