import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input().strip())

delivery = []

for _ in range(M):
    delivery.append(list(map(int, input().split())))

delivery.sort(key=lambda x:(x[1], x[0]))

available = [0] * N
result = 0

for start, end, weight in delivery:
    box = weight

    for i in range(start, end):
        box = min(box, C - available[i])

    for i in range(start, end):
        available[i] += box

    result += box

print(result)
