import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def calculate(pairs):
    global result
    visited = [[False] * N for _ in range(N)]
    temp = 0

    for i in pairs:
        x, y = i[0], i[1]

        if visited[x][y]:
            return

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if visited[nx][ny]:
                    return

                visited[nx][ny] = True
                temp += graph[nx][ny]

        visited[x][y] = True
        temp += graph[x][y]

    result = min(result, temp)


possible = []

for i in range(1, N - 1):
    for j in range(1, N - 1):
        possible.append((i, j))

result = sys.maxsize

for i in combinations(possible, 3):
    calculate(i)

print(result)