import sys

n, m = map(int, input().split()) #기차의 수 n, 명령어의 수 m
train = [[0 for _ in range(20)] for _ in range(n)] #기차 각각을 원소 20개를 가진 리스트로 생성

for i in range(m):
    a = list(map(int, input().split())) # 명령
    if a[0] == 1:
        train[a[1] - 1][a[2] - 1] = 1
    elif a[0] == 2:
        train[a[1] - 1][a[2] - 1] = 0 # 하차
    elif a[0] == 3:
        for j in range(m-1):
            train[a[1] - 1][j] = train[a[1] - 1][j - 1]
        train[a[1] - 1][0] = 0
    elif a[0] == 4:
        for j in range(m-1):
            train[a[1] - 1][j] = train[a[1] - 1][j + 1]
        train[a[1] - 1][19] = 0

cnt = 0
state =[]
# 은하수를 통과한 기차의 상태를 저장하는 리스트 state를 만들고,
# for문을 기차 수만큼 돌려서 i번째 기차의 상태가 state에 없다면 state에 삽입하고 cnt += 1
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)

