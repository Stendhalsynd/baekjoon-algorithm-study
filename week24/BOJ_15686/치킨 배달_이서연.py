import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

def check(positions):
    global result

    chicken_distance = []

    for i in house_location:
        hx, hy = i[0], i[1]
        temp = sys.maxsize

        for j in positions:
            cx, cy = j[0], j[1]
            distance = abs(hx - cx) + abs(hy - cy)
            temp = min(temp, distance)

        chicken_distance.append(temp)

    result = min(result, sum(chicken_distance))

house_location = []
chicken_location = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_location.append((i, j))
        elif graph[i][j] == 2:
            chicken_location.append((i, j))

result = sys.maxsize

for i in range(M, 0, -1):
    for j in combinations(chicken_location, i):
        check(j)

print(result)
