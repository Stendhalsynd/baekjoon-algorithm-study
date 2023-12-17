import sys
import heapq

input = sys.stdin.readline

city, road, aim, depart = map(int, input().split())

graph = [[] for _ in range(city + 1)]
distances = [1e9] * (city + 1)

for _ in range(road):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    heap = []
    distances[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, curr = heapq.heappop(heap)
        if distances[curr] > cost:
            continue

        for i in graph[curr]:
            distance = cost + 1
            if distances[i] > distance:
                distances[i] = distance
                heapq.heappush(heap, (distance, i))

dijkstra(depart)

flag = False
for i in range(city + 1):
    if distances[i] == aim:
        flag = True
        print(i)
if not flag:
    print(-1)
