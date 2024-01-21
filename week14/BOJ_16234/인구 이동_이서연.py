import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

people = []

for i in range(N):
    people.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def move(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if L <= abs(people[x][y] - people[nx][ny]) <= R:
                open.append((nx, ny))
                move(nx, ny)

    return open


cnt = 0

while True:
    flag = False
    visited = [[False] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            open = [(i, j)]

            if not visited[i][j]:
                open = move(i, j)

            if len(open) > 1:
                flag = True
                num = 0

                for x, y in open:
                    num += people[x][y]

                num = int(num / len(open))

                for x, y in open:
                    people[x][y] = num

    if not flag:
        break

    cnt += 1

print(cnt)