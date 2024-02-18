import sys

input = sys.stdin.readline

N = int(input().strip())

villages = []
total = 0

for _ in range(N):
    X, A = map(int, input().split())
    villages.append([X, A])
    total += A

total /= 2

villages.sort(key=lambda x:x[0])
temp = 0

for i in range(N):
    temp += villages[i][1]

    if temp >= total:
        print(villages[i][0])
        break
