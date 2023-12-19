const gameBoardElement = document.getElementById('gameBoard');
const rows = 6;
const columns = 7;
let currentPlayer = 'red';
let gameBoard = Array(rows).fill().map(() => Array(columns).fill(''));

// Initialize game board
for (let i = 0; i < rows * columns; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    gameBoardElement.appendChild(cell);
}

function placeChip() {
    const col = parseInt(document.getElementById('columnInput').value);
    if (isNaN(col) || col < 0 || col >= columns) {
        alert('ARE YOU STUPID OR SOMETHING PLACE IT FROM 0-6 DUMBASS');
        return;
    }

    for (let i = rows - 1; i >= 0; i--) {
        if (gameBoard[i][col] === '') {
            gameBoard[i][col] = currentPlayer;
            updateBoard();
            waitpid()
            if (checkWinner(currentPlayer)) {
                setTimeout(function() {
                    alert(`Congratulations! ${currentPlayer} wins. Click Restart game to play again.`);
                }, 100); 
            }
            currentPlayer = currentPlayer === 'red' ? 'yellow' : 'red';
            break;
        }
    }
}

function updateBoard() {
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            const cellIndex = i * columns + j;
            const cell = gameBoardElement.children[cellIndex];
            cell.classList.remove('red', 'yellow');
            if (gameBoard[i][j] === 'red') {
                cell.classList.add('red');
            } else if (gameBoard[i][j] === 'yellow') {
                cell.classList.add('yellow');
            }
        }
    }
}

function checkWinner(chip) {
    updateBoard();
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < columns - 3; c++) {
            if (gameBoard[r][c] === chip && gameBoard[r][c + 1] === chip && 
                gameBoard[r][c + 2] === chip && gameBoard[r][c + 3] === chip) {
                return true;
            }
        }
    }

    // Vertical check
    for (let r = 0; r < rows - 3; r++) {
        for (let c = 0; c < columns; c++) {
            if (gameBoard[r][c] === chip && gameBoard[r + 1][c] === chip && 
                gameBoard[r + 2][c] === chip && gameBoard[r + 3][c] === chip) {
                return true;
            }
        }
    }

    // Positive diagonal check
    for (let r = 0; r < rows - 3; r++) {
        for (let c = 0; c < columns - 3; c++) {
            if (gameBoard[r][c] === chip && gameBoard[r + 1][c + 1] === chip && 
                gameBoard[r + 2][c + 2] === chip && gameBoard[r + 3][c + 3] === chip) {
                return true;
            }
        }
    }

    // Negative diagonal check
    for (let r = 3; r < rows; r++) {
        for (let c = 0; c < columns - 3; c++) {
            if (gameBoard[r][c] === chip && gameBoard[r - 1][c + 1] === chip && 
                gameBoard[r - 2][c + 2] === chip && gameBoard[r - 3][c + 3] === chip) {
                return true;
            }
        }
    }

    return false;
}

function endGame(message) {
    document.getElementById('winnerMessage').textContent = message;
    const restartButton = document.createElement('button');
    restartButton.textContent = 'Restart Game';
    restartButton.onclick = resetGame;
    document.body.appendChild(restartButton);
}

function resetGame() {
    gameBoard = Array(rows).fill().map(() => Array(columns).fill(''));
    turnCounter = 0;
    currentPlayer = 'red';
    updateBoard();
    document.getElementById('winnerMessage').textContent = ''; // Clear the winner message
    document.body.removeChild(document.querySelector('button')); // Removes the restart button
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('restartButton').addEventListener('click', resetGame);
});
