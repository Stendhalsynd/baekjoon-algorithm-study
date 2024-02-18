n = int(input())
distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

answer = 0
curr = costs[0]

for i in range(n - 1):
    if costs[i] < curr:
        curr = costs[i]
    answer += curr * distance[i]

print(answer)
