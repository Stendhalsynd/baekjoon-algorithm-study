import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split()) # n, m: 지도의 세로, 가로의 크기 
field = []
for _ in range(n):
  field.append(list(map(int, input().rstrip().split())))
visited = [[-1 for _ in range(m)] for _ in range(n)]

def bfs(x: int, y: int):
  visited[y][x] = 0
  que = deque([(x, y)])
  
  while que:
    curr_x, curr_y = que.popleft()
    for dx, dy in [1, 0], [-1, 0], [0, 1], [0, -1]:
      nx, ny = curr_x + dx, curr_y + dy
      if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and visited[ny][nx] == -1:
        if field[ny][nx] == 0:
          visited[ny][nx] = 0
        elif field[ny][nx] == 1:
          visited[ny][nx] = visited[curr_y][curr_x] + 1
          que.append((nx, ny))

for r in range(n):
  for c in range(m):
    if field[r][c] == 2 and visited[r][c] == -1:
      bfs(c, r)

for r in range(n): # 시작점으로부터 연결된 지점들과 이어지지 않는 0을 탐색
  for c in range(m):
    if field[r][c] == 0:
      visited[r][c] = 0

for row in visited:
  for col in row:
    print(col, end=' ')
  print()