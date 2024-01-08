function solution(orders, course) {
  const alphaBits = new Array(26).fill().map((_, index) => 1 << index);

  orders = orders.map(
    (chars) => chars.split('')
      .map((char) => 1 << (90 - char.charCodeAt()))
      .reduce((acc, cur) => acc + cur, 0),
  );

  const getBucket = (n) => {
    const bucket = [];

    const dfs = (start, num, count) => {
      if (count === n) {
        bucket.push(num);
        return;
      }

      for (let i = start; i < 26; i += 1) {
        dfs(i + 1, num + alphaBits[i], count + 1);
      }
    };

    dfs(0, 0, 0);

    return bucket;
  };

  const result = [];

  for (const n of course) {
    const bucket = getBucket(n);
    const memo = new Map();

    for (const order of orders) {
      for (const comb of bucket) {
        if ((order & comb) === comb) {
          if (memo.has(comb)) {
            memo.set(comb, memo.get(comb) + 1);
          } else {
            memo.set(comb, 1);
          }
        }
      }
    }

    const targetCombs = Array
      .from(memo)
      .sort(
        (a, b) => b[1] - a[1],
      )
      .filter(
        (el, _, arr) => el[1] === Math.max(2, arr[0][1]),
      )
      .map((el) => el[0]);

    result.push(...targetCombs);
  }

  const convertBitToAlpha = (bit) => {
    let alpha = '';
    let prefix = 0;

    while (bit) {
      if (bit & 1) {
        alpha = String.fromCharCode(90 - prefix) + alpha;
      }

      bit >>= 1;
      prefix += 1;
    }

    return alpha;
  };
    
    
  return result.sort((a, b) => b - a).map(convertBitToAlpha).sort();
}