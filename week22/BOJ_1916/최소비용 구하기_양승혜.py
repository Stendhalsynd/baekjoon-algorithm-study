import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(graph, start):
    dist = [1e9] * (n + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            distance = cost + next_cost
            if distance < dist[next_node]:
                dist[next_node] = distance
                heapq.heappush(heap, [distance, next_node])
    return dist

result = dijkstra(graph, start)
print(result[end])
