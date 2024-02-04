import sys
input = sys.stdin.readline
from collections import deque

sand_castle = [] # 1 ~ 9: 모래의 강도, 0: 모래가 없음
waves = 0 # 출력할 파도의 횟수

dy = [1, 1, 0, -1, -1, -1, 0, 1] # 아래, 왼쪽 아래, 왼쪽, 왼쪽 위, 위, 오른쪽 위, 오른쪽, 오른쪽 아래
dx = [0, -1, -1, -1, 0, 1, 1, 1]
q = deque()

# 1. 3차원 배열 형태의 모래성 sand_castle 정보 입력
H, W = map(int, input().rstrip().split()) # H, W: 모성 가로세로 격자 크기
sand_castle = [['.' for _ in range(W)] for _ in range(H)]
for i in range(H):
  row = list(input().rstrip())
  # 비어있을 경우 0으로 표시
  for j in range(W):
    if row[j] != '.': sand_castle[i][j] = int(row[j])
    else: 
      q.append([i, j]) # 비어있는 좌표를 큐에 넣기
      sand_castle[i][j] = 0

# 2. 파도가 친 횟수 카운트
visited = [[0 for _ in range(W)] for _ in range(H)]

# 3. bfs 를 통해 모래가 없는 빈 공간들을 큐에 담으며 큐가 빌 때까지 너비우선탐색을 하여 파도의 최대치를 갱신한다.
def bfs():
  global sand_castle, waves
  while q:
    c_row, c_col = q.popleft()

    for i in range(8):
      nr, nc = c_row + dy[i], c_col + dx[i]
      if nr < 0 or nr > H - 1 or nc < 0 or nc > W - 1: continue
      # 비어있는 곳 기준 주변 8방향의 새 위치에 모래성이 있다면 튼튼함을 1 감소시킨다. 
      if sand_castle[nr][nc] != 0:
        sand_castle[nr][nc] -= 1
        # 새 위치의 튼튼함보다 주변의 비어있는 곳의 수가 크거나 같을 경우, 해당 위치의 모래성은 무너진다.
        if sand_castle[nr][nc] == 0:
          visited[nr][nc] = visited[c_row][c_col] + 1
          # 한 격자의 모래성이 무너지는 순간까지 갱신된 파도의 횟수와 최대치를 비교
          waves = max(waves, visited[nr][nc]) 
          q.append([nr, nc]) # 빈 공간이 새로 생성되었으니 큐에 추가

bfs()
print(waves)