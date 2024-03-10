import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = []

for _ in range(R):
    graph.append(list(input().strip()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


possible = True

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if -1 < x < R and -1 < y < C:
                    if graph[x][y] == "W":
                        possible = False
                        break
                    elif graph[x][y] == ".":
                        graph[x][y] = "D"

if not possible:
    print(0)
else:
    print(1)
    for i in range(R):
        print("".join(graph[i]))