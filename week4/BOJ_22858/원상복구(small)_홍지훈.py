# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

Si = list(map(int, input().rstrip().split()))
Di = list(map(int, input().rstrip().split()))

P = [0] * N

for _ in range(K):
  for idx, val in enumerate(Si):
    P[Di[idx]-1] = val
  Si = P[:]

for val in P:
  print(val, end=' ')
print()