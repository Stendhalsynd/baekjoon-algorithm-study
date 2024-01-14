const fs = require('fs');

const inputs = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [n, w, l] = inputs[0].split(' ').map(Number);
const weights = inputs[1].split(' ').map(Number);
const bridge = new Array(w).fill(0);
let totalWeight = 0;
let result = 0;

const moveInBridge = () => {
  totalWeight -= bridge[w - 1];

  for (let i = w - 1; i >= 1; i -= 1) {
    bridge[i] = bridge[i - 1];
  }

  bridge[0] = 0;
  result += 1;
};

const pushWeightToBridge = (weight) => {
  moveInBridge();

  while (totalWeight + weight > l) {
    moveInBridge();
  }

  totalWeight += weight;
  bridge[0] += weight;
};

for (const weight of weights) {
  pushWeightToBridge(weight);
}

const leastIndex = bridge.findIndex((el) => !!el);

if (leastIndex !== -1) {
  result += w - leastIndex;
}

console.log(result);
