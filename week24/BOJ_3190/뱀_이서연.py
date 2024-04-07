import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

graph = [[0] * N for i in range(N)]

K = int(input().strip())

for _ in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

rotate = deque()

L = int(input().strip())

for _ in range(L):
    a, b = map(str, input().split())
    rotate.append((int(a), b))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
graph[0][0] = 1

current = deque()
current.append((0, 0))

dir = 0
cnt = 0

while True:
    cnt += 1

    x += dx[dir]
    y += dy[dir]

    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] == 1:
        print(cnt)
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        current.append((x, y))
    elif graph[x][y] == 0:
        px, py = current.popleft()
        graph[px][py] = 0

        graph[x][y] = 1
        current.append((x, y))

    if len(rotate) > 0 and cnt == rotate[0][0]:
        X, C = rotate.popleft()

        if C == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4