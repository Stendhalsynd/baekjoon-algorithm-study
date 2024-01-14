import sys, math
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().rstrip().split()) # N: 격자의 크기, M: 파이어볼의 수, K: 이동 수
grid = [[[] for _ in range(N + 1)] for _ in range(N + 1)] # grid: 격자
dr = [-1, -1, 0, 1, 1, 1, 0, -1] # dr: 파이어볼 행 방향
dc = [0, 1, 1, 1, 0, -1, -1, -1] # dc: 파이어볼 열 방향
info = deque([list(map(int, input().rstrip().split())) for _ in range(M)]) # (r, c): 파이어볼의 위치, m: 질량, s: 속력, d: 방향

def all_even_or_odd(lst: list) -> bool:
  direction = [cell[4] for cell in lst]
  return all(d % 2 == 0 for d in direction) or all(d % 2 == 1 for d in direction)

# K 번 이동
for _ in range(K):
  curr_count = len(info)

  # 1단계 - 각 파이어볼이 이동한 결과 새 이동정보를 업데이트하고 grid 에 해당 좌표에 존재하는 파이어볼의 수 카운트
  for i in range(curr_count):
    r, c, m, s, d = info[i]
    nr, nc = (r + dr[d] * s - 1) % N + 1 , (c + dc[d] * s - 1) % N + 1
    grid[nr][nc].append([nr, nc, m, s, d])
    info.append([nr, nc, m, s, d])
  
  [info.popleft() for _ in range(curr_count)]
    
  # 2단계 - 2개 이상 존재하는 곳 찾기
  for r in range(1, N + 1):
    for c in range(1, N + 1):
      if len(grid[r][c]) < 2: continue
      new_weight = math.floor(sum(cell[2] for cell in grid[r][c]) / 5)
      new_velocity = math.floor(sum(cell[3] for cell in grid[r][c]) / len(grid[r][c]))
      is_even = all_even_or_odd(grid[r][c])

      if new_weight == 0: 
        grid[r][c] = []
        continue # 2단계 - 4
      grid[r][c] = [[ r, c , new_weight, new_velocity, i * 2] if is_even else [ r, c , new_weight, new_velocity, i * 2 + 1] for i in range(4)] # 2단계 - 3

  info = deque([])

  for r in range(1, N + 1):
    for c in range(1, N + 1):
      if grid[r][c]:
        for fireball in grid[r][c]:
          info.append(fireball)
        grid[r][c] = []

result = 0
for fireball in info:
  result += fireball[2] 

print(result)