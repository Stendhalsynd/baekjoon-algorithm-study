import sys
input = sys.stdin.readline

dir = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]} # 0: 북, 1: 동, 2: 남, 3: 서
result = []

def update(curr_loc):
  global maxR, minR, maxC, minC
  if maxR < curr_loc[0]: maxR = curr_loc[0]
  if maxC < curr_loc[1]: maxC = curr_loc[1]
  if minR > curr_loc[0]: minR = curr_loc[0]
  if minC > curr_loc[1]: minC = curr_loc[1]

T = int(input().rstrip()) # T: 테스트 케이스의 개수

for _ in range(T):
  test_case = input().rstrip() # 테스트 케이스를 나타내는 문자열
  curr_dir = 0
  curr_loc = [0, 0]
  maxR, minR = 0, 0
  maxC, minC = 0, 0

  for command in test_case:
    if command == 'F': 
      curr_loc = [curr_loc[0] + dir[curr_dir][0], curr_loc[1] + dir[curr_dir][1]] 
      update(curr_loc) 
    elif command == 'B': 
      curr_loc = [curr_loc[0] - dir[curr_dir][0], curr_loc[1] - dir[curr_dir][1]]
      update(curr_loc) 
    elif command == 'L': curr_dir = (curr_dir - 1) % 4
    elif command == 'R': curr_dir = (curr_dir + 1) % 4

  result.append((maxR - minR) * (maxC - minC))

[print(val) for val in result]