from itertools import combinations

n, l, r, x = map(int, input().split())
tasks = list(map(int, input().split()))

count = 0
for i in range(2, n + 1):
    cases = list(combinations(tasks, i))
    for case in cases:
        if l <= sum(case) <= r and (max(case) - min(case)) >= x:
            count += 1
print(count)
