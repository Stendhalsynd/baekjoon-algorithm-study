function solution(info, queries) {
  const kindsMap = {
    lang: new Set(['-']),
    position: new Set(['-']),
    career: new Set(['-']),
    soulFood: new Set(['-']),
  };

  for (let i = 0; i < info.length; i += 1) {
    const [lang, position, career, soulFood, score] = info[i].split(' ');

    kindsMap.lang.add(lang);
    kindsMap.position.add(position);
    kindsMap.career.add(career);
    kindsMap.soulFood.add(soulFood);
      
    info[i] = [lang, position, career, soulFood, Number(score)];
  }

  const leafs = [];
  const root = {};
  let cur = [root];

  for (const key in kindsMap) {
    const newCur = [];

    const kinds = kindsMap[key];

    for (const el of cur) {
      for (const kind of kinds) {
        const value = key === 'soulFood' ? [] : {};
        el[kind] = value;

        newCur.push(value);

        if (key === 'soulFood') {
          leafs.push(value);
        }
      }
    }

    cur = newCur;
  }

  for (const [lang, position, career, soulFood, score] of info) {
    for (const langEl of [lang, '-']) {
      for (const positionEl of [position, '-']) {
        for (const careerEl of [career, '-']) {
          for (const soulFoodEl of [soulFood, '-']) {
            root[langEl][positionEl][careerEl][soulFoodEl].push(score);
          }
        }
      }
    }
  }

  for (const leaf of leafs) {
    leaf.sort((a, b) => a - b);
  }

  const binarySearch = (left, right, target, arr) => {
    if (left > right) return left - 1;

    const mid = Math.floor((left + right) / 2);

    if (arr[mid] < target) {
      return binarySearch(mid + 1, right, target, arr);
    }

    return binarySearch(left, mid - 1, target, arr);
  };

  const getQueryCounts = (query) => {
    const [lang, position, career, rest] = query.split(' and ');
    const [soulFood, score] = rest.split(' ');
    const numScore = Number(score);
    const scoreArr = root[lang][position][career][soulFood];

    return scoreArr.length - binarySearch(0, scoreArr.length - 1, numScore, scoreArr) - 1;
  };

  return queries.map(getQueryCounts);
}