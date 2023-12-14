/* eslint-disable no-param-reassign */
/* eslint-disable no-bitwise */
const fs = require('fs');

const input = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number);

if (N >= K) {
  console.log(N - K);
} else {
  let result = 0;

  if (N === 0) {
    result += 1;
    N += 1;
  }

  const getCount = (num, length) => {
    let count = 0;

    const prefix = num >> (length - 1);

    count += prefix;

    num ^= (prefix << (length - 1));

    while (num) {
      while (!(num & 1)) {
        num >>= 1;
      }

      if ((num & 2)) {
        num += 1;
      }

      num >>= 2;
      count += 1;
    }

    return count;
  };

  let length = 1;
  while (N < K) {
    length += 1;
    N <<= 1;
  }

  const num1 = N - K;
  const num2 = K - (N >> 1);

  const count1 = getCount(num1, length);
  const count2 = getCount(num2, length - 1);

  console.log(result + Math.min(count1, count2));
}
