# 구현, 그리디 알고리즘, 정렬 3:44
import sys

N = int(sys.stdin.readline().rstrip()) # 일정의 개수

schedule = []

for i in range(N):
  S, E = map(int, sys.stdin.readline().rstrip().split()) # 일정의 시작 날짜, 종료 날짜
  schedule.append([S, E])

schedule.sort() # 일정 시작일 기준으로 정렬

# data - 각 날짜별 겹치는 일정의 수를 카운트한 dictionary
data = {}
start, maxEnd = schedule[0]
for i in range(start, maxEnd + 1):
  data[i] = 1

for item in schedule[1:]:
  for key in range(item[0], item[1] + 1):
    if key not in data:
      data[key] = 1
    else:
      data[key] += 1

# 각 data 를 순회하며 연속인 키가 나오는 동안엔 strike 를 카운트하고 
# 그 외의 상황엔 이전까지 누적된 최대 중첩 일정수와 연속수를 곱해 합계 sumVal 에 더한다.
start = 0
strike = 0
maxVal = 0
sumVal = 0
for key in data:  
  maxVal = max(data[key], maxVal)
  if start == 0 or start + 1 == key:
    strike += 1
    
  elif start + 1 < key:
    sumVal += strike * maxVal
    strike = 1
    maxVal = data[key]
  start = key

# 만약 마지막 일정구간이 남아있었다면 해당 구간을 커버하는 코팅지의 면적을 구해 더한다.
if maxVal != 0 and strike != 0:
  sumVal += strike * maxVal

print(sumVal)