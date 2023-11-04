# 구현, 브루트포스 알고리즘

def iswin(row, col):
    # 현재 위치에 바둑돌이 없는 경우
    if board[row][col] == 0:
      return False
    
    # 오른쪽 위 대각선
    if row >= 4 and col <= 14 and validRightUpDiagonal(row, col): 
      # 앞으로 육목인지
      if not isValid(row, col, board, 1):
        return False
      
      # 이전 값이 존재시 다른 값인지 비교
      if not board[row + 1][col - 1] or(board[row + 1][col - 1] and board[row + 1][col - 1] != board[row][col] ):
        return True
      
    # 오른쪽 
    if col <= 14 and validRight(row, col): 
      if not isValid(row, col, board, 2):
        return False
      if not board[row][col - 1] or (board[row][col - 1] and board[row][col - 1] != board[row][col]):
        return True
      
    # 오른쪽 아래 대각선
    if row <= 14 and col <= 14 and validRightDownDiagonal(row, col): 
      if not isValid(row, col, board, 3):
        return False
      if not board[row - 1][col - 1] or (board[row - 1][col - 1] and board[row - 1][col - 1] != board[row][col]):
        return True
      
    # 아래
    if row <= 14 and validDown(row, col): 
      if not isValid(row, col, board, 4):
        return False
      if not board[row - 1][col] or (board[row - 1][col] and board[row - 1][col] != board[row][col]):
        return True
    return False

# 아래 방향 오목 존재
def validDown(row, col):
    return board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == board[row + 4][col]

# 오른쪽 아래 대각선 방향 오목 존재
def validRightDownDiagonal(row, col):
    return board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == board[row + 4][col + 4]

# 오른쪽 방향 오목 존재
def validRight(row, col):
    return board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4]

# 오른쪽 위 방향 오목 존재
def validRightUpDiagonal(row, col):
    return board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == board[row - 4][col + 4]

# 현재 좌표에서 해당 방향으로 육목인지
def isValid(row, col, board, case):
  if case == 1:   
    if row >= 5 and col <= 13 and board[row][col] == board[row - 5][col + 5]:
      return False 
  elif case == 2:   
    if col <= 13 and board[row][col] == board[row][col + 5]:
      return False
  elif case == 3:
    if row <= 13 and col <= 13 and board[row][col] == board[row + 5][col + 5]:
      return False
  elif case == 4:
    if row <= 13 and board[row][col] == board[row + 5][col]:
      return False
  return True

def game(iswin, board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if iswin(r, c):
               print(board[r][c])
               print(r + 1, c + 1)
               return
    print(0)

board = []

for _ in range(19):
    row = [int(x) for x in input().split() ]
    board.append(row)

game(iswin, board)