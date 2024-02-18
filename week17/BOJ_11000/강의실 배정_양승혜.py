import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    classes.append(list(map(int, input().split())))

classes.sort()

heap = [classes[0][1]]

for i in range(1, n):
    if classes[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])

print(len(heap))
