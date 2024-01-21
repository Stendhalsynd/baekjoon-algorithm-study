import sys, copy
input = sys.stdin.readline

R, C = map(int, input().rstrip().split()) # R, C: 지도의 크기 R * C
grid = [] # 지도 정보를 담을 행렬

for _ in range(R):
  map = input().rstrip() # R 개 줄에 현재 지도, X 는 땅 . 은 바다
  grid.append(list(map))

new_grid = copy.deepcopy(grid)

def countSeaAround(row: int, col: int) -> int:
  sea_count = 0
  for dir in [1, 0], [-1, 0], [0, 1], [0, -1]:
    nr, nc = r + dir[0], c + dir[1]
    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
      sea_count += 1
    elif nr < 0 or nr >= R or nc < 0 or nc >= C:
      sea_count += 1
  return sea_count

def update(row: int, col: int): # 땅이 50년뒤 바다에 잠기는 경우
  sea_count = countSeaAround(row, col)
  if sea_count >= 3: new_grid[row][col] = '.'

for r in range(R):
  for c in range(C):
    if grid[r][c] == 'X': # 땅일 경우
      update(r, c)

hasUpdate = False

for r in range(R):
  for c in range(C):
    if new_grid[r][c] == 'X':
      if not hasUpdate:
        maxR, maxC, minR, minC = r, c, r, c
        hasUpdate = True
      if r > maxR: maxR = r
      if c > maxC: maxC = c
      if r < minR: minR = r
      if c < minC: minC = c

result = [''.join(row[minC: maxC + 1]) for row in new_grid[minR: maxR + 1]]

for row in result:
  print(row)