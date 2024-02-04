import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().rstrip().split()) # M, N 은 현수막의 크기
info = []
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(M):
  info.append(list(map(int, input().rstrip().split())))

dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(x, y):
  visited[y][x] = True
  q = deque([(x, y)])
  while q:
    cur_x, cur_y = q.popleft()
    for i in range(8):
      nr, nc = cur_y + dr[i], cur_x + dc[i]
      if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and info[nr][nc] == 1:
        visited[nr][nc] = True
        q.append((nc, nr))

answer = 0
for r in range(M):
  for c in range(N):
    if info[r][c] == 1 and not visited[r][c]:
      bfs(c, r)
      answer += 1


print(answer)