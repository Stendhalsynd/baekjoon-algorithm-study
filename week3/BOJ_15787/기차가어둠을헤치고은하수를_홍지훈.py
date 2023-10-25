# 구현, 비트마스킹
import sys

# 1번 추가 명령
def addPassenger(cur, p):
  return cur | (1 << p)

# 2번 하차 명령
def deletePassenger(cur, p):
  return cur & ~(1 << p)

# 3번 left shift
def leftShift(cur):
  return (cur << 1) & ~(1 << 20) # 2 ** 19 - 1 와 1 << 20 은 다르다.

# 4번 right shift
def rightShift(cur):
  return cur >> 1

N, M = map(int, sys.stdin.readline().rstrip().split())
trains = [0] * N

for i in range(M):
  commands = list(map(int, sys.stdin.readline().rstrip().split()))

  if commands[0] == 1:
    trainIdx = commands[1] - 1
    passengerIdx = commands[2] - 1
    trains[trainIdx] = addPassenger(trains[trainIdx], passengerIdx)
  elif commands[0] == 2:
    trainIdx = commands[1] - 1
    passengerIdx = commands[2] - 1
    trains[trainIdx] = deletePassenger(trains[trainIdx], passengerIdx)
  elif commands[0] == 3:
    trainIdx = commands[1] - 1
    trains[trainIdx] = leftShift(trains[trainIdx])
  elif commands[0] == 4:
    trainIdx = commands[1] - 1
    trains[trainIdx] = rightShift(trains[trainIdx])

print(len(set(trains)))