/* eslint-disable max-len */
const fs = require('fs');

const [_, ...words] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

class Heap {
  constructor() {
    this.heap = [];

    this.getParentIndex = (index) => Math.floor((index - 1) / 2);
    this.getLeftChild = (index) => index * 2 + 1;
    this.getRightChild = (index) => index * 2 + 2;
  }

  bubbleUp() {
    let index = this.heap.length - 1;

    while (index) {
      const parentIndex = this.getParentIndex(index);

      if (this.heap[index] < this.heap[parentIndex]) {
        [
          this.heap[index], this.heap[parentIndex],
        ] = [
          this.heap[parentIndex], this.heap[index],
        ];
      } else {
        break;
      }

      index = parentIndex;
    }
  }

  size() {
    return this.heap.length;
  }

  bubbleDown() {
    const size = this.size();
    let index = 0;
    let leftIndex = 1;
    let rightIndex = 2;

    while (
      (leftIndex < size && this.heap[index] > this.heap[leftIndex])
      || (rightIndex < size && this.heap[index] > this.heap[rightIndex])
    ) {
      if (
        (leftIndex < size && this.heap[index] > this.heap[leftIndex]) && (rightIndex < size && this.heap[index] > this.heap[rightIndex])
      ) {
        const targetIndex = this.heap[leftIndex] < this.heap[rightIndex]
          ? leftIndex
          : rightIndex;

        [
          this.heap[index], this.heap[targetIndex],
        ] = [
          this.heap[targetIndex], this.heap[index],
        ];

        index = targetIndex;
      } else if (leftIndex < size && this.heap[index] > this.heap[leftIndex]) {
        [
          this.heap[index], this.heap[leftIndex],
        ] = [
          this.heap[leftIndex], this.heap[index],
        ];

        index = leftIndex;
      } else if (rightIndex < size && this.heap[index] > this.heap[rightIndex]) {
        [
          this.heap[index], this.heap[rightIndex],
        ] = [
          this.heap[rightIndex], this.heap[index],
        ];

        index = rightIndex;
      }

      leftIndex = this.getLeftChild(index);
      rightIndex = this.getRightChild(index);
    }
  }

  push(x) {
    this.heap.push(x);

    this.bubbleUp();
  }

  pop() {
    if (!this.size()) return -1;
    if (this.size() === 1) return this.heap.pop();

    const popped = this.heap[0];
    this.heap[0] = this.heap.pop();

    this.bubbleDown();

    return popped;
  }
}

const getNextWord = (word) => {
  const heap = new Heap();
  const convertedArr = word.split('').map((str) => str.charCodeAt());

  while (convertedArr.length) {
    const { length } = convertedArr;
    if (convertedArr.length === 1) return word;

    if (convertedArr[length - 1] > convertedArr[length - 2]) {
      heap.push(convertedArr.pop());
      break;
    } else {
      heap.push(convertedArr.pop());
    }
  }

  const tmpSaved = [];
  const compare = convertedArr.pop();
  heap.push(compare);

  let flag = false;

  while (heap.size()) {
    const popped = heap.pop();

    if (!flag && popped > compare) {
      flag = true;
      convertedArr.push(popped);
    } else {
      tmpSaved.push(popped);
    }
  }

  return [...convertedArr, ...tmpSaved].map((el) => String.fromCharCode(el)).join('');
};

console.log(words.map(getNextWord).join('\n'));
