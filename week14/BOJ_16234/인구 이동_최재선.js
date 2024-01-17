/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [n, l, r] = inputs[0].split(' ').map(Number);
const map = inputs.slice(1).map((el) => el.split(' ').map(Number));
const moves = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const checkIsMoveValid = (i, j) => i >= 0 && i < n && j >= 0 && j < n;
const checkCondition = (i, j, mi, mj) => {
  const value = map[i][j];
  const movedValue = map[mi][mj];
  const diff = Math.abs(value - movedValue);

  if (diff >= l && diff <= r) {
    return true;
  }

  return false;
};

const fillGroup = (i, j, visited, group) => {
  visited[i][j] = 1;
  group.push([i, j]);

  for (const [di, dj] of moves) {
    const [mi, mj] = [i + di, j + dj];

    if (checkIsMoveValid(mi, mj) && !visited[mi][mj] && checkCondition(i, j, mi, mj)) {
      fillGroup(mi, mj, visited, group);
    }
  }
};

const fillGroups = (groups) => {
  const visited = new Array(n).fill().map(() => new Array(n).fill(0));

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      if (!visited[i][j]) {
        const group = [];
        fillGroup(i, j, visited, group);

        if (group.length >= 2) groups.push(group);
      }
    }
  }
};

const mergeGroups = (groups) => {
  for (const group of groups) {
    const divide = group.length;
    const sum = group.reduce((acc, cur) => acc + map[cur[0]][cur[1]], 0);
    const avg = Math.floor(sum / divide);

    for (const [i, j] of group) {
      map[i][j] = avg;
    }
  }
};

let result = 0;

while (1) {
  const groups = [];
  fillGroups(groups);

  if (!groups.length) break;

  mergeGroups(groups);

  result += 1;
}

console.log(result);
