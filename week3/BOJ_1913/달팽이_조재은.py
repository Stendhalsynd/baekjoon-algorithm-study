import sys

n = int(sys.stdin.readline()) # n*n
find = int(sys.stdin.readline()) # 찾는 값
graph = [[0] * (n) for _ in range(n)] # 그래프

# 방향벡터 (상, 하, 좌, 우)
dx = [-1, -1, 0, 0]
dy = [0, 0, -1, -1]

# n*n의 시작 좌표 (중심점)
x, y = n//2, n//2
# 중심점에 번호 할당
graph[x][y] = 1

# 시작 번호
i = 2
# 시작 외각 크기
start = 3

# 현재 좌표가 표를 다 돌아, (0,0)이 될 때까지
while (x != 0 or y != 0):
    # 번호가 현재 외각의 크기만큼 할당될 때까지
    while (i <= start * start):

        # 현재 좌표가 현재 외각의 시작 좌표라면, 상으로 이동
        if (x == y == (n//2)):
            # 상우하좌로 이동해야하는 횟수 저장
            up, right, down, left = start, start-2, start-1, start-1
            # 상으로 이동
            x += dx[0]
            y += dy[0]
            #상으로 이동해야하는 횟수 감소
            up -= 1
        elif (right > 0): # 우
            x += dx[3]
            y += dy[3]
            right -= 1
        elif (down > 0): # 하
            x += dx[1]
            y += dy[1]
            down -= 1
        elif (left > 0): # 좌
            x += dx[2]
            y += dy[2]
            left -= 1
        elif (up > 0): # 상
            x += dx[0]
            y += dy[0]
            up -= 1

        # 현재 좌표에 번호 할당
        graph[x][y] = i
        i += 1

    n -= 2
    start += 2

# n개의 줄에 걸쳐 표를 출력
for j in range(len(graph)):
    print(*graph[j])
    if find in graph[j]:
        mx = j + 1
        my = graph[j].index(find) + 1
print(mx, my)