import sys
input = sys.stdin.readline
import copy

T = int(input().rstrip()) # 테스트 케이스 수 1 ~ 10

for _ in range(T):
  n, d = map(int,input().rstrip().split()) # n : 배열의 크기, d : 각도

  group1 = [(i, i) for i in range(n)] # 주대각선 그룹 정방향
  group2 = [(i, (n + 1)//2 - 1) for i in range(n)] # 가운데 열 그룹 정방향
  group3 = [(i, n - i - 1) for i in range(n)] # 부대각선 그룹 정방향
  group4 = [((n + 1)//2 - 1, n - i - 1) for i in range(n)] # 가운데 행 그룹 역방향
  group5 = [(n - i - 1, n - i - 1) for i in range(n)] # 주대각선 그룹 역방향
  group6 = [(n - i - 1, (n + 1)//2 - 1) for i in range(n)] # 가운데 열 그룹 역방향
  group7 = [(n - i - 1, i) for i in range(n)] # 부대각선 그룹 역방향
  group8 = [((n + 1)//2 - 1, i) for i in range(n)] # 가운데 행 그룹 정방향
  dic = {0: group1, 1: group2, 2: group3, 3: group4, 4: group5, 5: group6, 6: group7, 7: group8}

  sign, rotate = d > 0, abs(d) // 45 # sign : 방향 ( true: 시계, false: 반시계 ), rotate : 얼만큼 회전해야 하는지
  inital_matrix = [ list(map(int, input().rstrip().split())) for _ in range(n)]
  copy_matrix = copy.deepcopy(inital_matrix)

  for start in range(4):
    idx = 0
    if sign:    
      idx = (start + rotate) % 8
    else:
      idx = (8 + start - rotate) % 8
    for i in range(n):
      r, c = dic[start][i]
      nr, nc = dic[idx][i]

      copy_matrix[nr][nc] = inital_matrix[r][c]
  for row in copy_matrix:
    print(*row)