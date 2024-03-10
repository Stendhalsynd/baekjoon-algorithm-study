import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, -1, 1, 1, -1, 0, 0, 1]
dy = [-1, 1, -1, 1, 0, -1, 1, 0]

def bfs(graph, queue):
    while queue:
        position = queue.popleft()
        x, y = position[0], position[1]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < N and -1 < ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs(graph, queue)

print(max(sum(graph, [])) - 1)



# 초기 코드

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# graph = []
#
# for _ in range(N):
#     graph.append(list(map(int, input().split())))
#
# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]
#
# def bfs(visited, x, y):
#     visited[x][y] = 1
#     queue = deque()
#     queue.append((x, y))
#
#     while queue:
#         position = queue.popleft()
#         px, py = position[0], position[1]
#
#         for i in range(8):
#             nx = px + dx[i]
#             ny = py + dy[i]
#
#             if -1 < nx < N and -1 < ny < M:
#                 if visited[nx][ny] == -1:
#                     if graph[nx][ny] == 1:
#                         return visited[px][py]
#                     else:
#                         visited[nx][ny] = visited[px][py] + 1
#                         queue.append((nx, ny))
#
#
# distances = []
#
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0:
#             visited = [[-1] * M for _ in range(N)]
#             distances.append(bfs(visited, i, j))
#
# print(max(distances))