import sys
input = sys.stdin.readline
from collections import deque

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x: int, y: int, w: int, h: int):
  visited[y][x] = True
  q = deque([(x, y)])
  while q:
    cur_x, cur_y = q.popleft()
    for i in range(8):
      nr, nc = cur_y + dr[i], cur_x + dc[i]
      if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and data[nr][nc] == 1:
        visited[nr][nc] = True
        q.append((nc, nr))

w, h = map(int, input().rstrip().split()) # w, h: 지도의 너비, 높이
result = []

while w != 0 or h != 0:
  data = []
  island = 0
  visited = [[False for _ in range(w)] for _ in range(h)]
  for _ in range(h):
    data.append(list(map(int, input().rstrip().split())))
  
  for r in range(h):
    for c in range(w):
      if data[r][c] == 1 and not visited[r][c]:
        bfs(c, r, w, h)
        island += 1

  result.append(island)
  w, h = map(int, input().rstrip().split()) # w, h: 지도의 너비, 높이

[print(v) for v in result]