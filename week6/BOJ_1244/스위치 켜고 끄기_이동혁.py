n = int(input())
switch = [None] + list(map(int, input().split()))
s = int(input())

for _ in range(s):
    sex, num = map(int, input().split())

    if sex == 1: # 남학생
        i = 1
        while num * i <= n:
            switch[num * i] = 1 - switch[num * i]
            i += 1
        
    if sex == 2: # 여학생
        left, right = num, num
        while True:
            if left - 1 < 1 or right + 1 > n:
                break
            if switch[left - 1] == switch[right + 1]:
                left = left - 1
                right = right + 1
            else:
                break

        for j in range(left, right+1):
            switch[j] = 1 - switch[j]

switch = switch[1:]
while True:
    if len(switch) <= 20:
        print(" ".join(map(str, switch)))
        break
    else:
        print(" ".join(map(str, switch[0:20])))
        switch = switch[20:]