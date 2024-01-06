/* eslint-disable no-bitwise */
const fs = require('fs');

const N = Number(fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim());

let result = 0;
let bucket = [N];
const memo = new Set();

while (1) {
  let isBreak = false;
  const newBucket = [];

  for (const el of bucket) {
    if (el === 1) {
      isBreak = true;
      break;
    }

    if (el % 3 === 0 && !memo.has(el / 3)) {
      newBucket.push(el / 3);
      memo.add(el / 3);
    }

    if (el % 2 === 0 && !memo.has(el / 2)) {
      newBucket.push(el / 2);
      memo.add(el / 2);
    }

    if (!memo.has(el - 1)) {
      newBucket.push(el - 1);
      memo.add(el - 1);
    }
  }

  if (isBreak) break;

  bucket = newBucket;
  result += 1;
}

console.log(result);
