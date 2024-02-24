import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N : 수열 A 의 크기 1 ~ 1000
nums = list(map(int, input().rstrip().split())) # 수열 A 를 이루고 있는 배열

dp = [0 for i in range(len(nums))] # dp: nums[i] 를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 합

for end in range(len(nums)):
  for start in range(end + 1):
    if nums[end] > nums[start]: # nums[i]: 현재 위치, nums[j]: 이전 위치
      dp[end] = max(dp[end], dp[start] + nums[end])
    if end == start and dp[end] == 0:
      dp[end] = nums[end]
    
print(max(dp))