const fs = require('fs');

const [_rawN, ...rawInfos] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const infos = rawInfos.map((el) => el.split(' ').map(Number));
const bucket = new Set();

const getSplit = (num) => [
  Math.floor(num / 100),
  Math.floor((num % 100) / 10),
  num % 10,
];

for (let i = 100; i < 1000; i += 1) {
  const [h, t, o] = getSplit(i);

  if (h && t && o && (h !== t) && (h !== o) && (t !== o)) {
    bucket.add(i);
  }
}

for (const [num, sCount, bCount] of infos) {
  const [nh, nt, no] = getSplit(num);

  for (const el of bucket) {
    let [es, eb] = [0, 0];
    const [eh, et, eo] = getSplit(el);

    if (eh === nh) es += 1;
    else if (eh === nt || eh === no) eb += 1;

    if (et === nt) es += 1;
    else if (et === nh || et === no) eb += 1;

    if (eo === no) es += 1;
    else if (eo === nh || eo === nt) eb += 1;

    if (sCount !== es || bCount !== eb) bucket.delete(el);
  }
}

console.log(bucket.size);
