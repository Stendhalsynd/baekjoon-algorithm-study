import sys

N = int(sys.stdin.readline().rstrip())
time = []

for i in range(N):
  start, end = map(int, sys.stdin.readline().rstrip().split())
  time.append([start, end])

time.sort(key = lambda x: (x[1], x[0]))

end = time[0][1]
count = 1

for i in range(1, N):
  if time[i][0] >= end or time[i][0] == time[i][1]:
    count += 1
    end = time[i][1]

print(count)