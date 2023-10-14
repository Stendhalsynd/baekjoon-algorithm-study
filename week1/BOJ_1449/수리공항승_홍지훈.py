import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 오름차순 정렬
nums.sort()

count = 1
cur = nums[0] + L - 1

for num in nums:
  if num > cur:
    count += 1
    cur = num + L - 1

print(count)