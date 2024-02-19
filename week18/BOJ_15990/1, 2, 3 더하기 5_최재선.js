const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const nums = inputs.map(Number).slice(1);
const max = Math.max(...nums);
const dp = new Array(max + 1).fill().map(() => new Array(3).fill(0));
const MOD = 1000000009;

dp[1][0] = 1;
dp[2][1] = 1;
dp[2][0] = 0;
dp[3][2] = 1;
dp[3][1] = 1;
dp[3][0] = 1;

for (let i = 4; i <= max; i += 1) {
  for (let j = 0; j < 3; j += 1) {
    for (let k = 0; k < 3; k += 1) {
      if (k !== j) {
        dp[i][j] += dp[i - j - 1][k];
        dp[i][j] %= MOD;
      }
    }
  }

  // dp[i][0] = dp[i - 1][1] + dp[i - 1][2];
  // dp[i][1] = dp[i - 2][0] + dp[i - 2][2];
  // dp[i][2] = dp[i - 3][0] + dp[i - 3][1];
}

const sum = dp.map((arr) => arr.reduce((acc, cur) => (acc + cur) % MOD, 0));
const answers = nums.map((num) => sum[num]);
console.log(answers.join('\n'));
