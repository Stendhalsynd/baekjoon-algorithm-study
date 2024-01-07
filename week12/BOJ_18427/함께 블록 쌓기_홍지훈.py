import sys
input = sys.stdin.readline

'''
dp[i][j] : i 번째 사람까지 계산한 j 를 만들기 위한 모든 경우의 수
| 학생 |  0  |  1  |  2  |  3  |  4  |  5  |
| --- | --- | --- | --- | --- | --- | --- |
|  0  |  1  |  0  |  0  |  0  |  0  |  0  |
|  1  |  1  |  0  |  1  |  1  |  0  |  1  |
|  2  |  1  |  0  |  1  |  2  |  0  |  3  |
|  3  |  1  |  1  |  2  |  4  |  3  |  6  |

1 -> dp[1][2] = dp[1][2] + dp[1 - 1][2 - 2]
1 -> dp[1][3] = dp[1][3] + dp[1 - 1][3 - 3]
1 -> dp[1][5] = dp[1][5] + dp[1 - 1][5 - 5]

2 -> dp[2][3] = dp[2][3] + dp[2 - 1][3 - 3]
2 -> dp[2][5] = dp[2][5] + dp[2 - 1][5 - 3] + dp[2 - 1][5 - 5]

3 -> dp[3][1] = dp[3][1] + dp[3 - 1][1 - 1]
3 -> dp[3][2] = dp[3][2] + dp[3 - 1][2 - 2]
3 -> dp[3][3] = dp[3][3] + dp[3 - 1][3 - 1] + dp[3 - 1][3 - 3]
3 -> dp[3][4] = dp[3][4] + dp[3 - 1][4 - 1] + dp[3 - 1][4 - 2]
3 -> dp[3][5] = dp[3][5] + dp[3 - 1][5 - 1] + dp[3 - 1][5 - 2] + dp[3 - 1][5 - 3]
'''

N, M, H = map(int, input().rstrip().split()) # N: 학생의 수, M: 최대 블록의 수, H: 탑의 높이
dp = [[1] + [0 for _ in range(H)] for _ in range(N + 1)]

for i in range(1, N + 1):
  dp[i] = dp[i - 1].copy()
  blocks = list(map(int,input().rstrip().split()))
  for block in blocks:
    for j in range(block, H + 1):
      dp[i][j] = dp[i][j] + dp[i - 1][j - block]

print(dp[N][H] % 10007)