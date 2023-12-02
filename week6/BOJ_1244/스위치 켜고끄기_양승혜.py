def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0 

n = int(input())
switch = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, n + 1, number):
            change(i)

    elif gender == 2:
        change(number)
        left, right = number - 1, number + 1
        while left >= 1 and right <= n and switch[left] == switch[right]:
            change(left)
            change(right)
            left, right = left - 1, right + 1

for i in range(1, n + 1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()
