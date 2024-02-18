import sys
input = sys.stdin.readline

weight = []
answer = 0
N = int(input().rstrip())
for _ in range(N):
  weight.append(int(input().rstrip()))

weight.sort()

for i in range(1, N + 1):
  if weight[-i] * i > answer: answer = weight[-i] * i

print(answer)