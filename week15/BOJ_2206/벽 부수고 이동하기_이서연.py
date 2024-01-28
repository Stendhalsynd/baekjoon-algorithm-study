import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    visited[0][0][0] = 1
    
    queue = deque([(0, 0, 0)])
    
    while queue:
        cx, cy, crashed = queue.popleft()
        
        if cx == N - 1 and cy == M - 1:
            return visited[cx][cy][crashed]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][crashed] == 0:
                    visited[nx][ny][crashed] = visited[cx][cy][crashed] + 1
                    queue.append((nx, ny, crashed))
                elif graph[nx][ny] == 1 and visited[nx][ny][crashed] == 0:
                    if crashed == 1:
                        continue
                    else:
                        visited[nx][ny][1] = visited[cx][cy][crashed] + 1
                        queue.append((nx, ny, 1))
    
    return -1

print(bfs())