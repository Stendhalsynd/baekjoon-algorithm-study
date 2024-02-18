/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = BigInt(inputs[0]);
const roadLengthes = inputs[1].split(' ').map((el) => BigInt(el));
const oilCosts = inputs[2].split(' ').map((el) => BigInt(el));

let min = BigInt(1000000001);
let sum = BigInt(0);

for (let i = BigInt(0); i < n - BigInt(1); i += BigInt(1)) {
  if (min > oilCosts[i]) {
    min = oilCosts[i];
  }

  sum += min * roadLengthes[i];
}

console.log(sum.toString());
