const fs = require('fs');

const input = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim();

const n = Number(input);
const MOD = 10007;

const dp = new Array(n + 1).fill(0);
dp[1] = 1;
dp[2] = 3;

for (let i = 3; i <= n; i += 1) {
  dp[i] = (dp[i - 1] + dp[i - 2] * 2) % MOD;
}

console.log(dp[n]);
