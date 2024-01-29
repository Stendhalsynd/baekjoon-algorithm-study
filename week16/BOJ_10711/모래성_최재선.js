/* eslint-disable no-shadow */
const fs = require('fs');

const [nm, ...rest] = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : 'dev/stdin')
  .toString().trim().split('\n');

const [n, m] = nm.split(' ').map(Number);
const states = rest.map((el) => el.split('').map((el) => (el === '.' ? 0 : Number(el))));
const dif = [-1, 0, 1];

let queue = [];

const pushQueue = (i, j) => {
  queue.push([i, j]);
};

for (let i = 0; i < n; i += 1) {
  for (let j = 0; j < m; j += 1) {
    if (!states[i][j]) pushQueue(i, j);
  }
}

let result = 0;

const isValidPos = (i, j) => i < n && i >= 0 && j < m && j >= 0;

const processPoses = (existQueue, newQueue) => {
  for (const [i, j] of existQueue) {
    for (const di of dif) {
      for (const dj of dif) {
        const [mi, mj] = [i + di, j + dj];

        if (isValidPos(mi, mj) && states[mi][mj]) {
          states[mi][mj] -= 1;

          if (!states[mi][mj]) {
            newQueue.push([mi, mj]);
          }
        }
      }
    }
  }
};

while (1) {
  const newQueue = [];
  processPoses(queue, newQueue);

  if (!newQueue.length) break;
  queue = newQueue;
  result += 1;
}

console.log(result);
