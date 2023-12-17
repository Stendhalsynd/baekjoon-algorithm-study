# import sys
# input = sys.stdin.readline

# def dfs(cur, level):
#   global max_friends
#   if level==2: return
#   for i in range(N):
#     if lst[cur][i]=='Y' and friends[i]==0:
#       friends[i] = 1
#       dfs(i, level+1)

# N = int(input())
# lst = [list(input().rstrip()) for _ in range(N)]
# max_friends = 0
# for i in range(N):
#   friends = [0]*N
#   friends[i]=1
#   dfs(i, 0)
#   max_friends = max(max_friends, sum(friends))
# print(max_friends-1)

# dfs로는 불가능
# https://hwayomingdlog.tistory.com/139



# bfs로 풂
import sys, collections
input = sys.stdin.readline

def bfs(x):
  q = collections.deque()
  q.append([x, 0]) # [cur, depth]
  visited =[False]*N
  visited[x]=True

  while q:
    cur, depth = q.popleft()
    if depth == 2: continue
    for i in range(N):
      if lst[cur][i]=='N': continue
      if visited[i]==True: continue
      visited[i]=True
      q.append([i, depth+1])
  return sum(visited)-1

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
max_count = 0
for i in range(N):
    max_count = max(max_count, bfs(i))
print(max_count)
# a와 b가 2-친구가 되기 위한 조건
# 1. 두 사람이 친구이거나
# 2. a와 친구이고 b와 친구인 c가 존재

