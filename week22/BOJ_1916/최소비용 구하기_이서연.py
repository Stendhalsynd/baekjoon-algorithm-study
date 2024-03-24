import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

start, end = map(int, input().split())

INF = sys.maxsize
distance = [INF] * (N + 1)

def dijkstra(start, distance):
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        w, curr = heapq.heappop(queue)

        if distance[curr] < w:
            continue

        for i in graph[curr]:
            cost = w + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start, distance)
print(distance[end])
