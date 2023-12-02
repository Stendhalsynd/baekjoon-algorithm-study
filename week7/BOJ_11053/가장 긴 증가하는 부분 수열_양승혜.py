n = int(input())
numList = list(map(int, input().split()))
count = [1] * n

for i in range(1, len(numList)):
    for j in range(i):
        if numList[i] > numList[j]:
            count[i] = max(count[i], count[j] + 1)

print(max(count))
