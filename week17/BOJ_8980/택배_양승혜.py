import sys
input = sys.stdin.readline

towns, maxWeight = map(int, input().split())
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

infos.sort(key = lambda x: x[1])

deliver = [maxWeight] * (towns + 1)
answer = 0

for start, end, weight in infos:
    temp = weight
    for i in range(start, end):
        temp = min(temp, deliver[i])
    temp = min(temp, weight)
    for i in range(start, end):
        deliver[i] -= temp
    answer += temp

print(answer)
