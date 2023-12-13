const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const graph = input.slice(1).map((el) => el.split(' ').map(Number));

const bfs = (colIndexes, visited, originRow) => {
  const newColIndexes = [];

  for (const colIndex of colIndexes) {
    const row = graph[colIndex];

    for (let i = 0; i < N; i += 1) {
      if (row[i] && !visited[i]) {
        originRow[i] = 1;
        newColIndexes.push(i);
        visited[i] = true;
      }
    }
  }

  if (newColIndexes.length) {
    bfs(newColIndexes, visited, originRow);
  }
};

for (let i = 0; i < N; i += 1) {
  const visited = new Array(N).fill(false);
  bfs([i], visited, graph[i]);
}

console.log(graph.map((el) => el.join(' ')).join('\n'));