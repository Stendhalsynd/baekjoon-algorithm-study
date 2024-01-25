from collections import deque

# 입력
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# bfs 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    house = 1  # 1부터 시작(값이 1일 때부터 함수 실행되니까)

    while queue:
        a, b = queue.popleft()
        for num1, num2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newA, newB = a + num1, b + num2
            if 0 <= newA < n and 0 <= newB < n and graph[newA][newB] == 1:
                house += 1
                graph[newA][newB] = 0
                queue.append((newA, newB))
    return house

# graph의 좌표가 1일때 bfs()함수 실행, houses에 리턴값(집 개수) 저장
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append(bfs(i, j))

# 오름차순으로 정렬
houses.sort()

# 출력 - 리스트의 개수, 리스트 크기순으로 출력
print(len(houses))
for house in houses:
    print(house)
