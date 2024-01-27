import sys
input = sys.stdin.readline
from collections import deque

# 요구사항 : 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수 출력하기

result = []

def bfs(fields, visited, X, Y, M, N):
  if visited[Y][X]: return 0, visited # 이미 카운트한 경우
  visited[Y][X] = True
  que = deque([[X, Y]])
  while que:
    next = que.popleft()

    for nx, ny in [next[0] - 1, next[1]], [next[0] + 1, next[1]], [next[0], next[1] - 1], [next[0], next[1] + 1]:
      if 0 <= nx <= M - 1 and 0 <= ny <= N - 1:
        if fields[ny][nx] and not visited[ny][nx]:
          visited[ny][nx] = True
          que.append([nx, ny])
  return 1, visited

T = int(input().rstrip()) # T: 테스트 케이스의 개수
# 1 <= M <= 50, 1 <= N <= 50, 1 <= K <= 2500
for _ in range(T): # 테스트 케이스 수만큼 테스트
  M, N, K = map(int, input().rstrip().split()) # M: 배추밭의 가로길이, N: 배추밭의 세로길이, K: 배추가 심어져 있는 위치의 개수 

  fields = [[0 for _ in range(M)] for _ in range(N)]
  visited = [[False for _ in range(M)] for _ in range(N)]
  cabbages = []

  for _ in range(K):
    X, Y = map(int, input().rstrip().split()) # X: 배추의 위치 X, Y: 배추의 위치 Y, 0 <= X <= M - 1, 0 <= Y <= N - 1
    fields[Y][X] = 1
    cabbages.append((X, Y))
  
  answer = 0

  for cabbage in cabbages:
    x, y = cabbage
    count, visited = bfs(fields, visited, x, y, M, N)
    answer += count
  result.append(answer)

[print(val) for val in result]