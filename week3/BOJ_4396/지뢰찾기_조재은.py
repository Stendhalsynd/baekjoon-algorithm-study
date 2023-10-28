import sys

n = int(input())
mine = [list(input()) for i in range(n)] # 지뢰의 위치
open = [list(input()) for i in range(n)] # 눌러본 위치
zone = [['.'] * n for _ in range(n)] # 플레이어가 보는 위치, n개의 list를 0으로 삽입

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    for y in range(n):
        if mine[x][y] == '.' and open[x][y] == 'x': # 지뢰가 없으면서 열린칸
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if mine[nx][ny] == '*':
                    cnt += 1
            zone[x][y] = cnt # 19번의 조건 절을 통과 하지 않아도 cnt 적용

        if mine[x][y] == '*' and open[x][y] == 'x': #지롸가 있는 칸이 열렸다면
            for a in range(n):
                for b in range(n):
                    if mine[a][b] == '*':
                        zone[a][b] = '*'

for i in range(n):
    for j in range(n):
        print(zone[i][j], end = '')
    print()