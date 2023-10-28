# 제한 조건 min(n,m) % 2 = 0 => 이를 활용해서 바깥쪽 직사각형에서 안쪽 직사각형을 확인
# 확인하는 순서는 맨 좌측, 하단, 우측, 상단
# 그래서 맨 좌측의 지점이 되는 i, i를 시작지점이라고 생각하고 좌표와 array[i][i]의 값을 미리 저장
# 바꿀 좌표로 이동해서, 바꿀 좌표에 있는 값을 temp 변수에 저장
# 그리고 현재 확인중인 좌표에 이전 값을 넣어줌 => array[x][y] = value
# value 값을 temp에 저장해둔 값으로 갱신

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 배열의 크기 : n x m, 회전의 수
array = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    array.append(data)

#r회 회전하기
for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i # 맨 처음 좌표 지점
        value = array[x][y] # 맨 처음 좌표가 가진 값
        # 확인 방향 : 좌 > 하 > 우 > 상

        for j in range(i + 1, n - i): #좌
            x = j
            temp = array[x][y]
            array[x][y] = value
            value = temp

        for j in range(i + 1, m - i): #하
            y = j
            temp = array[x][y]
            array[x][y] = value
            value = temp

        for j in range(i + 1, n - i): #우
            x = n - j - 1 # -1을 해야 n=m=4 일 때 (3,3) 됨, 즉. -1을 해줘야 이전 값을 넣을 그 다음칸을 가르킬 수 있음
            temp = array[x][y]
            array[x][y] = value
            value = temp

        for j in range(i + 1, m - i): #상
            y = m - j - 1
            temp = array[x][y]
            array[x][y] = value
            value = temp

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()