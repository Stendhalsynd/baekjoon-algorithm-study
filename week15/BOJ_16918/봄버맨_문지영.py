import sys

input = lambda: sys.stdin.readline().rstrip()
R, C, N = map(int, input().split())

#초기 그래프 입력받음
matrix = [list(input()) for _ in range(R)]

#먼저 초기 폭탄이 설치된 자리를 저장함 (1 초)
boompos = [] #처음 폭탄자리 저장
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'O':
            boompos.append([i, j])

#그 다음 '.' -> '0'으로 바꿔주는 함수 (짝수 초)
def set_boom(matrix):
    next_boom = set() #다음 폭탄 지정 위치 저장
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '.':
                next_boom.add((i, j))
                matrix[i][j] = 'O'
    return next_boom

#폭발시키는 함수
def boom(matrix, boompos, next_boom):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    destroypos = set() 
    for x, y in boompos:
        destroypos.add((x, y)) #폭발한는 위치 저장
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < R and 0 <= ny and ny < C:
                destroypos.add((nx, ny)) #주변도 폭발하는 위치 저장

    for x, y in destroypos: #직전에 설치한 폭탄이 터지면 직전 설치 집합에서 해당 폭탄 제거
        if (x, y) in next_boom:
            next_boom.remove((x, y))
        matrix[x][y] = '.'
        

time = 1
while time < N:
    next_boom = set_boom(matrix) #
    time += 1
    if time == N:
        break
    boom(matrix, boompos, next_boom)
    boompos = next_boom #하나씩 넘어감
    time += 1

for m in matrix:
    print("".join(m))