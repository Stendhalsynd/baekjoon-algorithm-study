/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [n, m] = inputs[0].split(' ').map(Number);
const map = inputs.slice(1, 1 + n).map((el) => el.split(' ').map(Number));
const magics = inputs.slice(1 + n).map((el) => el.split(' ').map(Number));

let cloudPoses = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]];

const directions = [
  null,
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
];

const diagonalDirs = [
  [1, 1],
  [-1, -1],
  [1, -1],
  [-1, 1],
];

const prefix = (x) => {
  x %= n;
  if (x < 0) x += n;

  return x;
};

const move = (dir, distance) => {
  const [dx, dy] = directions[dir];

  for (let i = 0; i < cloudPoses.length; i += 1) {
    const [cx, cy] = cloudPoses[i];
    cloudPoses[i] = [cx + dx * distance, cy + dy * distance].map(prefix);
  }
};

const saveAndGetTmpPoses = () => {
  const tmpPoses = new Set();

  for (const [cx, cy] of cloudPoses) {
    tmpPoses.add(`${cx},${cy}`);
  }

  return tmpPoses;
};

const raining = () => {
  for (const [cx, cy] of cloudPoses) {
    map[cx][cy] += 1;
  }
};

const checkCopyPosValid = (x, y) => (
  x >= 0 && x < n && y >= 0 && y < n
);

const copyBug = () => {
  for (const [cx, cy] of cloudPoses) {
    for (const [dx, dy] of diagonalDirs) {
      const [mx, my] = [cx + dx, cy + dy];

      if (checkCopyPosValid(mx, my) && map[mx][my]) {
        map[cx][cy] += 1;
      }
    }
  }

  cloudPoses = [];
};

const step5 = (savedPoses) => {
  const newCloudPoses = [];

  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < n; y += 1) {
      const key = `${x},${y}`;

      if (!savedPoses.has(key) && map[x][y] >= 2) {
        newCloudPoses.push([x, y]);

        map[x][y] -= 2;
      }
    }
  }

  cloudPoses = newCloudPoses;
};

const bibaragi = ([dir, distance]) => {
  move(dir, distance);

  const tmpSavedPoses = saveAndGetTmpPoses();

  raining();
  copyBug();
  step5(tmpSavedPoses);
};

for (const magic of magics) {
  bibaragi(magic);
}

let result = 0;

for (let i = 0; i < map.length; i += 1) {
  for (let j = 0; j < map[0].length; j += 1) {
    result += map[i][j];
  }
}

console.log(result);
