def path_finding():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 3차원 리스트, 벽 깰 때와 안 꺨 때
    visited[0][0][1] = 1 # 초기 값은 벽을 깨지 않았으니까 1
    while queue:
        y, x, wall = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 0 and visited[ny][nx][wall] == 0: # 이동할 수 있고, 아직 방문하지 않았으면
                    visited[ny][nx][wall] = visited[y][x][wall] + 1 # 이동하고 거리 +1
                    queue.append([ny,nx,wall])

                if maze[ny][nx] == 1 and wall == 1: #만약 벽에 만났는데 벽을 아직 안깨봤다면
                    visited[ny][nx][wall-1] = visited[y][x][wall] + 1 #벽을 깨고 이동해보고 거리 +1
                    queue.append([ny,nx,wall-1])

    if visited[N-1][M-1][wall] != 0: # 도달할 수 있으면
        return visited[N-1][M-1][wall] # 결과 반환
    else: # 없으면
        return -1 #-1 반환 


import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[1,0], [-1,0], [0,1], [0,-1]]
queue = deque([[0,0,1]])
print(path_finding())