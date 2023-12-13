const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, K] = input[0].split(' ').map(Number);

const visit = (pos, queue, visited) => {
  visited[pos] = true;
  queue.push(pos);
};

if (N >= K) {
  console.log(N - K);
} else {
  const maxSize = K * 2 + 1;
  const visited = new Array(maxSize).fill(false);

  let result = 0;
  let queue = [N];
  visited[N] = true;

  while (queue.length) {
    const newQueue = [];
    let isBreak = false;

    for (const pos of queue) {
      if (pos === K) {
        isBreak = true;
        break;
      }

      if (pos !== 0) {
        let posCache = pos * 2;

        while (posCache < maxSize) {
          if (!visited[posCache]) {
            visit(posCache, queue, visited);
          }

          posCache *= 2;
        }
      }
    }

    for (const pos of queue) {
      if (pos + 1 < maxSize && !visited[pos + 1]) {
        visit(pos + 1, newQueue, visited);
      }

      if (pos - 1 >= 0 && !visited[pos - 1]) {
        visit(pos - 1, newQueue, visited);
      }
    }

    if (isBreak) break;

    result += 1;

    queue = newQueue;
  }

  console.log(result);
}