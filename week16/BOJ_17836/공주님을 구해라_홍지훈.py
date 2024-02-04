import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().rstrip().split()) # N, M: 성의 크기, T: 저주의 제한 시간
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
castle = []
for _ in range(N):
  castle.append(list(map(int, input().rstrip().split())))

visited = [[ 0 for _ in range(M)] for _ in range(N)]
q = deque([[0, 0]]) # y, x
gram = 1e9

def bfs():
  global gram
  while q:
    y, x = q.popleft()
    if castle[y][x] == 2: # 그람
      gram = visited[y][x] + N - 1 - y + M - 1 - x
    if y == N - 1 and x == M - 1: return min(visited[y][x], gram) # 공주에 도달시 그람을 얻을때와 얻지 못했을 때 최소시간을 비교
    for dy, dx in move:
      ny, nx = y + dy, x + dx
      if 0 <= ny < N and 0 <= nx < M and castle[ny][nx] != 1 and visited[ny][nx] == 0: # 이동가능하며 아직 방문하지 않았을 경우 ( 그람 or 빈공간 )
        visited[ny][nx] = visited[y][x] + 1 # 이동하고 시간 + 1
        q.append([ny, nx])
  return gram # 공주에 도달하지 못했을 때

answer = bfs()

print("Fail") if answer > T else print(answer)