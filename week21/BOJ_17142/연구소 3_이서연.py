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

def bfs(v, visited1, visited2):
    queue1 = deque()
    queue2 = deque()

    for i in v:
        x, y = i[0], i[1]
        visited1[x][y] = 0
        visited2[x][y] = 0
        queue1.append((x, y))
        queue2.append((x, y))

    while queue1:
        x, y = queue1.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == 0 and visited1[nx][ny] == -1:
                visited1[nx][ny] = visited1[x][y] + 1
                queue1.append((nx, ny))

    if sum(room, []).count(1) + sum(room, []).count(2) == sum(visited1, []).count(-1) + sum(visited1, []).count(0):
        temp1 = max(sum(visited1, []))
    else:
        temp1 = sys.maxsize

    while queue2:
        x, y = queue2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != 1 and visited2[nx][ny] == -1:
                visited2[nx][ny] = visited2[x][y] + 1
                queue2.append((nx, ny))

    if sum(room, []).count(1) == sum(visited2, []).count(-1):
        temp2 = max(sum(visited2, []))
    else:
        temp2 = sys.maxsize

    if temp1 != sys.maxsize:
        return temp1
    elif temp1 == sys.maxsize and temp2 != sys.maxsize:
        return temp2
    else:
        return sys.maxsize


v_candidate = []

for i in range(N):
    for j in range(N):
        if room[i][j] == 2:
            v_candidate.append((i, j))

answer = sys.maxsize

for i in combinations(v_candidate, M):
    visited1 = [[-1] * N for _ in range(N)]
    visited2 = [[-1] * N for _ in range(N)]
    answer = min(answer, bfs(i, visited1, visited2))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)