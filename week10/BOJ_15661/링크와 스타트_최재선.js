/* eslint-disable no-bitwise */
const fs = require('fs');

const [rawN, ...rawS] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const N = Number(rawN);
const S = rawS.map((el) => el.split(' ').map(Number));

const keys = [];
const values = [];

for (let i = 0; i < N; i += 1) {
  for (let j = i + 1; j < N; j += 1) {
    const key = (1 << i) + (1 << j);
    const value = S[i][j] + S[j][i];

    keys.push(key);
    values.push(value);
  }
}

const first = 1 << (N - 1);
let min = Infinity;
let start = (1 << N) - 1;

const getDiff = (num) => {
  let [sum1, sum2] = [0, 0];

  for (let i = 0; i < keys.length; i += 1) {
    if (num & keys[i]) sum1 += values[i];
    if (~num & keys[i]) sum2 += values[i];
  }

  return Math.abs(sum1 - sum2);
};

while ((start & first) && min) {
  min = Math.min(min, getDiff(start));

  start -= 1;
}

console.log(min);
