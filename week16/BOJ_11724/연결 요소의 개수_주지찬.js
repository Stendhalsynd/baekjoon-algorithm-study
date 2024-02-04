const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input[0].split(' ').map(Number);

// 노드에 이어진 배열 만들기
const arr = [];
for(let i = 0; i <= n; i++) {
  arr[i] = []
}

const visited = [];
for(let i = 1; i <= n; i++) {
  visited[i] = false;
}

// 배열에 채워넣기
// 방문 테이블 만들기
for(let i = 1; i <= m; i++) {
  const [u, v] = input[i].split(' ').map(Number)
  arr[u].push(v)
  arr[v].push(u)    
}
// console.log(arr)
// console.log(visited)

let cnt = 0;
for(let i = 1; i < arr.length; i++) {
  if(visited[i] == false) {
    dfs(i)  
    cnt++
  }
  
}

function dfs(node) {
  // console.log('node',node)
  visited[node] = true;
  for(const item of arr[node]) {
    if(visited[item] == false) {  
      dfs(item)  
    }
  }
}
console.log(cnt)
