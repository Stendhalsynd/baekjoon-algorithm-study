n, v = map(int, input().split())

# [[1, 2], [2, 3], [3, 5], [1, 4], [1, 3]] 형식으로 input값 저장
info = [list(map(int, input().split())) for _ in range(v)]

# 몇 번을 걸쳐 친구가 될지 저장할 그래프 만듦
graph = [[1e9] * n for _ in range(n)]

# 나 자신과는 친구가 될 수 없음
for same in range(n):
    graph[same][same] = 0

# 쌍방향 그래프
for num1, num2 in info:
    graph[num1 - 1][num2 - 1], graph[num2 - 1][num1 - 1] = 1, 1

# 플로이드-와샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 그래프의 값이 6보다 크면 "Big World!", 작으면 "Small World!"
answer = "Small World!"
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] > 6:
            answer = "Big World!"
            break
print(answer)
