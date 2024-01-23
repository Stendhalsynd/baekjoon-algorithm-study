from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for neighbor in neighbors:
            newA = neighbor[0] + a
            newB = neighbor[1] + b

            if 0 <= newA < n and 0 <= newB < m and visited[newA][newB] == -1 and graph[newA][newB] == 1:
                visited[newA][newB] = visited[a][b] + 1
                queue.append((newA, newB))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0
        elif graph[i][j] == 2:
            bfs(i, j)
        

for row in visited:
    print(" ".join(map(str, row)))