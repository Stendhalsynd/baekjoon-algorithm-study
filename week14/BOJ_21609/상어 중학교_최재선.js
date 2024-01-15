/* eslint-disable no-unreachable-loop */
/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const convert = (str) => str.split(' ').map(Number);
const [N, M] = convert(inputs[0]);
let matrix = inputs.slice(1, 1 + N).map(convert);
let result = 0;
const moves = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const checkIsValidPos = (i, j) => (i >= 0 && i < N && j >= 0 && j < N);

const findGroupArea = (i, j, visited, blocksInfo, blockType) => {
  visited[i][j] = 1;

  blocksInfo.blocks.push([i, j]);
  if (matrix[i][j] === 0) {
    blocksInfo.rainbowCount += 1;
  }

  if (matrix[i][j] !== 0
    && (blocksInfo.represent[0] > i || (
      blocksInfo.represent[0] === i && blocksInfo.represent[1] > j
    ))) {
    blocksInfo.represent[0] = i;
    blocksInfo.represent[1] = j;
  }

  for (const [di, dj] of moves) {
    const [mi, mj] = [i + di, j + dj];

    if (checkIsValidPos(mi, mj) && !visited[mi][mj] && (matrix[mi][mj] === blockType || matrix[mi][mj] === 0)) {
      findGroupArea(mi, mj, visited, blocksInfo, blockType);
    }
  }
};

const getBlockGroups = () => {
  const groups = [];

  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      if (matrix[i][j] !== -1 && matrix[i][j] !== 0 && matrix[i][j] !== null) {
        const visited = new Array(N).fill().map(() => new Array(N).fill(0));
        const blocksInfo = {
          blocks: [],
          rainbowCount: 0,
          represent: [i, j],
        };
        findGroupArea(i, j, visited, blocksInfo, matrix[i][j]);

        if (blocksInfo.blocks.length >= 2) {
          groups.push(blocksInfo);
        }
      }
    }
  }

  return groups;
};

const filterBlockGroups = (blockGroups) => {
  blockGroups.sort((a, b) => {
    if (a.blocks.length !== b.blocks.length) {
      return b.blocks.length - a.blocks.length;
    }

    if (a.rainbowCount !== b.rainbowCount) {
      return b.rainbowCount - a.rainbowCount;
    }

    if (a.represent[0] !== b.represent[0]) {
      return b.represent[0] - a.represent[0];
    }

    if (a.represent[1] !== b.represent[1]) {
      return b.represent[1] - a.represent[1];
    }

    return 1;
  });

  return blockGroups[0].blocks;
};

const removeGroupStones = (groups) => {
  for (const [i, j] of groups) {
    matrix[i][j] = null;
  }
};

const gravity = () => {
  for (let j = 0; j < N; j += 1) {
    let fallingIndex = N - 1;
    for (let i = N - 1; i >= 0; i -= 1) {
      if (matrix[i][j] === -1) {
        fallingIndex = i - 1;
      } else if (matrix[i][j] !== null) {
        if (fallingIndex !== i) {
          matrix[fallingIndex][j] = matrix[i][j];
          matrix[i][j] = null;
        }
        fallingIndex -= 1;
      }
    }
  }
};

const rotate = () => {
  const newMatrix = new Array(N).fill().map(() => new Array(N));

  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      newMatrix[N - j - 1][i] = matrix[i][j];
    }
  }

  matrix = newMatrix;
};

while (1) {
  const blockGroups = getBlockGroups();
  if (!blockGroups.length) break;
  const targetGroup = filterBlockGroups(blockGroups);

  result += targetGroup.length ** 2;

  removeGroupStones(targetGroup);
  gravity();
  rotate();
  gravity();
}

console.log(result);
