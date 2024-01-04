/* eslint-disable no-loop-func */
const fs = require('fs');

const [cr, ...rawMap] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [c, r] = cr.split(' ').map(Number);
const map = rawMap.map((el) => el.split(' ').map(Number));
const moves = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const min = Math.min(c, r);
let prefix = 0;

const getCheeseCounts = () => {
  let count = 0;

  for (let i = prefix; i < c - prefix; i += 1) {
    for (let j = prefix; j < r - prefix; j += 1) {
      if (map[i][j] === 1) count += 1;
    }
  }

  return count;
};

let cheeseCountCache = getCheeseCounts();

const isValidPos = (curC, curR, visited) => (
  curC >= 0
    && curR >= 0
    && curC < (c - prefix)
    && curR < (r - prefix)
    && !visited[curC][curR]
);

while (prefix < min) {
  let poses = [[0, 0]];
  const visited = new Array(c - prefix).fill().map(
    () => new Array(r - prefix).fill(false),
  );
  visited[0][0] = true;

  while (poses.length) {
    const newPoses = [];

    for (const [curC, curR] of poses) {
      if (map[curC + prefix][curR + prefix] === 1) {
        map[curC + prefix][curR + prefix] = 0;
      } else {
        for (const move of moves) {
          const [mc, mr] = [curC + move[0], curR + move[1]];

          if (isValidPos(mc, mr, visited)) {
            visited[mc][mr] = true;

            poses.push([mc, mr]);
          }
        }
      }
    }

    poses = newPoses;
  }

  prefix += 1;

  const cheeseCount = getCheeseCounts();

  if (!cheeseCount) break;
  cheeseCountCache = cheeseCount;
}

console.log(`${prefix}\n${cheeseCountCache}`);
