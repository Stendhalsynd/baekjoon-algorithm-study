n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):

        # dp 배열의 값이 1일때, 그리고 보드의 값이 0이 아닐 때
        if dp[i][j] >= 1 and board[i][j] != 0:

            if i + board[i][j] < n:            # 아래로 이동
                dp[i + board[i][j]][j] += dp[i][j]

            if j + board[i][j] < n:             # 오른쪽으로 이동
                dp[i][j + board[i][j]] += dp[i][j]

# 마지막 값 출력
print(dp[-1][-1])
