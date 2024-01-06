const fs = require('fs');

const [rawN, ...rest] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const N = Number(rawN);
const arr = rest.map((el) => el.split(' ').map(Number));
const dp = new Array(N).fill().map(() => new Array(N).fill(BigInt(0)));
dp[0][0] = BigInt(1);

for (let i = 0; i < N; i += 1) {
  for (let j = 0; j < N; j += 1) {
    if (dp[i][j]) {
      const move = arr[i][j];

      if (move) {
        if (i + move < BigInt(N)) {
          dp[i + move][j] += dp[i][j];
        }

        if (j + move < BigInt(N)) {
          dp[i][j + move] += dp[i][j];
        }
      }
    }
  }
}

console.log(dp[N - 1][N - 1].toString());
