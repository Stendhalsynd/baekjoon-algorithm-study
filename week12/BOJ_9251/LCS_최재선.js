const fs = require('fs');

const [str1, str2] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const dp = new Array(str1.length).fill().map(() => new Array(str2.length).fill(0));

for (let i = 0; i < str1.length; i += 1) {
  for (let j = 0; j < str2.length; j += 1) {
    if (str1[i] === str2[j]) dp[i][j] += 1;
  }
}

for (let i = 0; i < str1.length - 1; i += 1) {
  let max = 0;

  for (let j = 0; j < str2.length; j += 1) {
    dp[i + 1][j] = Math.max(dp[i][j], max + dp[i + 1][j]);
    max = Math.max(max, dp[i][j]);
  }
}

let result = 0;

for (let i = 0; i < str2.length; i += 1) {
  if (result < dp[dp.length - 1][i]) result = dp[dp.length - 1][i];
}

console.log(result);
