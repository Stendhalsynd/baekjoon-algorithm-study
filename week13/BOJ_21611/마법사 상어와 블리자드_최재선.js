const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const convert = (str) => str.split(' ').map(Number);
const [N, M] = convert(inputs[0]);
const matrix = inputs.slice(1, 1 + N).map(convert);
const magics = inputs.slice(1 + N).map(convert);
const size = N ** 2;

let oneDimensionMatrix = new Array(size);
const pinVisited = new Array(N).fill().map(() => new Array(N).fill(false));

let inputIndex = size - 1;

const checkIsValidPos = (i, j) => i >= 0 && i < N && j >= 0 && j < N && !pinVisited[i][j];

const saveMove = (i, j) => {
  oneDimensionMatrix[inputIndex] = matrix[i][j];
  pinVisited[i][j] = true;
  inputIndex -= 1;
};

saveMove(0, 0);

const move = (i, j, direction) => {
  if (direction === '+j') {
    if (checkIsValidPos(i, j + 1)) {
      saveMove(i, j + 1);
      move(i, j + 1, direction);
    } else if (checkIsValidPos(i + 1, j)) {
      saveMove(i + 1, j);
      move(i + 1, j, '+i');
    }
  } else if (direction === '+i') {
    if (checkIsValidPos(i + 1, j)) {
      saveMove(i + 1, j);
      move(i + 1, j, direction);
    } else if (checkIsValidPos(i, j - 1)) {
      saveMove(i, j - 1);
      move(i, j - 1, '-j');
    }
  } else if (direction === '-j') {
    if (checkIsValidPos(i, j - 1)) {
      saveMove(i, j - 1);
      move(i, j - 1, direction);
    } else if (checkIsValidPos(i - 1, j)) {
      saveMove(i - 1, j);
      move(i - 1, j, '-i');
    }
  } else if (direction === '-i') {
    if (checkIsValidPos(i - 1, j)) {
      saveMove(i - 1, j);
      move(i - 1, j, direction);
    } else if (checkIsValidPos(i, j + 1)) {
      saveMove(i, j + 1);
      move(i, j + 1, '+j');
    }
  }
};

move(0, 0, '+j');

const directionIndexMap = new Array(5);
directionIndexMap[1] = [0, 7];
directionIndexMap[2] = [0, 3];
directionIndexMap[3] = [0, 1];
directionIndexMap[4] = [0, 5];

const fillIndexMap = (indexMap) => {
  let nextIndex = 2 * indexMap[indexMap.length - 1] - indexMap[indexMap.length - 2] + 8;

  while (nextIndex < size) {
    indexMap.push(nextIndex);
    nextIndex = 2 * indexMap[indexMap.length - 1] - indexMap[indexMap.length - 2] + 8;
  }
};

for (let i = 1; i < 5; i += 1) {
  fillIndexMap(directionIndexMap[i]);
}

const memo = [0, 0, 0];

const compress = () => {
  let bucket = [0];
  let counts = [1];

  for (let i = 0; i < oneDimensionMatrix.length; i += 1) {
    if (oneDimensionMatrix[i] !== 0) {
      if (bucket[bucket.length - 1] !== oneDimensionMatrix[i]) {
        bucket.push(oneDimensionMatrix[i]);
        counts.push(1);
      } else {
        counts[counts.length - 1] += 1;
      }
    }
  }

  while (1) {
    const newBucket = [0];
    const newCounts = [1];
    let flag = true;

    for (let i = 1; i < bucket.length; i += 1) {
      if (counts[i] > 3) {
        flag = false;

        memo[bucket[i] - 1] += counts[i];
      } else {
        // eslint-disable-next-line no-lonely-if
        if (newBucket[newBucket.length - 1] === bucket[i]) {
          newCounts[newCounts.length - 1] += counts[i];
        } else {
          newBucket.push(bucket[i]);
          newCounts.push(counts[i]);
        }
      }
    }

    if (flag) break;

    bucket = newBucket;
    counts = newCounts;
  }

  const newOneDimensionMatrix = [0];

  for (let i = 1; i < bucket.length; i += 1) {
    if (newOneDimensionMatrix.length + 2 <= size) {
      newOneDimensionMatrix.push(counts[i]);
      newOneDimensionMatrix.push(bucket[i]);
    } else {
      break;
    }
  }

  oneDimensionMatrix = newOneDimensionMatrix;
};

const blizard = (direction, distance) => {
  for (let i = 1; i <= distance; i += 1) {
    if (oneDimensionMatrix[directionIndexMap[direction][i]]) {
      oneDimensionMatrix[directionIndexMap[direction][i]] = 0;
    }
  }

  compress();
};

for (let i = 0; i < M; i += 1) {
  blizard(magics[i][0], magics[i][1]);
}

console.log(memo[0] + 2 * memo[1] + 3 * memo[2]);
