import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split()) # N: 비바라기 크기, M: 구름의 이동횟수

dir = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1],
      5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
clouds = [[N, 1], [N, 2], [N-1, 1], [N-1, 2]]

def update(next: int) -> int:
  return (next - 1) % N + 1

grid = [[0 for _ in range(N + 1)]]
for _ in range(N):
  grid.append([0] + list(map(int, input().rstrip().split())))

def water_copy_bug(row, col) -> int:
  count = 0
  for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    nr, nc = row + dr, col + dc
    if 1 <= nr <= N and 1 <= nc <= N and grid[nr][nc] > 0:
      count += 1
  if 1 <= row <= N and 1 <= col <= N:
    grid[row][col] += count

def move(row: int, col: int, dr: int, dc: int):
  # 1. 구름이 di 방향으로 si 칸 이동
  nr, nc = update(row + dr), update(col + dc) 

  if 1 <= nr <= N and 1 <= nc <= N:
    # 2. 물의 양 1 증가
    grid[nr][nc] += 1
    moved_clouds.append([nr, nc])
    visited[nr][nc] = True

for _ in range(M):
  direction, dist = map(int, input().rstrip().split())
  dr, dc = dir[direction][0] * dist, dir[direction][1] * dist
  moved_clouds = deque([])

  visited = [[False] * (N + 1) for _ in range(N + 1)]
  for loc in clouds:
    curr_row, curr_col = loc[0], loc[1]
    move(curr_row, curr_col, dr, dc)

  # 3. 구름이 모두 사라진다.
  clouds = []

  # 4. 대각선 방향 물복사버그
  for loc in moved_clouds: 
    curr_row, curr_col = loc[0], loc[1]
    water_copy_bug(curr_row, curr_col)

  # 5. 물의 양 2 이상인 칸에 구름이 생기고 물의 양 2 감소, 단 앞의 3 에서 구름이 사라진 칸 제외
  for row in range(1, N + 1):
    for col in range(1, N + 1):
      if grid[row][col] >= 2 and visited[row][col] == False:
        grid[row][col] -= 2
        clouds.append([row, col])
print(sum(sum(grid, [])))