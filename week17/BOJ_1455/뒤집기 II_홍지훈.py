import sys
input = sys.stdin.readline

def flip(coin, i, j):
  for x in range(i+1):
    for y in range(j+1):
      coin[x][y] = 1 - coin[x][y]

coin = []
count = 0
N, M = map(int, input().rstrip().split()) # N, M : 세로크기, 가로크기
for _ in range(N):
  input_str = input().rstrip()
  coin.append([int(status) for status in input_str])

for i in range(N-1, -1, -1):
  for j in range(M-1, -1, -1):
    if coin[i][j] == 1:
      count += 1
      flip(coin, i, j)
      
print(count)