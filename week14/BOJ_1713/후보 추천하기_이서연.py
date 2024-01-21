import sys

input = sys.stdin.readline

N = int(input().strip())
C = int(input().strip())

students = list(map(int, input().split()))

candidates = []
cnt = [0] * N

for i in students:
    if candidates.count(i) != 0:
        cnt[candidates.index(i)] += 1
    else:
        if len(candidates) < N:
            candidates.append(i)
            cnt[candidates.index(i)] = 1
        else:
            idx = cnt.index(min(cnt))
            candidates.pop(idx)
            candidates.append(i)
            cnt.pop(idx)
            cnt.append(1)

candidates.sort()

for i in candidates:
    print(i, end = " ")