const fs = require('fs');

const [rawN, rawArr] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const N = Number(rawN);
const arr = rawArr.split(' ').map(Number);
const dp = new Array(1001).fill(0);
const bucket = new Set();

for (let i = 0; i < N; i += 1) {
  dp[arr[i]] = Math.max(dp[arr[i]], arr[i]);

  for (const num of bucket) {
    if (num < arr[i]) {
      const sum = dp[num] + arr[i];

      dp[arr[i]] = Math.max(dp[arr[i]], sum);
    }
  }

  bucket.add(arr[i]);
}

console.log(Math.max(...dp));
