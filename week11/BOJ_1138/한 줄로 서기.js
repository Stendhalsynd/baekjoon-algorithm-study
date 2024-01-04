const fs = require('fs');

const [rawN, rest] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const N = Number(rawN);
const info = rest.split(' ').map(Number);

class UnionFind {
  constructor(size) {
    this.arr = new Array(size);

    for (let i = 0; i < size; i += 1) {
      this.arr[i] = i;
    }
  }

  find(x) {
    if (this.arr[x] === x) return x;

    const value = this.find(this.arr[x]);
    this.arr[x] = value;

    return value;
  }
}

const result = new Array(N);
const uf = new UnionFind(N + 1);

for (let i = 0; i < N; i += 1) {
  const index = info[i];
  let prefixedIndex = uf.find(0);

  for (let j = 1; j <= index; j += 1) {
    const newIndex = uf.find(prefixedIndex + 1);

    if (prefixedIndex === newIndex) break;
    prefixedIndex = newIndex;
  }

  result[prefixedIndex] = i + 1;
  uf.arr[prefixedIndex] += 1;
}

console.log(result.join(' '));
