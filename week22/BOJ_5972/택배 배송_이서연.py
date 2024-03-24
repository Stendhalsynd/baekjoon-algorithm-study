import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, distance):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        w, curr = heapq.heappop(queue)

        if distance[curr] < w:
            continue

        for i in graph[curr]:
            cost = w + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

INF = sys.maxsize
distance = [INF] * (N + 1)

dijkstra(1, distance)

print(distance[-1])