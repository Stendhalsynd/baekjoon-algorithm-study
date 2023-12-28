const fs = require('fs');

const [nm, ...rawDNAs] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [N, M] = nm.split(' ').map(Number);
const DNAs = rawDNAs.map((el) => el.split(''));
const chars = ['A', 'C', 'G', 'T'];
const result = ['', 0];

for (let j = 0; j < M; j += 1) {
  const count = new Array(4).fill(0); // A, C, G, T

  for (let i = 0; i < N; i += 1) {
    const char = DNAs[i][j];

    if (char === 'A') count[0] += 1;
    else if (char === 'C') count[1] += 1;
    else if (char === 'G') count[2] += 1;
    else if (char === 'T') count[3] += 1;
  }

  const max = Math.max(...count);
  const maxIndex = count.findIndex((el) => el === max);
  result[0] += chars[maxIndex];
  result[1] += (N - max);
}

console.log(result.join('\n'));