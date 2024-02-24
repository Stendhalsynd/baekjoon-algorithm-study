n = int(input())
array = list(map(int, input().split()))
dp = array[:]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[j] + array[i], dp[i])

print(max(dp))
