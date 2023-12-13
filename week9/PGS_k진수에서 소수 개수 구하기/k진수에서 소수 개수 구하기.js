function solution(n, k) {
  const nums = n.toString(k).split('0').map(Number);
  const primeNums = new Set();
  primeNums.add(2);

  const isPrime = (number) => {
    if (primeNums.has(number)) return true;
    if (number === 1) return false;
    if (number % 2 === 0) return false;

    const mid = Math.floor(Math.sqrt(number));

    for (let i = 3; i <= mid; i += 2) {
      if (number % i === 0) {
        return false;
      }
    }

    primeNums.add(number);
    return true;
  };

  let result = 0;

  for (const num of nums) {
    if (isPrime(num)) result += 1;
  }

  return result;
}