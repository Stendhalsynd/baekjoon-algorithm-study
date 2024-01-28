import sys
from collections import deque

input = sys.stdin.readline

R, C, N = map(int, input().split())

graph = []

for _ in range(R):
    graph.append(list(input().strip()))

def bomb_list(bombs):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "O":
                bombs.append((i, j))

def full_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == ".":
                graph[i][j] = "O"

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def explode(bombs):
    while bombs:
        p = bombs.popleft()
        
        cx, cy = p[0], p[1]
        graph[cx][cy] = "."
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                graph[nx][ny] = "."
N -= 1

while N:
    bombs = deque()
    
    bomb_list(bombs)
    
    full_bomb()
    
    N -= 1
    
    if N == 0:
        break
        
    explode(bombs)
    
    N -= 1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end = "")

    print()