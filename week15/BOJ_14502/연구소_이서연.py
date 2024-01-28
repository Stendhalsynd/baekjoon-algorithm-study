import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    
    new_graph = copy.deepcopy(graph)
    
    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                queue.append((i, j))
        
    while queue:
        cx, cy = queue.popleft()
            
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
                
            if 0 <= nx < N and 0 <= ny < M:
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    queue.append((nx, ny))

    result = max(result, sum(new_graph, []).count(0))


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return 
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                
                make_wall(cnt)
                
                graph[i][j] = 0
                cnt -= 1


result = 0

make_wall(0)

print(result)