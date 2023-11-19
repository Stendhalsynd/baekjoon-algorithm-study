'''
1. 주어진 사탕으 n * n 모양으로 놓여있고, 빨강(c), 파랑(p), 초록(z), 노랑(y)의 4가지 색의 사탕이 존재한다.
2. 인접한 사탕이면서 서로 다른 색상일 경우에만 두 사탕의 위치를 서로 바꿔준다.
3. 핵심2의 과정을 한번 수행할 때마다 전체 사탕을 검사하여 모두 같은 색상으로만 이루어져 있는 가장 긴 부분을 찾아 최대 길이를 갱신한다.
    따라서, 구현해야할 주요 로직은 인접한 사탕이 서로 다른 색상일 경우 두 사탕의 위치를 스왑하는 부분과 주어진 n*n 사탕 배열을 돌면서 같은 색상으로
    연속된 사탕의 개수를 검사해 최대 길이를 갱신하는 부분이다.
'''

import sys
input = sys.stdin.readline

'''
같은 색상으로 연속된 사탕의 개수가 최대 몇 개인지 검사
'''

def check_candy():
    max_candy = 0
    same_candy = 0
    # 행 체크
    for x in range(n):
        same_candy = 1
        for y in range(n-1):
            if candy[x][y] == candy[x][y+1]:
                same_candy += 1
            else:
                same_candy = 1
            # 최대 개수이면 갱신
            if same_candy > max_candy:
                max_candy = same_candy

    # 열 체크
    for y in range(n):
        same_candy = 1
        for x in range(n-1):
            if candy[x][y] == candy[x+1][y]:
                same_candy += 1
            else:
                same_candy = 1
            #최대 개수면 갱신
            if same_candy > max_candy:
                max_candy = same_candy
    return max_candy

n = int(input())
candy = [list(map(str, input().rstrip())) for _ in range(n)]
result = 0

# 탐색할 방향 설정(좌우하상)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열의 범위를 벗어나는지 체크
            if 0 <= nx < n and 0 <= ny < n:
                # 인접한 사탕이 다른 색이면 둘이 교체
                if candy[x][y] != candy[nx][ny]:
                    candy[nx][ny], candy[x][y] = candy[x][y], candy[nx][ny]
                    # 교체한 후 배열에서 같은 색이 최대로 연결된 사탕 개수 검새해 더 큰 값으로 갱신
                    result = max(result, check_candy())
                    # 다른 경우도 전부 검사하기 위해 교체하기 전 상태로 복구
                    candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]

print(result)