/* eslint-disable no-bitwise */
const fs = require('fs');

const rawBoard = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const board = rawBoard.map((el) => el.split(' ').map(Number));
const length = 19;
const moves = [
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
];

const isNotValidPos = (i, j) => (i < 0 || i >= length || j < 0 || j >= length);

function solution() {
  const search = (i, j) => {
    const sign = board[i][j];
    if (!sign) return null;

    for (const [di, dj] of moves) {
      let isValid = true;

      for (let c = 1; c <= 4; c += 1) {
        const [mi, mj] = [i + di * c, j + dj * c];

        if (isNotValidPos(mi, mj) || board[mi][mj] !== sign) {
          isValid = false;
          break;
        }
      }

      if (isValid && (
        isNotValidPos(i + di * 5, j + dj * 5)
        || board[i + di * 5][j + dj * 5] !== sign
      ) && (
        isNotValidPos(i - di, j - dj)
        || board[i - di][j - dj] !== sign
      )) {
        return [sign, `${i + 1} ${j + 1}`];
      }
    }

    return null;
  };

  for (let i = 0; i < length; i += 1) {
    for (let j = 0; j < length; j += 1) {
      const searchResult = search(i, j);
      if (searchResult) return searchResult;
    }
  }

  return null;
}

const result = solution();
console.log(result ? result.join('\n') : 0);
