# 주어진 판으로 빙고 게임을 할 때, 언제 세 번째 빙고가 완성되는지 출력하는 문제
# 딕셔너리 자료형을 이용해 순서가 들어오는 대로 각 숫가젱 맞는 보드판의 위치를 기록
# 사회자가 숫자를 부를 때, 그 수를 키로 이용하여 바로 보드에 해당하는 곳의 위치를 기록
# 숫자가 기록될 때마다 보드판을 순환하며 빙고가 몇 갠지 세고, 만약 3개 이상이라면 횟수 출력

import sys
input = sys.stdin.readline

# 숫자들의 위치 기록
board = dict()
check = [[0] * 5 for i in range(5)] # 5x5, 0으로 채우기

# 철수의 빙고판
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        board[a[j]] = (i,j)     # 철수가 적은 숫자의 인덱스 (i,j) 확인
                                # 출력값 : 11은 (0, 0)에 위치, 12은 (0, 1)에 위치
tick = 0 # 빙고 숫자

# 사회자가 부르는 수
for _ in range(5):
    a = list(map(int, input().split()))
    for i in range(5):
        tick += 1

        # 불린 숫자 a[i]가 보드에 있을 경우
        if a[i] in board:
            # 딕셔너리를 이용해 기록
            # 불려진 숫자를 0으로 채워진 리스트에 a[i]의 위치에 1을 넣음
            check[board[a[i]][0]][board[a[i]][1]] = 1

            bingo = 0

            # 일자 선
            for j in range(5):
                # 가로
                if sum(check[j]) == 5:
                    bingo += 1
                # 세로
                # check에서 각 리스트(k)의 j번째 요소를 추출합니다.
                if sum([k[j] for k in check]) == 5:
                    bingo += 1

            # 우 대각선
            if check[0][4] + check[1][3] + check[2][2] + check[1][3] + check[4][0] == 5:
                bingo += 1
            # 좌 대각선
            if check[0][0] + check[0][1] + check[2][2] + check[3][3] + check[4][4] == 5:
                bingo += 1

            if bingo >= 3:
                print(tick)
                sys.exit()