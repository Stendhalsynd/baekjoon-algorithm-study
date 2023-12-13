import sys
input = sys.stdin.readline

def dfs(start, level):
  global visited
  for i in range(N):
    if lst[level][i]==1 and visited[start][i]==0:
      visited[start][i]=1
      dfs(start, i)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
  dfs(i, i)

# 표시
for v in visited:
  print(*v)
