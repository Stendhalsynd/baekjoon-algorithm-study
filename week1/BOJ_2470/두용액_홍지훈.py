import sys, bisect

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 오름차순 정렬
nums.sort()

# 투포인터
start, end = 0, N - 1

# 최소쌍
result = []
# 최소합
sum = 2000000000

# 두 포인터로 0에 가장 가까울 경우
while (start < end):
  currentSum = abs(nums[start] + nums[end])
  if currentSum < sum:
    sum = currentSum
    result = [nums[start], nums[end]]
  if nums[start] + nums[end] < 0:
    start += 1
  else:
    end -= 1


print(result[0], result[1])
