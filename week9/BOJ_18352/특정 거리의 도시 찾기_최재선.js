const fs = require('fs');

const [[N, M, K, X], ...roads] = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
  .map((el) => el.split(' ').map(Number));

const graph = new Array(N + 1).fill().map(() => new Set());
const visited = new Array(N + 1).fill(false);
visited[X] = true;

for (const [start, end] of roads) {
  graph[start].add(end);
}

let poses = [X];
let length = 0;

while (poses.length && length !== K) {
  const newPoses = [];

  for (const pos of poses) {
    for (const nextPos of graph[pos]) {
      if (!visited[nextPos]) {
        visited[nextPos] = true;
        newPoses.push(nextPos);
      }
    }
  }

  length += 1;
  poses = newPoses;
}

if (length !== K || !poses.length) {
  console.log(-1);
} else {
  poses.sort((a, b) => a - b);
  console.log(poses.join('\n')); 
}
