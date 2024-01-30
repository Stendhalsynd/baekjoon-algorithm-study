from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def BFS(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        a, b = queue.popleft()
        for num1, num2 in moves:
            A, B = a + num1, b + num2
            if 0 <= A < n and 0 <= B < m and graph[A][B] == 1:
                graph[A][B] = 0
                queue.append([A, B])

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            BFS(i, j)
            count += 1
print(count)
