import sys
input = sys.stdin.readline

king, rock, N = input().rstrip().split() # king: 킹의 위치, rock: 돌의 위치, N: 움직이는 횟수

dir = {'R': [0, 1], 'L': [0, -1], 'B': [-1, 0], 'T': [1, 0], 
       'RT': [1, 1], 'LT': [1, -1], 'RB': [-1, 1], 'LB': [-1, -1]}

board = [[chr(j) + str(i) for j in range(65, 73)] for i in range(8, 0, -1)]

def find_loc(coordinate):
  col = ord(coordinate[0]) - 65
  row = int(coordinate[1]) - 1
  return [row, col]

def find_coordinate(row, col):
  return chr(col + 65) + str(row + 1)

curr_king = find_loc(king)
curr_rock = find_loc(rock)

for _ in range(int(N)):
  move = input().rstrip() # move: 킹의 움직임
  dr, dc = dir[move]

  nr = curr_king[0] + dr
  nc = curr_king[1] + dc
  
  if 0 <= nr <= 7 and 0 <= nc <= 7: # 킹의 다음 예정 위치가 체크판 위에 존재할 경우
    rock_row, rock_col = curr_rock
    if nr == rock_row and nc == rock_col: # 킹의 다음 예정 위치가 돌의 현재 위치와 같을 때
      rock_nr = nr + dr
      rock_nc = nc + dc
      if 0 <= rock_nr <= 7 and 0 <= rock_nc <= 7: # 돌의 다음 위치가 체스판 위에 존재시,
        curr_rock = [rock_nr, rock_nc]
        curr_king = [nr, nc]     
      else: # 돌의 다음 위치가 체스판 위에 존재하지 않을 경우
        pass
    else:
      curr_king = [nr, nc]

print(find_coordinate(curr_king[0], curr_king[1]))
print(find_coordinate(curr_rock[0], curr_rock[1]))