import sys, collections
input = sys.stdin.readline

def bfs(x):
  global result
  visited = [0]*(N+1)
  q = collections.deque()
  q.append([x, 1]) # 현재 위치, 거리
  visited[x]=1
  while q:
    x, dist = q.popleft()
    for curr in bucket[x]: # 현재 위치에서 갈 수 있는 인덱스 순회
      if visited[curr]==0 & dist < result[curr]: # 만약 방문한 적이 없고, 최단거리인 경우 갱신 및 큐에 추가
        result[curr]=dist
        visited[curr]=1
        q.append([curr, dist+1])
  return

N, M, K, X = map(int, input().split())
# 1. 출발지별로 갈 수 있는 도착지를 리스트에 추가
bucket = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  bucket[a].append(b)

# 2. 출발지 X부터 각 인덱스까지의 최단거리를 담을 배열 초기화
INF = int(21e8)
result = [INF]*(N+1)

# 3. bfs 후 result 배열 변경
bfs(X)

# 4. 조건에 맞는 인덱스 또는 -1 출력
flag = False
for index, r in enumerate(result):
  if r==K:
    print(index)
    flag= True
if flag==False: print(-1)
