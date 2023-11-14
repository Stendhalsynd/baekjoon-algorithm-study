# 구현, 재귀
size = int(input())
stack = [0] * (size - 2)

def print_matrix(new_matrix):
    for row in new_matrix:
      print(''.join(row))
    print()

def create_matrix(matrix):
  r = len(matrix)
  c = len(matrix[0])

  nr = r + 4
  nc = c + 4

  new_matrix = [[' '] * nc for _ in range(nr)]

  # 내부 이전 matrix 채우기
  for row in range(2, nr - 2):
    for col in range(2, nc - 2):
      new_matrix[row][col] = matrix[row - 2][col - 2]

  # 외부 껍질 새로 채우기
  for col in range(nc):
    new_matrix[0][col]='*'
    new_matrix[nr - 1][col]='*'
  for row in range(nr):
    if row != 0 and row != nr -1:
      new_matrix[row][0] = '*'
      new_matrix[row][nc - 1] = '*'

  return new_matrix

def print_stars(size):
  matrix = [['*','*','*','*','*'],['*',' ',' ',' ','*'],['*',' ','*',' ','*'],['*',' ',' ',' ','*'],['*','*','*','*','*'],]

  if size == 1:
    print('*')
    return
  elif size == 2:
    print_matrix(matrix)
  else:
    while stack:
      stack.pop()
      matrix = create_matrix(matrix)
    print_matrix(matrix)

print_stars(size)