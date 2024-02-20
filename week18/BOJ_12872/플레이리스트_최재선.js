/* eslint-disable no-shadow */
/* eslint-disable no-param-reassign */
const fs = require('fs');

const input = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim();

const [n, m, p] = input.split(' ').map((el) => BigInt(el));
const dp = new Array(Number(n) + 1).fill(BigInt(0));
const MOD = BigInt(1000000007);

const getFactorial = (x) => {
  let result = BigInt(1);
  while (x !== BigInt(1)) {
    result *= x;
    x -= BigInt(1);
  }

  return result;
};

const combination = (x, y) => (getFactorial(x) / getFactorial(x - y) / getFactorial(y));

const f = (n, m, p) => {
  if (n <= m) {
    if (n === p) return getFactorial(n);
    return BigInt(0);
  }

  return (getFactorial(n) / getFactorial(n - m)) * (n - m) ** (p - m);
};

for (let i = m; i <= n; i += BigInt(1)) {
  dp[i] = f(i, m, p);

  for (let j = BigInt(1); j < i; j += BigInt(1)) {
    dp[i] -= (combination(i, j) * dp[j]) % MOD;
  }

  dp[i] %= MOD;
}

console.log(dp.pop().toString());
