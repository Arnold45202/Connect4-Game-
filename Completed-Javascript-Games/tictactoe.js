const cells = document.querySelectorAll('.cell');
let currentPlayer = 'X';

let rows = 3;
let columns = 3;

let gameBoard = Array(rows).fill().map(() => Array(columns).fill(''));

cells.forEach(cell => {
    cell.addEventListener('click', () => {
        if (cell.textContent === '') {
            cell.textContent = currentPlayer;
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    });
});

document.getElementById('resetButton').addEventListener('click', () => {
    cells.forEach(cell => {
        cell.textContent = '';
    });
    currentPlayer = 'X';
});

// function checkForWinner(symbol) {
//     let i = 0
//     while (i < 3) {
//         if (gameBoard[0][i] == symbol && gameBoard[1][i] == symbol && gameBoard[2][i] == symbol){
//             alert("Winner is ", symbol, "ty for playing !!")
//             return True
//         }
//         if (gameBoard[i][0] == symbol && gameBoard[i][1] == symbol && gameBoard[i][2] == symbol) {
//             alert("Winner is ", symbol, "ty for playing !!")
//             return True
//         }
//         i++;
//     }

//     if (gameBoard[0][0] == symbol && gameBoard[1][1] == symbol && gameBoard[2][2] == symbol):
//         alert("Winner is ", symbol, "ty for playing !!")
//         return True
    
//     if (gameBoard[0][2] == symbol && gameBoard[1][1] == symbol && gameBoard[2][0]) {
//         alert("Winner is ", symbol, "ty for playing !!")
//         return True
//     }
// }
