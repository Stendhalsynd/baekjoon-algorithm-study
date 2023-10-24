import sys, math

N = int(sys.stdin.readline().rstrip()) # 3 ~ 999 범위의 홀수인 자연수
M = int(sys.stdin.readline().rstrip()) # 위치를 찾고싶은 N^2 이하의 자연수

answer = [[0] * N for _ in range(N)]
point = [N // 2, N // 2]
direction = ([0, -1], [1, 0], [0, 1], [-1, 0])
loc = []

distance = [ math.ceil(idx / 2) for idx in range(1, 2 * N)]
distance[-1] = distance[-2]

num = 0
for idx, dis in enumerate(distance):
  dir = direction[idx % 4]
  for i in range(1, dis + 1):
    dx, dy = dir
    row, col = point[0], point[1]
    num += 1
    answer[row][col] = num
    if num == M: loc = [row + 1, col + 1]
    newX, newY = col + dx, row + dy
    point = [newY, newX]

answer[0][0] = N * N
isTarget = False
loc = []

for i in range(N):
  for j in range(N):
    if answer[i][j] == M:
      loc.append(i + 1)
      loc.append(j + 1)
      isTarget = True
      break
  if isTarget: break


for row in answer:
  for col in row:
    print(col, end=" ")
  print(end='\n')

print(loc[0], loc[1])

