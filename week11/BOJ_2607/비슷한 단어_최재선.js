/* eslint-disable no-bitwise */
const fs = require('fs');

const [_, ...rest] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [targetStr, ...restStrs] = rest;
const targetMemo = new Array(26).fill(0);

let result = 0;

const checkIsSimilar = (arr) => {
  let targetCounts = 0;
  let arrCounts = 0;

  for (let i = 0; i < 26; i += 1) {
    if (targetMemo[i] !== arr[i]) {
      const diff = Math.abs(targetMemo[i] - arr[i]);

      if (arr[i] > targetMemo[i]) arrCounts += diff;
      else targetCounts += 1;

      if (targetCounts >= 2 || arrCounts >= 2) return false;
    }
  }

  return true;
};

for (let i = 0; i < targetStr.length; i += 1) {
  targetMemo[targetStr[i].charCodeAt() - 65] += 1;
}

for (let i = 0; i < restStrs.length; i += 1) {
  const str = restStrs[i];
  const strMemo = new Array(26).fill(0);

  for (let j = 0; j < str.length; j += 1) {
    strMemo[str[j].charCodeAt() - 65] += 1;
  }

  const isSimilar = checkIsSimilar(strMemo);

  if (isSimilar) result += 1;
}

console.log(result);
