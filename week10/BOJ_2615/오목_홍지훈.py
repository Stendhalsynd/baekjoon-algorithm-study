import sys
input = sys.stdin.readline

matrix = []

for _ in range(19):
  rows = list(map(int, input().rstrip().split()))
  matrix.append(rows)

def is_win(r, c):
  if matrix[r][c] == 0:
    return False
  # 오른쪽 가로방향 오목 충족
  if c < 15 and matrix[r][c] == matrix[r][c + 1] == matrix[r][c + 2] == matrix[r][c + 3] == matrix[r][c + 4]:
    # 육목 방지
    if c == 14 and matrix[r][c] != matrix[r][c - 1] or c == 0 and matrix[r][c] != matrix[r][c + 5]:
      return True
    elif 0 < c < 14:
      if matrix[r][c] != matrix[r][c + 5] and matrix[r][c - 1] != matrix[r][c]:
        return True

  # 아래 세로방향 오목 충족
  if r < 15 and matrix[r][c] == matrix[r + 1][c] == matrix[r + 2][c] == matrix[r + 3][c] == matrix[r + 4][c]:
    # 육목 방지
    if r == 14 and matrix[r][c] != matrix[r - 1][c] or r == 0 and matrix[r][c] != matrix[r + 5][c]:
      return True
    elif 0 < r < 14:
      if matrix[r][c] != matrix[r + 5][c] and matrix[r - 1][c] != matrix[r][c]:
        return True
    
  # 오른쪽 아래 방향 대각선 오목 충족
  if r < 15 and c < 15 and matrix[r][c] == matrix[r + 1][c + 1] == matrix[r + 2][c + 2] == matrix[r + 3][c + 3] == matrix[r + 4][c + 4]:
    # 육목 방지
    if r == 14 and (c == 0 or matrix[r][c] != matrix[r - 1][c - 1]) or c == 14 and (r == 0 or matrix[r][c] != matrix[r - 1][c - 1]) or r == 0 and matrix[r][c] != matrix[r + 5][c + 5] or c == 0 and matrix[r][c] != matrix[r + 5][c + 5]:
      return True
    elif 0 < r < 14 and 0 < c < 14:
      if matrix[r][c] != matrix[r + 5][c + 5] and matrix[r - 1][c - 1] != matrix[r][c]:
        return True

  # 오른쪽 위 방향 대각선 오목 충족 
  if r > 3 and c < 15 and matrix[r][c] == matrix[r - 1][c + 1] == matrix[r - 2][c + 2] == matrix[r - 3][c + 3] == matrix[r - 4][c + 4]:
    # 육목 방지
    if r == 4 and (c == 0 or matrix[r][c] != matrix[r + 1][c - 1]) or c == 14 and (r == 18 or matrix[r][c] != matrix[r + 1][c - 1]) or r == 18 and (c == 14 or matrix[r][c] != matrix[r - 5][c + 5]) or c == 0 and (r == 4 or matrix[r][c] != matrix[r - 5][c + 5]):
      return True
    elif 4 < r < 18 and 0 < c < 14:
      if matrix[r][c] != matrix[r - 5][c + 5] and matrix[r + 1][c - 1] != matrix[r][c]:
        return True
    
  return False

def game():
  for r in range(19):
    for c in range(19):
      if is_win(r, c):
        print(matrix[r][c])
        print(r + 1, c + 1)
        return
  print(0)

game()