/* eslint-disable no-bitwise */
const fs = require('fs');

const N = Number(fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim());

if (N & 1) console.log('SK');
else console.log('CY');
