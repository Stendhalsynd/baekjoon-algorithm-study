import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N : 게임 판의 크기, 4 ~ 100
dp = []

for _ in range(N):
  row = list(map(int, input().rstrip().split()))
  dp.append([[val, 0] for val in row])

def update(r, c, curr, start = False):
    if curr + c < N: # col 방향 경로 존재할 때
      dp[r][c + curr][1] = 1 if start else dp[r][c + curr][1] + dp[r][c][1]
    if curr + r < N: # row 방향 경로 존재할 때
      dp[r + curr][c][1] = 1 if start else dp[r + curr][c][1] + dp[r][c][1]

for r in range(N):
  for c in range(N):
    curr = dp[r][c][0]
    if r == 0 and c == 0:
      update(r, c, curr, True)
    elif r != N - 1 or c != N - 1:
      if dp[r][c][1] != 0:
        update(r, c, curr)

print(dp[N-1][N-1][1])