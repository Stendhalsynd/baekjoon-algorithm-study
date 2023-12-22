const fs = require('fs');
const [rawN, ...rawS] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(rawN);
const S = rawS.map((el) => el.split(' ').map(Number));

const keyValues = [];

for (let i = 0; i < N; i += 1) {
  for (let j = i + 1; j < N; j += 1) {
    keyValues.push((1 << i) | (1 << j), S[i][j] + S[j][i]);
  }
}

const first = 1 << (N - 1);
let min = 38000;
let start = (1 << N) - 1;

const getDiff = (num) => {
  let diff = 0;

  for (let i = 0; i < keyValues.length; i += 2) {
    const flag = num & keyValues[i];
    if (flag === keyValues[i]) diff += keyValues[i + 1];
    else if (!flag) diff -= keyValues[i + 1];
  }

  return Math.abs(diff);
};

while ((start & first) && min) {
  min = Math.min(min, getDiff(start));

  start -= 1;
}

console.log(min);