import sys
input = sys.stdin.readline
import copy

N = int(input().rstrip())
colors = [list(input().rstrip()) for _ in range(N)]

# 현재 행 또는 열에서 연속으로 존재하는 가장 긴 값
def find_longest_length(input):
  max_length = 1
  curr_length = 0
  before_char = ''

  for char in input:
    if char != before_char:
      curr_length, before_char = initiate(char)
    elif char == before_char:
      curr_length += 1
      max_length = max(max_length, curr_length)
    else:
      curr_length = 0
  return max_length

# 길이 초기화
def initiate(char):
  before_char = char
  curr_length = 1
  return curr_length,before_char

# 행렬 transpose
def transpose(matrix):
  for i in range(len(matrix)):
    for j in range(i):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  return matrix

# 현재 행렬에서 먹을 수 있는 사탕의 최대 개수
def find_longest_in_matrix(matrix):
  max_count = 0

  for row in matrix:
    max_count = max(max_count, find_longest_length(row))

  for col in transpose(matrix):
    max_count = max(max_count, find_longest_length(col))
  
  return max_count

# 가로로 인접한 사탕간에 교환
def exchange(matrix, row, col):
  matrix[row][col], matrix[row][col + 1] = matrix[row][col + 1], matrix[row][col]
  return matrix

# 상근이가 먹을 수 있는 사탕의 최대 개수
def solve(matrix):
  max_value = 0
  max_value = max(find_max_val(matrix, max_value), find_max_val(transpose(matrix), max_value))
  print(max_value)

def find_max_val(matrix, max_value):
    for row in range(len(matrix)):
      for col in range(len(matrix[0]) - 1):
        if matrix[row][col] == matrix[row][col + 1]:
          continue
        changed_matrix = exchange(copy.deepcopy(matrix), row, col)
        max_value = max(max_value, find_longest_in_matrix(changed_matrix))
    return max_value

solve(colors)