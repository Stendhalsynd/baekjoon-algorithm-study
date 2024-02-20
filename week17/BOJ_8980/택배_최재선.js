/* eslint-disable no-param-reassign */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const [n, c] = inputs[0].split(' ').map(Number);
const infos = inputs.slice(2).map((el) => el.split(' ').map(Number));

class SegmentTree {
  constructor(arr, compare) {
    this.arr = arr;
    this.tree = new Array(arr.length * 4);
    this.lazy = new Array(arr.length * 4).fill(0);
    this.compare = compare;

    this.getMidIndex = (index1, index2) => Math.floor((index1 + index2) / 2);
    this.getLeftIndex = (index) => index * 2 + 1;
    this.getRightIndex = (index) => index * 2 + 2;

    this.build(0, 0, arr.length - 1);
  }

  build(node, left, right) {
    if (left === right) {
      this.tree[node] = this.arr[left];
    } else {
      const mid = this.getMidIndex(left, right);
      const leftChild = this.getLeftIndex(node);
      const rightChild = this.getRightIndex(node);
      this.build(leftChild, left, mid);
      this.build(rightChild, mid + 1, right);
      this.tree[node] = this.compare(this.tree[leftChild], this.tree[rightChild]);
    }
  }

  updateRange(node, start, end, l, r, diff) {
    if (this.lazy[node] !== 0) {
      this.tree[node] += this.lazy[node];
      if (start !== end) {
        this.lazy[this.getLeftIndex(node)] += this.lazy[node];
        this.lazy[this.getRightIndex(node)] += this.lazy[node];
      }
      this.lazy[node] = 0;
    }

    if (start > end || start > r || end < l) {
      return;
    }

    if (l <= start && end <= r) {
      this.tree[node] += diff;
      if (start !== end) {
        this.lazy[this.getLeftIndex(node)] += diff;
        this.lazy[this.getRightIndex(node)] += diff;
      }
      return;
    }

    const mid = this.getMidIndex(start, end);
    this.updateRange(this.getLeftIndex(node), start, mid, l, r, diff);
    this.updateRange(this.getRightIndex(node), mid + 1, end, l, r, diff);

    this.tree[node] = this.compare(
      this.tree[this.getLeftIndex(node)],
      this.tree[this.getRightIndex(node)],
    );
  }

  query(node, left, right, queryLeft, queryRight) {
    if (left > queryRight || right < queryLeft) {
      return -Infinity;
    }

    if (this.lazy[node] !== 0) {
      this.tree[node] += this.lazy[node];
      if (left !== right) {
        this.lazy[this.getLeftIndex(node)] += this.lazy[node];
        this.lazy[this.getRightIndex(node)] += this.lazy[node];
      }
      this.lazy[node] = 0;
    }

    if (left >= queryLeft && right <= queryRight) {
      return this.tree[node];
    }

    const mid = this.getMidIndex(left, right);
    const leftChild = this.getLeftIndex(node);
    const rightChild = this.getRightIndex(node);
    const leftValue = this.query(leftChild, left, mid, queryLeft, queryRight);
    const rightValue = this.query(rightChild, mid + 1, right, queryLeft, queryRight);

    return this.compare(leftValue, rightValue);
  }
}

infos.sort((a, b) => {
  if (a[1] !== b[1]) return a[1] - b[1];

  return a[0] - b[0];
});

let result = 0;

const acc = new Array(n + 1).fill(0);
const maxSegTree = new SegmentTree(acc, (left, right) => Math.max(left, right));

const getAvailableAmount = (start, end) => c - maxSegTree.query(0, 0, n, start, end);

for (const [start, end, amount] of infos) {
  const availableAmount = getAvailableAmount(start, end - 1);
  const prefixAmount = Math.min(availableAmount, amount);

  if (prefixAmount) {
    maxSegTree.updateRange(0, 0, n, start, end - 1, prefixAmount);
    result += prefixAmount;
  }
}

console.log(result);
