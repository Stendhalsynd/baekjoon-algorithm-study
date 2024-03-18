const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [m, n] = input[0].split(' ').map(Number)
let cnt = 0; // 글자의 개수

// 현수막 모양 만들기
let arr = [];
for(let i = 1; i <= m; i++) {
  arr.push(input[i].split(' ').map(Number))
}
// console.log(arr)
// visited 만들기
let visited = []
for(let i = 0; i < m; i++) {
  const temp = [];
  for(let j = 0; j < n; j++) {
    temp.push(false)
  }
  visited.push(temp)
}
// console.log(visited)

// dfs 탐색 만들기
function dfs (x, y) {
  // 예외처리 만들기
  if(x < 0 || x >= m || y < 0 || y >= n || visited[x][y] == true || arr[x][y] == 0) return
  // 방문처리
  visited[x][y] = true;

  // 상 하 좌 우 좌상 우하 우상 좌하 탐색
  dfs(x-1, y)   // 상
  dfs(x+1, y)   // 하
  dfs(x, y-1)   // 좌
  dfs(x, y+1)   // 우
  dfs(x-1, y-1) // 좌상
  dfs(x+1, y+1) // 우하
  dfs(x-1, y+1) // 우상
  dfs(x+1, y-1) // 좌하

}

for(let i = 0; i < arr.length; i++) {
  for(let j = 0; j < arr[i].length; j++) {
    if(visited[i][j] == false && arr[i][j] == 1) {
      // console.log('i, j',i, j)
      dfs(i, j);
      cnt++;
    }
  }
}

console.log(cnt)
