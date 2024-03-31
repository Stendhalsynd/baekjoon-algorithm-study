import sys
from itertools import permutations

input = sys.stdin.readline

A, B = map(int, input().split())
C = 0

temp = list(str(A))

for i in permutations(temp, len(temp)):
    result = int("".join(list(i)))

    if i[0] != "0" and result < B:
        C = max(C, result)

if C == 0:
    print(-1)
else:
    print(C)
