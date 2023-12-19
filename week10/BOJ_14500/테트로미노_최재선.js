/* eslint-disable prefer-destructuring */
const fs = require('fs');

const [nm, ...rawS] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [N, M] = nm.split(' ').map(Number);
const S = rawS.map((el) => el.split(' ').map(Number));

const rAcc = new Array(N).fill().map(() => new Array(M));
const cAcc = new Array(N).fill().map(() => new Array(M));

for (let i = 0; i < N; i += 1) {
  rAcc[i][0] = S[i][0];

  for (let j = 1; j < M; j += 1) {
    rAcc[i][j] = S[i][j] + rAcc[i][j - 1];
  }
}

for (let j = 0; j < M; j += 1) {
  cAcc[0][j] = S[0][j];

  for (let i = 1; i < N; i += 1) {
    cAcc[i][j] = S[i][j] + cAcc[i - 1][j];
  }
}

const arrMaker = (isRow, comp) => {
  const colLen = !isRow ? N - comp : N;
  const rowLen = isRow ? M - comp : M;

  const array = new Array(colLen).fill().map(() => new Array(rowLen));
  const acc = isRow ? rAcc : cAcc;

  if (isRow) {
    for (let i = 0; i < N; i += 1) {
      array[i][0] = acc[i][comp];
      for (let j = 1; j < M - comp; j += 1) {
        array[i][j] = acc[i][j + comp] - acc[i][j - 1];
      }
    }
  } else {
    for (let j = 0; j < M; j += 1) {
      array[0][j] = acc[comp][j];
      for (let i = 1; i < N - comp; i += 1) {
        array[i][j] = acc[i + comp][j] - acc[i - 1][j];
      }
    }
  }

  return array;
};

const oneByFour = arrMaker(true, 3);
const fourByOne = arrMaker(false, 3);

const twoByTwo = arrMaker(false, 1);

for (let i = 0; i < N - 1; i += 1) {
  for (let j = 0; j < M - 1; j += 1) {
    twoByTwo[i][j] += twoByTwo[i][j + 1];
  }

  twoByTwo[i].pop();
}

const twoByThree = arrMaker(true, 2);
const threeByTwo = arrMaker(false, 2);

for (let i = N - 1; i >= 1; i -= 1) {
  for (let j = 0; j < M - 2; j += 1) {
    const nums = [S[i][j], S[i - 1][j], S[i][j + 2], S[i - 1][j + 2]];
    nums.sort((a, b) => a - b);
    const min = Math.min(
      (nums[0] + nums[1]),
      (S[i][j + 1] + Math.min(S[i][j + 2], S[i][j])),
      (S[i - 1][j + 1] + Math.min(S[i - 1][j + 2], S[i - 1][j])),
    );

    twoByThree[i][j] += twoByThree[i - 1][j] - min;
  }
}

twoByThree.shift();

for (let i = 0; i < N - 2; i += 1) {
  for (let j = 0; j < M - 1; j += 1) {
    const nums = [S[i][j], S[i + 2][j], S[i][j + 1], S[i + 2][j + 1]];
    nums.sort((a, b) => a - b);
    const min = Math.min(
      (nums[0] + nums[1]),
      (S[i + 1][j] + Math.min(S[i][j], S[i + 2][j])),
      (S[i + 1][j + 1] + Math.min(S[i][j + 1], S[i + 2][j + 1])),
    );

    threeByTwo[i][j] += threeByTwo[i][j + 1] - min;
  }

  threeByTwo[i].pop();
}

console.log(Math.max(
  ...oneByFour.flat(),
  ...fourByOne.flat(),
  ...twoByTwo.flat(),
  ...twoByThree.flat(),
  ...threeByTwo.flat(),
));
