const fs = require('fs');

const [rawN, ...rest] = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : 'dev/stdin')
  .toString().trim().split('\n');

class TreeNode {
  constructor(x, y, r) {
    this.x = x;
    this.y = y;
    this.r = r;

    this.children = [];
    this.parent = null;
  }

  isIncludeIn(node) {
    return ((this.x - node.x) ** 2 + (this.y - node.y) ** 2 - (this.r + node.r) ** 2) < 0;
  }
}

const n = Number(rawN);
const circles = rest.map((el) => el.split(' ').map(Number));
circles.sort((a, b) => b[2] - a[2]);

const head = new TreeNode(0, 0, 1010002);

const placeNode = (curNode, node) => {
  let flag = false;

  for (const childNode of curNode.children) {
    if (childNode.isIncludeIn(node)) {
      placeNode(childNode, node);
      flag = true;
      break;
    }
  }

  if (!flag) {
    curNode.children.push(node);
  }
};

for (const [x, y, r] of circles) {
  const treeNode = new TreeNode(x, y, r);

  placeNode(head, treeNode);
}

let result = 0;

const dfs = (curNode, accValue) => {
  if (!curNode.children.length) {
    result = Math.max(result, accValue);

    return accValue;
  }

  const values = [];

  for (const childNode of curNode.children) {
    values.push(dfs(childNode, 1));
  }

  const max = Math.max(...values);
  values.push(accValue);
  values.sort((a, b) => b - a);
  result = Math.max(result, values[0] + values[1]);

  return accValue + max;
};

dfs(head, 0);

console.log(result);
