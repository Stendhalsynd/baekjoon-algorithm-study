const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = Number(inputs[0]);
const p = inputs[1].split(' ').map(Number);
const dp = [...p];

const getMax = (index) => {
  let max = 0;

  for (let i = 0; i < index; i += 1) {
    max = Math.max(max, dp[i] + dp[index - 1 - i]);
  }

  return max;
};

for (let i = 1; i < n; i += 1) {
  dp[i] = Math.max(dp[i], getMax(i));
}

console.log(dp.pop());
