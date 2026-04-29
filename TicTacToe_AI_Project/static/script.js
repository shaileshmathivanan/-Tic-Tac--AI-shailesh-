let board = Array(9).fill("");

function drawBoard() {
    const div = document.getElementById("board");
    div.innerHTML = "";
    board.forEach((cell, i) => {
        let btn = document.createElement("button");
        btn.innerText = cell;
        btn.onclick = () => playerMove(i);
        div.appendChild(btn);
    });
}

function playerMove(i) {
    if (board[i] === "") {
        board[i] = "X";
        fetch("/move", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({board: board, algo: document.getElementById("algo").value})
        })
        .then(res => res.json())
        .then(data => {
            board = data.board;
            drawBoard();
            document.getElementById("stats").innerText =
                `Nodes: ${data.nodes}, Time: ${data.time.toFixed(5)}s`;
        });
    }
}
drawBoard();
