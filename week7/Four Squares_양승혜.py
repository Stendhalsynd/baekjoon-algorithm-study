# python 3 로도 통과
n = int(input())

numList = [0] * (n + 1)

root = 1
while root <= n:
    if int(root ** 0.5) == root ** 0.5:
        numList[root] = 1
    root += 1

minValue = 4
for i in range(int(n ** 0.5), 0, -1):
    if numList[n]:
        minValue = 1
        break
    elif numList[n - i ** 2]:
        minValue = 2
        break
    else:
        for j in range(int((n - i ** 2) ** 0.5), 0, -1):
            if numList[(n - i ** 2) - j ** 2]:
                minValue = 3
print(minValue)

# pypy로 통과
n = int(input())

numList = [0, 1]

for i in range(2, n + 1):
    min_value = 4
    for j in range(1, int(i ** 0.5) + 1):
        min_value = min(min_value, numList[i - j * j] + 1)
    numList.append(min_value)

print(numList[n])
