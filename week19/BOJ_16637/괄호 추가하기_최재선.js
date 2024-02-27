/* eslint-disable no-multi-assign */
/* eslint-disable no-shadow */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = +inputs[0];
const exp = inputs[1];

if (n === 1) {
  console.log(exp);
} else {
  const calculator = (n, symbol, m) => {
    if (symbol === '+') return n + m;
    if (symbol === '*') return n * m;
    if (symbol === '-') return n - m;

    return null;
  };

  const dp = new Array((n + 1) / 2).fill().map(() => [-Infinity, Infinity]);
  dp[0][0] = dp[0][1] = Number(exp[0]);
  dp[1][0] = dp[1][1] = calculator(Number(exp[0]), exp[1], Number(exp[2]));

  for (let i = 1; i < ((n - 1) / 2); i += 1) {
    const index = (i * 2) + 1;
    const symbol = exp[index];
    const num = Number(exp[index + 1]);

    const left1 = calculator(
      dp[i][0],
      symbol,
      num,
    );

    const left2 = calculator(
      dp[i][1],
      symbol,
      num,
    );

    const partSum = calculator(
      Number(exp[index - 1]),
      symbol,
      num,
    );

    const right1 = calculator(
      dp[i - 1][0],
      exp[index - 2],
      partSum,
    );

    const right2 = calculator(
      dp[i - 1][1],
      exp[index - 2],
      partSum,
    );

    dp[i + 1][0] = Math.max(dp[i + 1][0], left1, left2, right1, right2);
    dp[i + 1][1] = Math.min(dp[i + 1][1], left1, left2, right1, right2);
  }

  console.log(dp.pop()[0]);
}
