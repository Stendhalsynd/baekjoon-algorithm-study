const fs = require('fs');

const input = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim();

const [n, k] = input.split(' ').map(Number);
const MOD = 1000000000;
const dp = new Array(n + 1).fill(0);
dp[0] = 1;

let left = k;

while (left) {
  for (let i = 1; i <= n; i += 1) {
    dp[i] += dp[i - 1];
    dp[i] %= MOD;
  }

  left -= 1;
}

console.log(dp.pop());
