/* eslint-disable prefer-destructuring */
const fs = require('fs');

const inputs = fs.readFileSync(process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin')
  .toString().trim().split('\n');

const args = [];
for (let i = 1; i < inputs.length; i += 2) {
  args.push(inputs[i + 1].split(' ').map(Number));
}

const solution = (arg) => {
  const n = arg.length;
  const dp = new Array(n).fill().map(() => new Array(n).fill(null));
  const sum = new Array(n).fill(0);
  sum[0] = arg[0];
  for (let i = 1; i < n; i += 1) {
    sum[i] += sum[i - 1] + arg[i];
  }

  const recursive = (left, right) => {
    if (dp[left][right] !== null) return dp[left][right];

    let min = Infinity;

    if (right - left === 0) {
      min = 0;
    } else if (right - left === 1) {
      min = arg[right] + arg[left];
    } else {
      const partSum = sum[right] - (sum[left - 1] || 0);

      if (right - left === 2) {
        min = 0;

        min += arg[left + 1] + Math.min(arg[left], arg[right]);
      } else {
        for (let i = left; i < right; i += 1) {
          min = Math.min(
            min,
            recursive(left, i) + recursive(i + 1, right),
          );
        }
      }

      min += partSum;
    }

    dp[left][right] = min;
    dp[right][left] = min;

    return min;
  };

  recursive(0, n - 1);

  return dp[0][n - 1];
};

console.log(args.map(solution).join('\n'));
