import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
seen = list(map(int, input().split()))
seen[-1] = 0

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())

    if seen[a] != 1 and seen[b] != 1:
        graph[a].append((b, c))
        graph[b].append((a, c))

INF = sys.maxsize
distance = [INF] * N

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

dijkstra(0, distance)

if distance[N - 1] == INF:
    print(-1)
else:
    print(distance[N - 1])