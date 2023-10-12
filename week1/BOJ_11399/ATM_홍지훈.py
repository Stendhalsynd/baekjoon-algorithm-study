N = int(input()) # 사람의 수 1 ~ 1000
P = [int(x) for x in input().split()] # 인출하는데 걸리는 시간 1 ~ 1000

# i 번째 사람이 돈을 인출하는데 걸리는 시간 Pi

P.sort()
sum = 0

for i in range(0, N):
  sum += P[i] * ( N - i )

print(sum)