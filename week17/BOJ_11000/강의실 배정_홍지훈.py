import sys, heapq
input = sys.stdin.readline

def calc_classromms(time):
  classrooms = []
  heapq.heappush(classrooms, time[0][1])

  for i in range(1, len(time)):
    s, t = time[i]
    if classrooms[0] <= s:
      heapq.heappop(classrooms)
    heapq.heappush(classrooms, t)

  return len(classrooms)

N = int(input().rstrip()) # N : 수업의 수
time = []
for _ in range(N):
  Si, Ti = map(int, input().rstrip().split())
  time.append([Si, Ti])

time.sort()
print(calc_classromms(time))