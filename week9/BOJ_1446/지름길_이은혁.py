# import heapq
# # 다익스트라

# def dijkstra(start):
#     heapq.heappush(heap, (0, start))  #비용, 목적지
#     res[start] = 0

#     while heap:
#         distance, node = heapq.heappop(heap)

#         if res[node] < distance: continue
#         for i in lst[node]:

# n, d = map(int, input().split())
# lst = [[] for _ in range(n)]
# for _ in range(n):
#     a,b,c = map(int, input().split())
#     lst[a].append([b, c]) # lst[시작] = [도착, 비용]
# inf = 21e8
# res = [inf]*n
# heap = []
# dijkstra(0)

import sys
input = sys.stdin.readline

def dfs(location, dist):
  global min_dist
  if location > D: return
  elif location==D:
    if dist < min_dist: min_dist = dist
    return
  if dist > min_dist: return
  for i in range(N): # 지름길로 가는 경우
    start, end, d = lst[i]
    if location <= start:
      dfs(end, dist+d+(start-location))
  dfs(D, dist+D-location) # 나머지를 지름길 없이 가는 경우

N, D = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
min_dist = int(21e8)
dfs(0, 0)
print(min_dist)
