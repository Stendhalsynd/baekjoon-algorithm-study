const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m, t] = input[0].split(' ').map(Number)         // 성의크기, 제한시간

let castle = [];                                          // 성 모양의 배열 만들기
for(let i = 1; i <= n; i++) {
  castle.push(input[i].split(' ').map(Number))
}
const dx = [1, -1, 0, 0]                                  // 상 하
const dy = [0, 0, 1, -1]                                  // 좌 우우

function gram(a, b) {                                     // 칼을 만났을때의 최단 거리
  const q = []                                            // queue 생성
  q.push({row : a, col : b, count : 0})                   // 현재 좌표와 도달한 시간

  let visited = [];                                       // 방문처리 배열 만들기
  for(let i = 1; i <= n; i++) {
    visited.push(Array(m).fill(false))
  }
  visited[a][b] = true;                                   // 방문처리하기

  while(q) {                                              // bfs 시작
    const temp = q.shift();                               // q에서 하나 뽑아온다
    if(temp == undefined) return t + 1                    // 만약 뽑아올게 없다면 제한시간 + 1 을 리턴해 예외처리해준다

    const x = temp.row                                    // row 좌표
    const y = temp.col                                    // col 좌표
    const count = temp.count                              // 도달한 시간
    if(castle[x][y] == 2) {                               // 만약 칼을 만났다면 
      return count + (n + m - x - y - 2)                  // 공주의 좌표에서 칼의 좌표를 계산 해준다.
    }
    for(let i = 0; i < 4; i++) {                          // 상하 좌우 탐색 실시한다
      const nx = dx[i] + x
      const ny = dy[i] + y
      if(nx < n && ny < m && nx >= 0 && ny >= 0) {        // 말단 예외처리
        if(castle[nx][ny] != 1 && !visited[nx][ny]) {     // 벽이 아니고 방문하지않았다면
          visited[nx][ny] = true                          // 방문 처리 후
          q.push({row : nx, col : ny, count : count + 1}) // queue에 삽입한다
        }
      }
    }
  }
  return t + 1                                            // bfs순회 하였음에도 불구하고 값을 못구했다면 한시간 + 1 을 리턴해 예외처리해준다
}

function princess(a, b) {                                 // bfs 순회한다.
  const q = [];
  q.push({row : a, col : b, count : 0})
  
  let visited = [];
  for(let i = 1; i <= n; i++) {
    visited.push(Array(m).fill(false))
  }
  visited[a][b] = true;
  while(q) {
    const temp = q.shift();
    if(temp == undefined) return t + 1
    const x = temp.row
    const y = temp.col
    const count = temp.count

    if(x == n - 1 && y == m - 1) {
      return count
    }

    for(let i = 0; i < 4; i++) {
      const nx = dx[i] + x
      const ny = dy[i] + y
      if(nx < n && ny < m && nx >= 0 && ny >= 0) {
        if(castle[nx][ny] != 1 && !visited[nx][ny]) {
          visited[nx][ny] = 1
          q.push({row : nx, col : ny, count : count + 1})
        }
      }
    }
  }
  return t + 1
}

const p = princess(0, 0)          // 단순 bfs순회와
const g = gram(0, 0)              // 칼을 만났을때의 순회를
const result = Math.min(p, g)     // 비교하여 낮은값을 할당한다.

if(result <= t) {                 // 만약 그 값이 제한시간 안에 해당 된다면
  console.log(result)             // 값을 출력하고
} else {                          // 만약 그 값이 제한시간 안에 해당 되지 않는다면
  console.log('Fail')             // Fail을 출력한다.
}
