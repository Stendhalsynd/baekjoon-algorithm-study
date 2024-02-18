n, m = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(list(map(int, input())))

def flip(a, b):
    for i in range(a + 1):
        for j in range(b + 1):
            if coins[i][j] == 1:
                coins[i][j] = 0
            else:
                coins[i][j] = 1

answer = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if coins[i][j]:
            flip(i, j)
            answer += 1

print(answer)
