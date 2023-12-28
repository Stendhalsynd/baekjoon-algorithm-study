/* eslint-disable no-bitwise */
const fs = require('fs');

const [rawN, ...rawInfos] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const N = Number(rawN);
const infos = rawInfos.map((el) => el.split(' ').map(Number));

let cur = (1 << N) - 1;
let min = Infinity;

while (cur) {
  let [index, multiply, plus] = [0, 1, 0];
  let copyCur = cur;

  while (copyCur) {
    if (copyCur & 1) {
      multiply *= infos[index][0];
      plus += infos[index][1];
    }

    copyCur >>= 1;
    index += 1;
  }

  min = Math.min(min, Math.abs(multiply - plus));

  cur -= 1;
}

console.log(min);