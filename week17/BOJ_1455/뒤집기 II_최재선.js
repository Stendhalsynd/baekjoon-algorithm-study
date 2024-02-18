/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const [n, m] = inputs[0].split(' ').map(Number);
const board = inputs.slice(1).map((el) => el.split('').map(Number));

let count = 0;

const reverse = (a, b) => {
  for (let i = 0; i <= a; i += 1) {
    for (let j = 0; j <= b; j += 1) {
      board[i][j] = !board[i][j];
    }
  }
};

for (let i = n - 1; i >= 0; i -= 1) {
  for (let j = m - 1; j >= 0; j -= 1) {
    if (board[i][j]) {
      reverse(i, j);
      count += 1;
    }
  }
}

console.log(count);
