const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin').toString().split('\n');

const [n, m, t] = inputs[0].split(' ').map(Number);
const matrix = inputs.slice(1).map((el) => el.split(' ').map(Number));

const moves = [[1, 0], [-1, 0], [0, 1], [0, -1]];
let curTime = 0;

const visited = new Array(n).fill().map(() => new Array(m).fill(0));
let poses = [[0, 0]];
let flag1 = Infinity;
let flag2 = Infinity;

visited[0][0] = 1;

const isValidPos = (i, j) => i >= 0 && i < n && j >= 0 && j < m && matrix[i][j] !== 1;

while (curTime < flag2 && curTime < t && poses.length) {
  curTime += 1;
  const newPoses = [];

  for (const [i, j] of poses) {
    for (const [di, dj] of moves) {
      const [mi, mj] = [i + di, j + dj];

      if (isValidPos(mi, mj) && !visited[mi][mj]) {
        visited[mi][mj] = 1;
        newPoses.push([mi, mj]);

        if (matrix[mi][mj] === 2) {
          const calculatedTime = curTime + n - 1 - mi + m - 1 - mj;
          flag2 = calculatedTime;
        }
      }
    }
  }

  if (visited[n - 1][m - 1]) {
    flag1 = curTime;
    break;
  }
  poses = newPoses;
}

const spend = Math.min(flag1, flag2);
console.log(spend <= t ? spend : 'Fail');
