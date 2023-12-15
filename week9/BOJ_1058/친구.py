import sys 
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # N : 사람의 수
graph = [[INF] * (N + 1) for _ in range(N + 1)]
max_two_friend = 0

# 친구관계 확인
for i in range(1, N + 1):
  info = list(input().rstrip())
  for j, val in enumerate(info):
    if val == 'Y':
      graph[i][j + 1] = 1

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

for a in range(1, N + 1):
  count = 0
  for b in range(1, N + 1):
    if graph[a][b] == 1 or graph[a][b] == 2:
      count += 1
    if count > max_two_friend:
      max_two_friend = count
  
print(max_two_friend)