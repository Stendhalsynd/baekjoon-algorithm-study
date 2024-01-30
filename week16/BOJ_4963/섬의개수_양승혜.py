from collections import deque

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    dir =  [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        x, y = queue.popleft()
        for num1, num2 in dir: # 상 하 좌 우 대각선
            newX, newY = x + num1, y + num2
            if 0 <= newX < h and 0 <= newY < w and graph[newX][newY] == 1:
                graph[newX][newY] = 0
                queue.append((newX, newY))

while True:
    count = 0
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(i, j)
                count += 1
    print(count)
