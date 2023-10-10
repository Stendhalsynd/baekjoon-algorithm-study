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
  const P = input[1].split(" ").map(Number);

  P.sort((a, b) => a - b);

  console.log(P.reduce((acc, val, idx) => (acc += val * (N - idx)), 0));

  process.exit();
});
