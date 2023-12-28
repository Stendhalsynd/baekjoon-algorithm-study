function solution(rows, columns, queries) {
  const board = new Array(rows).fill().map((_, rIndex) => new Array(columns).fill().map((_, cIndex) => rIndex * columns + cIndex));

  const result = [];
  
  for (const query of queries) {
      const [x1, y1, x2, y2] = [query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1];
      const tmpArr = [];
      
      for (let i = y1; i < y2; i += 1) {
          tmpArr.push(board[x1][i]);
      }
      
      for (let i = x1; i < x2; i += 1) {
          tmpArr.push(board[i][y2]);
      }
      
      for (let i = y2; i > y1; i -= 1) {
          tmpArr.push(board[x2][i]);
      }
      
      for (let i = x2; i > x1; i -= 1) {
          tmpArr.push(board[i][y1]);
      }
      
      tmpArr.unshift(tmpArr.pop());
      let index = 0;
      
      for (let i = y1; i < y2; i += 1) {
          board[x1][i] = tmpArr[index];
          index += 1;
      }
      
      for (let i = x1; i < x2; i += 1) {
          board[i][y2] = tmpArr[index];
          index += 1;
      }
      
      for (let i = y2; i > y1; i -= 1) {
          board[x2][i] = tmpArr[index];
          index += 1;
      }
      
      for (let i = x2; i > x1; i -= 1) {
          board[i][y1] = tmpArr[index];
          index += 1;
      }
      
      result.push(Math.min(...tmpArr) + 1);
  }
  
  return result;
}