import sys
import time

N = int(sys.stdin.readline().rstrip())
meets = []

for _ in range(N):
    meets.append(list(map(int, sys.stdin.readline().split()))) # [회의 시작하는 시간, 끝나는 시간]

meets = sorted(meets, key=lambda x: (x[1], x[0])) # 끝나는 시간 순으로 정렬한 뒤, 같으면 시작하는 시간으로 정렬

max_meet_count = 1
end_time = meets[0][1] # 처음만 확인하면 된다. (제일 끝나는 시간이 이르기 때문)

for i in range(1, N):
    if end_time <= meets[i][0]:
        max_meet_count += 1
        end_time = meets[i][1]

print(max_meet_count)