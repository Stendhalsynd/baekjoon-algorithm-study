import sys
input = sys.stdin.readline
from collections import deque

# N * M 행렬의 미로
N, M = list(map(int,input().rstrip().split()))

maze = [ list(map(int,input().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
  queue = deque()
  queue.append((y, x))
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      newX = x + dx[i]
      newY = y + dy[i]
      if newX < 0 or newY < 0 or newX >= M or newY >= N:
        continue
      if maze[newY][newX] == 0:
        continue
      if maze[newY][newX] == 1:
        maze[newY][newX] = maze[y][x] + 1
        queue.append((newY, newX))
  return maze[N - 1][M - 1]

print(bfs(0, 0))