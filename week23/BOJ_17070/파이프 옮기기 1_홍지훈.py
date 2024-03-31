# 0 → ─, 1 → /, 2 → |

def solution():
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    for r in range(1, N):
        for c in range(1, N):
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                
	    # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    
    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()

# import sys
# input = sys.stdin.readline

# INF = sys.maxsize
# N = int(input().rstrip()) # N: 집의 크기 3 ~ 16
# house = [[0] * (N + 1)] # 집의 상태, 빈칸은 0, 벽은 1, (1,1), (1,2) 는 항상 빈 칸
# start = [1, 2, 0] # y, x, status (0: 가로, 1: 대각선, 2: 세로)

# def diagonal(y, x) -> bool:
#   return True if house[y][x + 1] or house[y + 1][x] or house[y + 1][x + 1] else False

# def right(y, x) -> bool:
#   return True if house[y][x + 1] else False

# def down(y, x) -> bool:
#   return True if house[y + 1][x] else False

# def check(cur, status, dir):
#   y, x = cur[0], cur[1]
#   if status == 0: # 가로였을 때
#     if dir == 0 and right(y, x): return False, [INF, INF] # 오른쪽이고 벽이 있을 때    
#     elif dir == 1 and diagonal(y, x): return False, [INF, INF] # 대각선이고 벽이 있을 때
#     else:
#       if dir == 0: return True, [y, x + 1]
#       elif dir == 1: return True, [y + 1, x + 1]
#   elif status == 1: # 세로였을 때
#     if dir == 2 and down(y, x): return False, [INF, INF] # 아래
#     elif dir == 1 and diagonal(y, x): return False, [INF, INF]
#     else:
#       if dir == 2: return True, [y + 1, x]
#       elif dir == 1: return True, [y + 1, x + 1]
#   else: # 대각선이었을 때
#     if dir == 0 and right(y, x): return False, [INF, INF]
#     elif dir == 1 and diagonal(y, x): return False, [INF, INF]
#     elif dir == 2 and down(y, x): return False, [INF, INF]
#     else:
#       if dir == 0: return True, [y, x + 1]
#       elif dir == 1: return True, [y + 1, x + 1]
#       elif dir == 2: return True, [y + 1, x] 

# for _ in range(N):
#   house.append([0] + list(map(int, input().rstrip().split())))

# def move():
#   dp = [[INF] * (N + 1) for _ in range(N + 1)]

#   for i in range(1, N + 1):
#     for j in range(2, N + 1):

#       dp[i][j] = 