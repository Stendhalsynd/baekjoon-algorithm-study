import sys
from collections import deque

T = int(input().strip())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, visited):
    visited[x][y] = True

    queue = deque()
    queue.append((x, y))
    
    while queue:
        vx, vy = queue.popleft()

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    
                    
def calculate():
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for i, j in exist:
        if not visited[i][j]:
            bfs(i, j, visited)
            cnt += 1
    
    print(cnt)


for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    
    exist = []
    
    for _ in range(K):
        x, y = map(int, input().split())
        exist.append((y, x))
        graph[y][x] = 1
    
    calculate()