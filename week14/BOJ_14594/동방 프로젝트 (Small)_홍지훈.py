import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N: 동아리방의 개수 2 <= N <= 100
M = int(input().rstrip()) # M: 박-종빈빌런의 행동 횟수를 나타내는 음이 아닌 정수 0 <= M <= 100

rooms = [False for _ in range(N + 1)]

for _ in range(M):
  x, y = map(int, input().rstrip().split()) # x, y: 박-종빌런의 행동을 나타내는 양의 정수 1 <= x < y <= N, 행동: x ~ y 방 사이의 벽을 무너뜨리는 것

  opened_rooms = 0

  for idx in range(x, y):
    if not rooms[idx]: rooms[idx] = True

print(rooms.count(False) - 1)