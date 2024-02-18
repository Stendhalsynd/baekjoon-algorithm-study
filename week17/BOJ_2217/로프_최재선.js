/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = Number(inputs[0]);
const ropes = inputs.slice(1).map(Number).sort((a, b) => a - b);
let max = 0;

for (let i = 0; i < n; i += 1) {
  const multiply = n - i;
  max = Math.max(max, ropes[i] * multiply);
}

console.log(max);
