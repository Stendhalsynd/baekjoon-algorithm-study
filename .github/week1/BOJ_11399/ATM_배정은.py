import sys

N = int(sys.stdin.readline().rstrip())
atm_time = sorted(list(map(int, sys.stdin.readline().split()))) # 오름차순 으로 정렬

min_time = 0
for i in range(N):
    min_time += sum(atm_time[:i + 1]) # 필요한 시간의 합의 최솟값

print(min_time)