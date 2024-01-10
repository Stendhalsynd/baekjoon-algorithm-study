/* eslint-disable no-param-reassign */

const fs = require('fs');

const [n, k] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split(' ')
  .map(Number);

class LinkedNode {
  constructor(value, next) {
    this.value = value;
    this.next = next || null;
  }
}

const last = new LinkedNode(n);
let curNode = last;

for (let i = n - 1; i >= 1; i -= 1) {
  const node = new LinkedNode(i, curNode);

  curNode = node;
}

last.next = curNode;
curNode = last;

const murdered = [];

const forwardStep = (steps) => {
  while (steps) {
    curNode = curNode.next;
    steps -= 1;
  }
};

while (1) {
  if (curNode.next.value === curNode.value) {
    murdered.push(curNode.value);
    break;
  }

  forwardStep(k - 1);

  murdered.push(curNode.next.value);
  curNode.next = curNode.next.next;
}

console.log(`<${murdered.join(', ')}>`);
