/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = Number(inputs[0]);
const infos = inputs.slice(1).map((el) => el.split(' ').map(Number));
infos.sort((a, b) => a[0] - b[0]);
const total = infos.reduce((acc, cur) => acc + cur[1], 0);

let pos = null;
let sum = 0;

for (const [a, b] of infos) {
  sum += b;

  if ((total / 2) <= sum) {
    pos = a;
    break;
  }
}

console.log(pos);
