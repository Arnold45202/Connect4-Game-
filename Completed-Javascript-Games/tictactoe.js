const cells = document.querySelectorAll('.cell');
let currentPlayer = 'X';

let rows = 3;
let columns = 3;
let gameBoard = Array(rows).fill().map(() => Array(columns).fill(''));

function updateGameBoard() {
    cells.forEach((cell, index) => {
        let row = Math.floor(index / 3);
        let col = index % 3;
        gameBoard[row][col] = cell.textContent;
    });
}

function checkForWinner(symbol) {
    // Check rows and columns
    for (let i = 0; i < 3; i++) {
        if (gameBoard[i].every(cell => cell === symbol) || 
            gameBoard.every(row => row[i] === symbol)) {
            setTimeout(function() {
                alert("Winner is " + symbol + ". Thanks for playing!  press restart to play again.");
            }, 100); 
            return true;
        }
    }

    // Check diagonals
    if ((gameBoard[0][0] === symbol && gameBoard[1][1] === symbol && gameBoard[2][2] === symbol) ||
        (gameBoard[0][2] === symbol && gameBoard[1][1] === symbol && gameBoard[2][0] === symbol)) {
        setTimeout(function() {
            alert("Winner is " + symbol + ". Thanks for playing! press restart to play again.");
        }, 100); 
        return true;
    }

    return false;
}

cells.forEach((cell, index) => {
    cell.addEventListener('click', () => {
        if (cell.textContent === '') {
            cell.textContent = currentPlayer;
            updateGameBoard();

            if (checkForWinner(currentPlayer)) {
                return;
            }

            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    });
});

document.getElementById('resetButton').addEventListener('click', () => {
    cells.forEach(cell => {
        cell.textContent = '';
    });
    gameBoard = Array(rows).fill().map(() => Array(columns).fill(''));
    currentPlayer = 'X';
});
