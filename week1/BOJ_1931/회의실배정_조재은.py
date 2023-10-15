import sys

# 입력값 받기
n = int(input()) # 해야하는 회의
meetings = [] # 회의시간 리스트

# 시작시간, 끝나는 시간 입력받아 리스트에 넣기
for i in range(n):
    start, end = list(map(int, input().split()))
    meetings.append([start, end])

# 2차원 요소를 기준으로 정렬할 때 sorted(list, key = lambda a : (a[m], a[n]))을 사용
meetings.sort(key = lambda a : (a[0], a[1]))

last_time = 0 # 이전 회의의 종료 시간
count = 0 # 회의 개수
print("meetings", meetings)

# meetings 리스트에서 각 회의의 시작 시간(start)과 종료 시간(end)을 순회하며,
# 각 회의에 대한 반복문을 시작.
# 이렇게 하면 각 회의의 시작 시간과 종료 시간을 변수 start와 end에 자동으로 할당
for start, end in meetings:
    if start >= last_time:
        last_time = end # 현재 회의의 종료 시간(end)을 last_time 변수에 할당
        count = count + 1

print(count)
