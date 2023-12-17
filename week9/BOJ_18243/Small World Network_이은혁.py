import sys, collections
input = sys.stdin.readline

def bfs(index):
  q = collections.deque()
  q.append([index, 0]) #[index, depth]
  visited = [0]*(N+1)
  flag = True
  while q:
    index, depth = q.popleft()
    if depth>6: flag = False
    for i in range(1, N+1):
      if lst[index][i]==1 and visited[i]==0:
        visited[i]=1
        q.append([i, depth+1])

  return flag and sum(visited)==N


N, K = map(int , input().split())

lst = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
  a, b = map(int, input().split())
  lst[a][b] = lst[b][a] = 1

for i in range(1, N+1):
  if bfs(i)==False and N!=1:
    print("Big World!")
    break
else:
  print("Small World!")