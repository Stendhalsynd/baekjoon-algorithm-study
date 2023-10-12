const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const N = Number(input[0]);
  const numbers = input[1].split(" ").map(Number);

  let result = Number.MAX_SAFE_INTEGER;
  let smallestSum = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < N; i++) {
    let currentSum = 0;

    for (let j = 0; j < N; j++) {
      if (i !== j) {
        currentSum += Math.abs(numbers[i] - numbers[j]);
      }
    }

    if (
      currentSum < smallestSum ||
      (currentSum === smallestSum && numbers[i] < result)
    ) {
      smallestSum = currentSum;
      result = numbers[i];
    }
  }

  console.log(result);

  process.exit();
});
