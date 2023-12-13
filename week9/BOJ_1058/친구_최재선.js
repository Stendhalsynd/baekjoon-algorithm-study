const fs = require('fs');

const [rawN, ...rawConnections] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const availableDepth = 2;
const N = Number(rawN);
const connections = rawConnections.map((el) => el.split(''));
let maxCount = 0;

const bfs = (indexes, visited, depth) => {
  if (depth > availableDepth || !indexes.length) return 0;

  const newIndexes = [];

  for (const index of indexes) {
    const row = connections[index];

    for (let i = 0; i < N; i += 1) {
      if (row[i] === 'Y' && !visited[i]) {
        visited[i] = true;
        newIndexes.push(i);
      }
    }
  }

  return newIndexes.length + bfs(newIndexes, visited, depth + 1);
};

for (let i = 0; i < N; i += 1) {
  const visited = new Array(N).fill(false);
  visited[i] = true;
  maxCount = Math.max(maxCount, bfs([i], visited, 1));
}

console.log(maxCount);
