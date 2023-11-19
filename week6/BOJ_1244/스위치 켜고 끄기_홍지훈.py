import sys
input = sys.stdin.readline

N = int(input()) # N : 스위치 개수 <= 100 양의 정수
states = list(map(int,input().rstrip().split())) # 상태 1 : 켜짐, 0: 꺼짐
M = int(input()) # M : 학생 수 <= 100 양의 정수

def convert(states, idx):
    if states[idx] == 0:
      states[idx] = 1
    else:
      states[idx] = 0

for _ in range(M):
  student, num = map(int, input().rstrip().split()) # student = 1 : 남학생, 2 : 여학생
  
  # 1) 남학생
  if student == 1:
    for idx, val in enumerate(states):
      if (idx + 1) % num == 0:
        convert(states, idx)

  # 2) 여학생
  else:
    convert(states, num - 1)
    if 1 < num < N:
      bef = num - 2
      aft = num
      
      while 0 <= bef and aft <= N - 1 and states[bef] == states[aft]:
        convert(states, bef)
        convert(states, aft)
        bef -= 1
        aft += 1

for idx, val in enumerate(states):
  print(val, end=' ')
  if idx > 0 and (idx + 1) % 20 == 0:
    print()