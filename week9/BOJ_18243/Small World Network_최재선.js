const fs = require('fs');

const [[N, K], ...connections] = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
  .map((el) => el.split(' ').map(Number));

const graph = new Array(N).fill().map(() => new Array(N).fill(false));
const connectionGraph = new Array(N).fill().map(() => new Array(N).fill(false));
let isOverDepth = false;

for (let i = 0; i < N; i += 1) {
  for (let j = 0; j < N; j += 1) {
    if (i === j) {
      connectionGraph[i][j] = true;
    }
  }
}

for (const [x, y] of connections) {
  graph[x - 1][y - 1] = true;
  graph[y - 1][x - 1] = true;
}

const bfs = (indexes, visited, originRow, depth) => {
  if (isOverDepth) return;

  const newIndexes = [];

  for (const index of indexes) {
    const row = graph[index];

    for (let i = 0; i < N; i += 1) {
      if (row[i] && !visited[i]) {
        originRow[i] = true;
        newIndexes.push(i);
        visited[i] = true;
      }
    }
  }

  if (newIndexes.length) {
    if (depth < 6) {
      bfs(newIndexes, visited, originRow, depth + 1);
    } else {
      isOverDepth = true;
    }
  }
};

for (let i = 0; i < N; i += 1) {
  const visited = new Array(N).fill(false);
  visited[i] = true;
  bfs([i], visited, connectionGraph[i], 0);

  if (isOverDepth) break;
}

(isOverDepth || connectionGraph.map(
  (row) => row.some((el) => !el),
).some((el) => el)) ? console.log('Big World!') : console.log('Small World!');
