import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, graph, visited, num):
    graph[a][b] = num
    visited[a][b] = True
    
    queue = deque()
    queue.append((a, b))
    
    while queue:
        p = queue.popleft()
        cx, cy = p[0], p[1]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    graph[nx][ny] = num
                    visited[nx][ny] = True
                    queue.append((nx, ny))

visited = [[False] * N for _ in range(N)]
num = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            if not visited[i][j]:
                num += 1
                bfs(i, j, graph, visited, num)

print(num)

temp = sum(graph, [])
result = []

for i in range(num):
    result.append(temp.count(i + 1))

result.sort()

for i in range(num):
    print(result[i])