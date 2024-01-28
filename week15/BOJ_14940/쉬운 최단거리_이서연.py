import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
goal = (-1, -1)

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    if goal == (-1, -1) and graph[i].count(2) != 0:
        goal = (i, graph[i].index(2))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start, visited):
    visited[start[0]][start[1]] = 0
    queue = deque([start])
    
    while queue:
        p = queue.popleft()
        
        for i in range(4):
            cx, cy = p[0], p[1]
            
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))


visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0

bfs(goal, visited)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end = " ")
    
    print()