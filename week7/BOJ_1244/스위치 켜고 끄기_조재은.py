import sys

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

# 스위치 개수
n = int(input())
# 스위치 상태, 켜저 있으면 1, 꺼져 있으면 0, 사이에는 빈칸
switch = [-1] + list(map(int, input().split()))
# 학생수
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())
    # 남학생 : 받은 수의 배수에 해당하는 모든 스위치를  현재 상태의 반대로 만든다. (꺼져있으면 키고, 켜저있으면 끈다)
    if gender == 1:
        for i in range(num, n+1, num):
            change(i)
    # 여학생 : 받은 수를 중심으로 좌우가 서로 다은 상태일때까지 모든 스위치를 반대로 만든다.
    # ex) 스위치의 상태: [1 1 1 1 0] 이고 주어진 수는 3이면 2,4 번째가 같은 상태미으로 반대로 만들고, 그 이후에 1, 5번째가 다른 상태이므로 여기서 끝낸다.
    # 받은 스위치의 번호를 기준으로 -i와 +i를 비교하여 같으면 스위치의 상태를 반대로 만들어주면 된다.
    else:
        change(num)
        for k in range(n//2):
            if num + k > n or num - k < 1:
                break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

# 출력
for i in range(1, n+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()