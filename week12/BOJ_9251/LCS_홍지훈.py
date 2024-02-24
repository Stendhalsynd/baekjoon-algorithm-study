import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]


for i in range(1, len(str1) + 1):
  for j in range(1, len(str2) + 1):
    if str1[i - 1] == str2[j - 1]:
      dp[i][j] = dp[i- 1][j - 1] + 1 # 각 위치의 문자가 동일하면 각 문자열에서 해당 문자를 제외하고 다시 dp를 하고 구하고자 하는 공통 부분 수열 문자열의 길이는 1 증가
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # 만약 각 위치의 문자가 다르다면 해당 문자를 제외하고 다시 dp
    
print(dp[len(str1)][len(str2)])