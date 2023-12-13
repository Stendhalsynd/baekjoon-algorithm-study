const fs = require('fs');

const [[N, D], ...roads] = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
  .map((el) => el.split(' ').map(Number));

const graph = new Array(D + 1).fill().map(() => new Array(D + 1).fill(Infinity));

for (const [start, end, length] of roads) {
  if (start <= D && end <= D && length < end - start) {
    graph[end][start] = Math.min(graph[end][start], length);
  }
}

const dp = new Array(D + 1);
dp[0] = 0;

for (let i = 1; i <= D; i += 1) {
  dp[i] = dp[i - 1] + 1;

  const row = graph[i];

  for (let j = 0; j < i; j += 1) {
    if (row[j] !== Infinity) {
      dp[i] = Math.min(dp[i], dp[j] + row[j]);
    }
  }
}

console.log(dp[D]);