import sys 
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split()) # N : 사람의 수, K : 친구 관계의 개수
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 친구관계 확인
for _ in range(K):
  A, B = map(int, input().split())
  graph[A][B] = 1
  graph[B][A] = 1

# 자신과는 친구가 아니다.
for a in range(1, N + 1):
  for b in range(1, N + 1):
    if a == b:
      graph[a][b] = 0

# 플로이드 - 워셜
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

def isSmallWorld():
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      if graph[a][b] >= 7:
        return False
  return True
  
print('Small World!' if isSmallWorld() else 'Big World!')