const fs = require('fs');

const [poses, ...commands] = fs.readFileSync(
  process.env.LOGNAME === 'jake' ? './input.txt' : '/dev/stdin',
).toString().trim().split('\n');

const [kPos, sPos, n] = poses.split(' ');

const convertPosToNumber = (pos) => {
  const [rawR, rawC] = pos.split('');
  const r = Number(rawC) - 1;
  const c = rawR.charCodeAt() - 65;

  return [r, c];
};

let [kr, kc] = convertPosToNumber(kPos, 1);
let [sr, sc] = convertPosToNumber(sPos, 2);

const checkIsMovePossible = (mr, mc) => (
  mr >= 0 && mr < 8 && mc >= 0 && mc < 8
);

const checkIsMoveValid = (dr, dc) => {
  const [mkr, mkc] = [kr + dr, kc + dc];

  if (checkIsMovePossible(mkr, mkc)) {
    if (mkr === sr && mkc === sc) {
      const [msr, msc] = [sr + dr, sc + dc];
      if (checkIsMovePossible(msr, msc)) {
        [kr, kc, sr, sc] = [mkr, mkc, msr, msc];
      }
    } else {
      [kr, kc] = [mkr, mkc];
    }
  }
};

for (const command of commands) {
  let [dr, dc] = [0, 0];

  if (command === 'R') {
    dc += 1;
  } else if (command === 'L') {
    dc -= 1;
  } else if (command === 'B') {
    dr -= 1;
  } else if (command === 'T') {
    dr += 1;
  } else if (command === 'RT') {
    dc += 1;
    dr += 1;
  } else if (command === 'LT') {
    dc -= 1;
    dr += 1;
  } else if (command === 'RB') {
    dc += 1;
    dr -= 1;
  } else if (command === 'LB') {
    dc -= 1;
    dr -= 1;
  }

  checkIsMoveValid(dr, dc);
}

const convertNumberToPos = (r, c) => `${String.fromCharCode(c + 65)}${r + 1}`;

console.log(`${convertNumberToPos(kr, kc)}\n${convertNumberToPos(sr, sc)}`);
