import sys
from collections import deque

# N, M - 배열의 크기, R - 수행해야 하는 회전의 수
N, M, R = map(int, sys.stdin.readline().rstrip().split())

matrix = []

for i in range(N):
  matrix.append([int(val) for val in list(sys.stdin.readline().rstrip().split())])


def extract_shells(matrix):
  shells = []
    
  # 반복하여 각 쉘을 추출
  for shell in range(min(N, M) // 2):
    shell_coords = []
    
    # 상단 가로
    for i in range(shell, M - shell):
      shell_coords.append(matrix[shell][i])
    
    # 오른쪽 세로
    for i in range(shell + 1, N - shell):
      shell_coords.append(matrix[i][M - shell - 1])
    
    # 하단 가로
    if shell < N - shell - 1:
      for i in range(M - shell - 2, shell - 1, -1):
        shell_coords.append(matrix[N - shell - 1][i])
    
    # 왼쪽 세로
    if shell < M - shell - 1:
      for i in range(N - shell - 2, shell, -1):
        shell_coords.append(matrix[i][shell])
    
    shells.append(shell_coords)
  
  return shells

def combine_shells(shells, rows, cols):
  matrix = [[0] * cols for _ in range(rows)]
  shell_idx = 0
    
  for shell in range(min(rows, cols) // 2):
    shell_coords = shells[shell_idx]
    
    # 상단 가로
    for i in range(shell, cols - shell):
      matrix[shell][i] = shell_coords.pop(0)
    
    # 오른쪽 세로
    for i in range(shell + 1, rows - shell):
      matrix[i][cols - shell - 1] = shell_coords.pop(0)
    
    # 하단 가로
    if shell < rows - shell - 1:
      for i in range(cols - shell - 2, shell - 1, -1):
        matrix[rows - shell - 1][i] = shell_coords.pop(0)
    
    # 왼쪽 세로
    if shell < cols - shell - 1:
      for i in range(rows - shell - 2, shell, -1):
        matrix[i][shell] = shell_coords.pop(0)
    
    shell_idx += 1
  
  return matrix


shells = extract_shells(matrix)
result = []

for stack in shells:
  deq = deque(stack)
  deq.rotate(-R)
  result.append(list(deq))

convertedMatrix = combine_shells(result, N, M)

for row in convertedMatrix:
  for col in row:
    print(col, end=' ')
  print()