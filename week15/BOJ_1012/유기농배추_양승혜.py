import sys
from collections import deque

input = sys.stdin.readline

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    farm[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for move in moves:
            newX = x + move[0]
            newY = y + move[1]
            if 0 <= newX < length and 0 <= newY < width and farm[newX][newY] == 1:
                farm[newX][newY] = 0
                queue.append((newX, newY))


for _ in range(int(input())):
    worm = 0
    width, length, n = map(int, input().split())
    farm = [[0] * width for _ in range(length)]

    for _ in range(n):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(length):
        for j in range(width):
            if farm[i][j] == 1:
                bfs(i, j)
                worm += 1
    print(worm)