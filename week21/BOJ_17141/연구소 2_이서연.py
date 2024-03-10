import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

room = []

for _ in range(N):
    room.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(v, visited):
    queue = deque()

    for i in v:
        x, y = i[0], i[1]
        visited[x][y] = 0
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


    if sum(room, []).count(1) == sum(visited, []).count(-1):
        return max(sum(visited, []))
    else:
        return sys.maxsize


v_candidate = []

for i in range(N):
    for j in range(N):
        if room[i][j] == 2:
            v_candidate.append((i, j))

answer = sys.maxsize

for i in combinations(v_candidate, M):
    visited = [[-1] * N for _ in range(N)]
    answer = min(answer, bfs(i, visited))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
