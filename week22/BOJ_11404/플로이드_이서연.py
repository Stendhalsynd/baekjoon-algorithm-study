import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    temp = [INF] * (n + 1)
    temp[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        w, curr = heapq.heappop(queue)

        if temp[curr] < w:
            continue

        for i in graph[curr]:
            cost = w + i[1]

            if cost < temp[i[0]]:
                temp[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return temp

INF = sys.maxsize
distance = []

for i in range(1, n + 1):
    distance.append(dijkstra(i))

for i in range(n):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()