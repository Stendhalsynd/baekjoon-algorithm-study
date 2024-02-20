/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const n = Number(inputs[0]);
const infos = inputs.slice(1).map((el) => el.split(' ').map(Number));
const flatInfos = infos.flat();
const compressed = [...new Set(flatInfos)].sort((a, b) => a - b);
const map = new Map();

for (let i = 0; i < compressed.length; i += 1) {
  map.set(compressed[i], i);
}

const dp = new Array(compressed.length + 1).fill(0);

for (const [s, t] of infos) {
  dp[map.get(s)] += 1;
  dp[map.get(t)] -= 1;
}

for (let i = 1; i < dp.length; i += 1) {
  dp[i] += dp[i - 1];
}

console.log(Math.max(...dp));
