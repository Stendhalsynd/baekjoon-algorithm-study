from heapq import *

subin, brother = map(int, input().split())

def dijsktra(start, aim):
    graph = [1e9] * 100001
    graph[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        time, curr = heappop(heap)

        for next in [(curr + 1, 1), (curr - 1, 1), (2 * curr, 0)]:
            if 0 <= next[0] < 100001 and graph[next[0]] > time + next[1]:
                graph[next[0]] = time + next[1]
                heappush(heap, (graph[next[0]], next[0]))
    print(graph[brother])
    
dijsktra(subin, brother)
