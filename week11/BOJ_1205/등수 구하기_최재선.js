const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [_N, myScore, P] = inputs[0].split(' ').map(Number);
const list = inputs[1] ? inputs[1].split(' ').map(Number) : [];

list.push(myScore);
list.sort((a, b) => b - a);

const binarySearch = (left, right, target, arr) => {
  if (left > right) return right;

  const mid = Math.floor((left + right) / 2);

  if (arr[mid] > target) {
    return binarySearch(mid + 1, right, target, arr);
  }

  return binarySearch(left, mid - 1, target, arr);
};

const myScoreIndex = binarySearch(0, list.length - 1, myScore, list) + 1;

if (myScoreIndex >= P || list[P] === myScore) console.log(-1);
else console.log(myScoreIndex + 1);
