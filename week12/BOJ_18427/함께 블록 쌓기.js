const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [N, M, H] = inputs[0].split(' ').map(Number);
const blockGroups = inputs.slice(1).map((el) => el.split(' ').map(Number));

const dp = new Array(H + 1).fill(0);
dp[0] += 1;

for (let i = 0; i < N; i += 1) {
  const blockGroup = blockGroups[i];

  for (let j = H; j >= 0; j -= 1) {
    for (let k = 0; k < blockGroup.length; k += 1) {
      if (dp[j] && ((j + blockGroup[k]) <= H)) {
        dp[j + blockGroup[k]] += dp[j];
        dp[j + blockGroup[k]] %= 10007;
      }
    }
  }
}

console.log(dp[H]);